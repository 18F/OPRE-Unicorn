from flask import Blueprint

from ops_api.ops.views import (
    ADMINISTRATIVE_AND_SUPPORT_PROJECT_ITEM_API_VIEW_FUNC,
    ADMINISTRATIVE_AND_SUPPORT_PROJECT_LIST_API_VIEW_FUNC,
    AGREEMENT_HISTORY_LIST_API_VIEW_FUNC,
    AGREEMENT_ITEM_API_VIEW_FUNC,
    AGREEMENT_LIST_API_VIEW_FUNC,
    AGREEMENT_REASON_LIST_API_VIEW_FUNC,
    AGREEMENT_TYPE_LIST_API_VIEW_FUNC,
    AZURE_SAS_TOKEN_VIEW_FUNC,
    BUDGET_LINE_ITEMS_ITEM_API_VIEW_FUNC,
    BUDGET_LINE_ITEMS_LIST_API_VIEW_FUNC,
    CAN_FUNDING_BUDGET_ITEM_API_VIEW_FUNC,
    CAN_FUNDING_BUDGET_LIST_API_VIEW_FUNC,
    CAN_FUNDING_DETAILS_ITEM_API_VIEW_FUNC,
    CAN_FUNDING_DETAILS_LIST_API_VIEW_FUNC,
    CAN_FUNDING_RECEIVED_ITEM_API_VIEW_FUNC,
    CAN_FUNDING_RECEIVED_LIST_API_VIEW_FUNC,
    CAN_FUNDING_SUMMARY_LIST_API_VIEW_FUNC,
    CAN_HISTORY_LIST_API_VIEW_FUNC,
    CAN_ITEM_API_VIEW_FUNC,
    CAN_LIST_API_VIEW_FUNC,
    CANS_BY_PORTFOLIO_API_VIEW_FUNC,
    CHANGE_REQUEST_LIST_API_VIEW_FUNC,
    CHANGE_REQUEST_REVIEW_API_VIEW_FUNC,
    CONTRACT_ITEM_API_VIEW_FUNC,
    CONTRACT_LIST_API_VIEW_FUNC,
    DIVISIONS_ITEM_API_VIEW_FUNC,
    DIVISIONS_LIST_API_VIEW_FUNC,
    DOCUMENT_API_FUNC,
    HEALTH_CHECK_VIEW_FUNC,
    NOTIFICATIONS_ITEM_API_VIEW_FUNC,
    NOTIFICATIONS_LIST_API_VIEW_FUNC,
    OPS_DB_HISTORY_LIST_API_VIEW_FUNC,
    PORTFOLIO_CALCULATE_FUNDING_API_VIEW_FUNC,
    PORTFOLIO_CANS_API_VIEW_FUNC,
    PORTFOLIO_FUNDING_SUMMARY_ITEM_API_VIEW_FUNC,
    PORTFOLIO_ITEM_API_VIEW_FUNC,
    PORTFOLIO_LIST_API_VIEW_FUNC,
    PORTFOLIO_STATUS_ITEM_API_VIEW_FUNC,
    PORTFOLIO_STATUS_LIST_API_VIEW_FUNC,
    PROCUREMENT_ACQUISITION_PLANNING_ITEM_API_VIEW_FUNC,
    PROCUREMENT_AWARD_ITEM_API_VIEW_FUNC,
    PROCUREMENT_EVALUATION_ITEM_API_VIEW_FUNC,
    PROCUREMENT_PRE_AWARD_ITEM_API_VIEW_FUNC,
    PROCUREMENT_PRE_SOLICITATION_ITEM_API_VIEW_FUNC,
    PROCUREMENT_SHOPS_ITEM_API_VIEW_FUNC,
    PROCUREMENT_SHOPS_LIST_API_VIEW_FUNC,
    PROCUREMENT_SOLICITATION_ITEM_API_VIEW_FUNC,
    PROCUREMENT_STEP_LIST_API_VIEW_FUNC,
    PRODUCT_SERVICE_CODE_ITEM_API_VIEW_FUNC,
    PRODUCT_SERVICE_CODE_LIST_API_VIEW_FUNC,
    PROJECT_ITEM_API_VIEW_FUNC,
    PROJECT_LIST_API_VIEW_FUNC,
    RESEARCH_PROJECT_FUNDING_SUMMARY_LIST_API_VIEW_FUNC,
    RESEARCH_PROJECT_ITEM_API_VIEW_FUNC,
    RESEARCH_PROJECT_LIST_API_VIEW_FUNC,
    RESEARCH_TYPE_LIST_API_VIEW_FUNC,
    SERVICES_COMPONENT_ITEM_API_VIEW_FUNC,
    SERVICES_COMPONENT_LIST_API_VIEW_FUNC,
    USERS_ITEM_API_VIEW_FUNC,
    USERS_LIST_API_VIEW_FUNC,
    VERSION_API_VIEW_FUNC,
)

