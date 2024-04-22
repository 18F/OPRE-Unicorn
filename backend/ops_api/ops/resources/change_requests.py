import copy
from datetime import datetime

import marshmallow_dataclass as mmdc
from flask import Response, current_app, request
from flask_jwt_extended import verify_jwt_in_request
from sqlalchemy import select
from typing_extensions import override

from models import BudgetLineItem, BudgetLineItemChangeRequest, ChangeRequest, ChangeRequestStatus
from ops_api.ops.base_views import BaseListAPI, handle_api_error
from ops_api.ops.resources import budget_line_items
from ops_api.ops.resources.budget_line_items import validate_and_prepare_change_data
from ops_api.ops.schemas.budget_line_items import PATCHRequestBody
from ops_api.ops.utils.auth import Permission, PermissionType, is_authorized
from ops_api.ops.utils.response import make_response_with_headers
from ops_api.ops.utils.user import get_user_from_token


def review_change_request(
    change_request_id: int, status_after_review: ChangeRequestStatus, reviewed_by_user_id: int
) -> ChangeRequest:
    session = current_app.db_session
    change_request = session.get(ChangeRequest, change_request_id)
    change_request.reviewed_by_id = reviewed_by_user_id
    change_request.reviewed_on = datetime.now()
    change_request.status = status_after_review

    # If approved, then apply the changes
    if status_after_review == ChangeRequestStatus.APPROVED:
        if isinstance(change_request, BudgetLineItemChangeRequest):
            budget_line_item = session.get(BudgetLineItem, change_request.budget_line_item_id)
            # need to copy to avoid changing the original data in the ChangeRequest and triggering an update
            data = copy.deepcopy(change_request.requested_changes)
            schema = mmdc.class_schema(PATCHRequestBody)()
            schema.context["id"] = change_request.budget_line_item_id
            schema.context["method"] = "PATCH"

            change_data, changing_from_data = validate_and_prepare_change_data(
                data,
                budget_line_item,
                schema,
                ["id", "status", "agreement_id"],
                partial=False,
            )

            budget_line_items.update_data(budget_line_item, change_data)
            session.add(budget_line_item)

    session.add(change_request)
    session.commit()
    return change_request


# TODO: Implement the queries needs for the For Approvals page, for now it's just a placeholder
class ChangeRequestListAPI(BaseListAPI):
    def __init__(self, model: ChangeRequest = ChangeRequest):
        super().__init__(model)

    @override
    @is_authorized(PermissionType.GET, Permission.CHANGE_REQUEST)
    @handle_api_error
    def get(self) -> Response:
        print("~~~GET ChangeRequestListAPI~~~")
        limit = request.args.get("limit", 10, type=int)
        offset = request.args.get("offset", 0, type=int)
        # status = request.args.get("status", ChangeRequestStatus.IN_REVIEW, type=lambda x: ChangeRequestStatus[x])
        # status = request.args.get("status", "IN_REVIEW", type=str)
        # agreement_id = request.args.get("agreement_id", None, type=int)
        # budget_line_item_id = request.args.get("budget_line_item_id", None, type=int)

        stmt = select(ChangeRequest).where(ChangeRequest.status == ChangeRequestStatus.IN_REVIEW)
        # if agreement_id:
        #     stmt = stmt.where(ChangeRequest.agreement_id == agreement_id)
        # if budget_line_item_id:
        #     stmt = stmt.where(ChangeRequest.budget_line_item_id == budget_line_item_id)
        # stmt = stmt.order_by(ChangeRequest.created_on.desc())
        stmt = stmt.limit(limit)
        if offset:
            stmt = stmt.offset(int(offset))
        print("~~~stmt~~~", str(stmt))
        results = current_app.db_session.execute(stmt).all()
        change_requests = [row[0] for row in results] if results else None
        if change_requests:
            response = make_response_with_headers([change_request.to_dict() for change_request in change_requests])
        else:
            # response = make_response_with_headers({}, 404)
            response = make_response_with_headers([], 200)
        return response


class ChangeRequestReviewAPI(BaseListAPI):
    def __init__(self, model: ChangeRequest = ChangeRequest):
        super().__init__(model)
        # self._response_schema = ContractAgreementResponse()
        # self._response_schema_collection = ContractAgreementResponse(many=True)

    @is_authorized(PermissionType.POST, Permission.CHANGE_REQUEST_REVIEW)
    def post(self) -> Response:
        request_json = request.get_json()
        change_request_id = request_json.get("change_request_id")
        action = request_json.get("action", "").upper()
        if action == "APPROVE":
            status_after_review = ChangeRequestStatus.APPROVED
        elif action == "REJECT":
            status_after_review = ChangeRequestStatus.REJECTED
        else:
            raise ValueError(f"Invalid action: {action}")

        # schema = mmdc.class_schema(ChangeRequestReviewRequest)()
        # schema.context["method"] = "POST"
        # data = schema.load(request_json, unknown=EXCLUDE)
        # change_request_id = data["change_request_id"]
        # status_after_review = data["status"]

        token = verify_jwt_in_request()
        user = get_user_from_token(token[1])
        reviewed_by_user_id = user.id

        change_request = review_change_request(change_request_id, status_after_review, reviewed_by_user_id)

        return make_response_with_headers(change_request.to_dict(), 200)

    # @override
    # @is_authorized(PermissionType.POST, Permission.BUDGET_LINE_ITEM)
    # @handle_api_error
    # def post(self) -> Response:
    #     message_prefix = f"POST to {ENDPOINT_STRING}"
    #     with OpsEventHandler(OpsEventType.CREATE_BLI) as meta:
    #         self._post_schema.context["method"] = "POST"
    #
    #         data = self._post_schema.dump(self._post_schema.load(request.json))
    #         data["status"] = BudgetLineItemStatus[data["status"]] if data.get("status") else None
    #         data = convert_date_strings_to_dates(data)
    #
    #         new_bli = BudgetLineItem(**data)
    #
    #         current_app.db_session.add(new_bli)
    #         current_app.db_session.commit()
    #
    #         new_bli_dict = self._response_schema.dump(new_bli)
    #         meta.metadata.update({"new_bli": new_bli_dict})
    #         current_app.logger.info(f"{message_prefix}: New BLI created: {new_bli_dict}")
    #
    #         return make_response_with_headers(new_bli_dict, 201)
