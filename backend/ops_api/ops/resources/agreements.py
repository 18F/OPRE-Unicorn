from flask import Response, current_app, jsonify, request
from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity, jwt_required
from models.base import BaseModel
from models.cans import Agreement, AgreementReason, AgreementType
from ops_api.ops.base_views import BaseItemAPI, BaseListAPI
from ops_api.ops.utils.query_helpers import QueryHelper
from ops_api.ops.utils.response import make_response_with_headers
from sqlalchemy.future import select
from typing_extensions import override


class AgreementItemAPI(BaseItemAPI):
    def __init__(self, model: BaseModel = Agreement):
        super().__init__(model)

    @override
    @jwt_required()
    def get(self, id: int) -> Response:
        identity = get_jwt_identity()
        is_authorized = self.auth_gateway.is_authorized(identity, ["GET_AGREEMENT"])

        if is_authorized:
            response = self._get_item_with_try(id)
        else:
            response = make_response_with_headers({}, 401)

        return response


class AgreementListAPI(BaseListAPI):
    def __init__(self, model: BaseModel = Agreement):
        super().__init__(model)

    @staticmethod
    def _get_query(search=None, research_project_id=None):
        stmt = select(Agreement).order_by(Agreement.id)
        query_helper = QueryHelper(stmt)

        if search is not None and len(search) == 0:
            query_helper.return_none()
        elif search:
            query_helper.add_search(Agreement.name, search)

        if research_project_id:
            query_helper.add_column_equals(Agreement.research_project_id, research_project_id)

        stmt = query_helper.get_stmt()
        current_app.logger.debug(f"SQL: {stmt}")

        return stmt

    @override
    @jwt_required()
    def get(self) -> Response:
        identity = get_jwt_identity()
        is_authorized = self.auth_gateway.is_authorized(identity, ["GET_AGREEMENTS"])

        if is_authorized:
            search = request.args.get("search")
            research_project_id = request.args.get("research_project_id")

            stmt = self._get_query(search, research_project_id)

            result = current_app.db_session.execute(stmt).all()
            response = make_response_with_headers([i.to_dict() for item in result for i in item])
        else:
            response = make_response_with_headers({}, 401)

        return response


class AgreementReasonListAPI(MethodView):
    def get(self) -> Response:
        reasons = [item.name for item in AgreementReason]
        return jsonify(reasons)


class AgreementTypeListAPI(MethodView):
    def get(self) -> Response:
        return jsonify([e.name for e in AgreementType])