# Ideas from Flask docs: https://flask.palletsprojects.com/en/2.2.x/views/#method-dispatching-and-apis


def register_api(api_bp: Blueprint) -> None:
    api_bp.add_url_rule(
        "/health/",
        view_func=HEALTH_CHECK_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/azure/sas-token/",
        view_func=AZURE_SAS_TOKEN_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/portfolios/<int:id>/calcFunding/",
        view_func=PORTFOLIO_CALCULATE_FUNDING_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/portfolios/<int:id>/cans/",
        view_func=PORTFOLIO_CANS_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/portfolios/<int:id>",
        view_func=PORTFOLIO_ITEM_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/portfolios/",
        view_func=PORTFOLIO_LIST_API_VIEW_FUNC,
    )

    api_bp.add_url_rule(
        "/cans/<int:id>",
        view_func=CAN_ITEM_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/cans/",
        view_func=CAN_LIST_API_VIEW_FUNC,
    )

    api_bp.add_url_rule("/can-funding-budgets/<int:id>", view_func=CAN_FUNDING_BUDGET_ITEM_API_VIEW_FUNC)

    api_bp.add_url_rule("/can-funding-budgets/", view_func=CAN_FUNDING_BUDGET_LIST_API_VIEW_FUNC)

    api_bp.add_url_rule("/can-funding-details/<int:id>", view_func=CAN_FUNDING_DETAILS_ITEM_API_VIEW_FUNC)

    api_bp.add_url_rule("/can-funding-details/", view_func=CAN_FUNDING_DETAILS_LIST_API_VIEW_FUNC)

    api_bp.add_url_rule(
        "/can-funding-received/",
        view_func=CAN_FUNDING_RECEIVED_LIST_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/can-funding-received/<int:id>",
        view_func=CAN_FUNDING_RECEIVED_ITEM_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/ops-db-histories/",
        view_func=OPS_DB_HISTORY_LIST_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/cans/portfolio/<int:id>",
        view_func=CANS_BY_PORTFOLIO_API_VIEW_FUNC,
    )

    api_bp.add_url_rule(
        "/budget-line-items/<int:id>",
        view_func=BUDGET_LINE_ITEMS_ITEM_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/budget-line-items/",
        view_func=BUDGET_LINE_ITEMS_LIST_API_VIEW_FUNC,
    )

    api_bp.add_url_rule(
        "/procurement-shops/<int:id>",
        view_func=PROCUREMENT_SHOPS_ITEM_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/procurement-shops/",
        view_func=PROCUREMENT_SHOPS_LIST_API_VIEW_FUNC,
    )

    api_bp.add_url_rule(
        "/portfolio-status/<int:id>",
        view_func=PORTFOLIO_STATUS_ITEM_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/portfolio-status/",
        view_func=PORTFOLIO_STATUS_LIST_API_VIEW_FUNC,
    )

    api_bp.add_url_rule(
        "/divisions/<int:id>",
        view_func=DIVISIONS_ITEM_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/divisions/",
        view_func=DIVISIONS_LIST_API_VIEW_FUNC,
    )

    api_bp.add_url_rule(
        "/users/<int:id>",
        view_func=USERS_ITEM_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/users/",
        view_func=USERS_LIST_API_VIEW_FUNC,
    )

    api_bp.add_url_rule(
        "/can-funding-summary",
        view_func=CAN_FUNDING_SUMMARY_LIST_API_VIEW_FUNC,
    )

    api_bp.add_url_rule("/can-history/", view_func=CAN_HISTORY_LIST_API_VIEW_FUNC)
    api_bp.add_url_rule(
        "/portfolio-funding-summary/<int:id>",
        view_func=PORTFOLIO_FUNDING_SUMMARY_ITEM_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/research-project-funding-summary/",
        view_func=RESEARCH_PROJECT_FUNDING_SUMMARY_LIST_API_VIEW_FUNC,
    )

    api_bp.add_url_rule(
        "/projects/<int:id>",
        view_func=PROJECT_ITEM_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/projects/",
        view_func=PROJECT_LIST_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/research-projects/<int:id>",
        view_func=RESEARCH_PROJECT_ITEM_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/research-projects/",
        view_func=RESEARCH_PROJECT_LIST_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/administrative-and-support-projects/<int:id>",
        view_func=ADMINISTRATIVE_AND_SUPPORT_PROJECT_ITEM_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/administrative-and-support-projects/",
        view_func=ADMINISTRATIVE_AND_SUPPORT_PROJECT_LIST_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/research-types/",
        view_func=RESEARCH_TYPE_LIST_API_VIEW_FUNC,
    )

    api_bp.add_url_rule(
        "/agreements/<int:id>",
        view_func=AGREEMENT_ITEM_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/agreements/",
        view_func=AGREEMENT_LIST_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/agreement-history/<int:id>",
        view_func=AGREEMENT_HISTORY_LIST_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/agreement-reasons/",
        view_func=AGREEMENT_REASON_LIST_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/agreement-types/",
        view_func=AGREEMENT_TYPE_LIST_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/contracts/<int:id>",
        view_func=CONTRACT_ITEM_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/contracts/",
        view_func=CONTRACT_LIST_API_VIEW_FUNC,
    )

    api_bp.add_url_rule(
        "/product-service-codes/",
        view_func=PRODUCT_SERVICE_CODE_LIST_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/product-service-codes/<int:id>",
        view_func=PRODUCT_SERVICE_CODE_ITEM_API_VIEW_FUNC,
    )

    api_bp.add_url_rule(
        "/notifications/",
        view_func=NOTIFICATIONS_LIST_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/notifications/<int:id>",
        view_func=NOTIFICATIONS_ITEM_API_VIEW_FUNC,
    )

    api_bp.add_url_rule(
        "/services-components/<int:id>",
        view_func=SERVICES_COMPONENT_ITEM_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/services-components/",
        view_func=SERVICES_COMPONENT_LIST_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/procurement-steps/",
        view_func=PROCUREMENT_STEP_LIST_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/procurement-acquisition-plannings/<int:id>",
        view_func=PROCUREMENT_ACQUISITION_PLANNING_ITEM_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/procurement-pre-solicitations/<int:id>",
        view_func=PROCUREMENT_PRE_SOLICITATION_ITEM_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/procurement-solicitations/<int:id>",
        view_func=PROCUREMENT_SOLICITATION_ITEM_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/procurement-evaluations/<int:id>",
        view_func=PROCUREMENT_EVALUATION_ITEM_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/procurement-pre-awards/<int:id>",
        view_func=PROCUREMENT_PRE_AWARD_ITEM_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/procurement-awards/<int:id>",
        view_func=PROCUREMENT_AWARD_ITEM_API_VIEW_FUNC,
    )
    # Add a new URL rule for the version endpoint
    api_bp.add_url_rule(
        "/version/",
        view_func=VERSION_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/change-requests/",
        view_func=CHANGE_REQUEST_LIST_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/change-request-reviews/",
        view_func=CHANGE_REQUEST_REVIEW_API_VIEW_FUNC,
    )
    api_bp.add_url_rule(
        "/documents/<int:agreement_id>",
        view_func=DOCUMENT_API_FUNC,
    )
    api_bp.add_url_rule(
        "/documents/",
        view_func=DOCUMENT_API_FUNC,
    )
    api_bp.add_url_rule(
        "/documents/<string:document_id>/status/",
        view_func=DOCUMENT_API_FUNC,
    )
