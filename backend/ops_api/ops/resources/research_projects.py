from flask import Response, jsonify, request
from models.base import BaseModel
from models.cans import CANFiscalYear
from models.research_projects import ResearchProject
from ops_api.ops import db
from ops_api.ops.base_views import BaseItemAPI, BaseListAPI
from sqlalchemy.future import select
from typing_extensions import override


class ResearchProjectItemAPI(BaseItemAPI):
    def __init__(self, model: BaseModel):
        super().__init__(model)

    @override
    def _get_item(self, id: int) -> ResearchProject:
        research_project = self.model.query.filter_by(id=id).first_or_404()
        return research_project

    @override
    def get(self, id: int) -> Response:
        research_project = self._get_item(id)
        response = jsonify(research_project.to_dict())
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response


class ResearchProjectListAPI(BaseListAPI):
    def __init__(self, model: BaseModel):
        super().__init__(model)

    @staticmethod
    def get_query(fiscal_year=None, portfolio_id=None, search=None):
        stmt = (
            select(ResearchProject)
            .distinct(ResearchProject.id)
            .join(ResearchProject.cans, isouter=True)
            .join(CANFiscalYear, isouter=True)
        )

        if portfolio_id:
            stmt = stmt.where(ResearchProject.portfolio_id == portfolio_id)

        if fiscal_year:
            stmt = stmt.where(CANFiscalYear.fiscal_year == fiscal_year)

        if search:
            stmt = stmt.where(ResearchProject.title.ilike(f"%{search}%"))

        return stmt

    def get(self) -> Response:
        fiscal_year = request.args.get("fiscal_year")
        portfolio_id = request.args.get("portfolio_id")
        search = request.args.get("search")

        stmt = ResearchProjectListAPI.get_query(fiscal_year, portfolio_id, search)

        result = db.session.execute(stmt).all()

        return jsonify([i.to_dict() for item in result for i in item])
