"""add updated_by to BaseModel

Revision ID: 95e0429b780a
Revises: 7b0f215948a8
Create Date: 2024-03-20 20:19:49.019176+00:00

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "95e0429b780a"
down_revision: Union[str, None] = "6c85c1668a9f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("agreement", sa.Column("updated_by", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "agreement", "user", ["updated_by"], ["id"])
    op.add_column(
        "agreement_team_members", sa.Column("updated_by", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(
        None, "agreement_team_members", "user", ["updated_by"], ["id"]
    )
    op.add_column(
        "agreement_team_members_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "agreement_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "budget_line_item", sa.Column("updated_by", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(None, "budget_line_item", "user", ["updated_by"], ["id"])
    op.add_column(
        "budget_line_item_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column("can", sa.Column("updated_by", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "can", "user", ["updated_by"], ["id"])
    op.add_column(
        "can_fiscal_year", sa.Column("updated_by", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(None, "can_fiscal_year", "user", ["updated_by"], ["id"])
    op.add_column(
        "can_fiscal_year_carry_forward",
        sa.Column("updated_by", sa.Integer(), nullable=True),
    )
    op.create_foreign_key(
        None, "can_fiscal_year_carry_forward", "user", ["updated_by"], ["id"]
    )
    op.add_column(
        "can_fiscal_year_carry_forward_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "can_fiscal_year_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "can_funding_sources", sa.Column("updated_by", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(None, "can_funding_sources", "user", ["updated_by"], ["id"])
    op.add_column(
        "can_funding_sources_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "can_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column("clin", sa.Column("updated_by", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "clin", "user", ["updated_by"], ["id"])
    op.add_column(
        "clin_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column("contact", sa.Column("updated_by", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "contact", "user", ["updated_by"], ["id"])
    op.add_column(
        "contact_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column("division", sa.Column("updated_by", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "division", "user", ["updated_by"], ["id"])
    op.add_column(
        "division_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "funding_partner", sa.Column("updated_by", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(None, "funding_partner", "user", ["updated_by"], ["id"])
    op.add_column(
        "funding_partner_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "funding_source", sa.Column("updated_by", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(None, "funding_source", "user", ["updated_by"], ["id"])
    op.add_column(
        "funding_source_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column("group", sa.Column("updated_by", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "group", "user", ["updated_by"], ["id"])
    op.add_column(
        "group_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column("notification", sa.Column("updated_by", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "notification", "user", ["updated_by"], ["id"])
    op.add_column(
        "notification_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "ops_db_history", sa.Column("updated_by", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(None, "ops_db_history", "user", ["updated_by"], ["id"])
    op.add_column(
        "ops_db_history_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column("ops_event", sa.Column("updated_by", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "ops_event", "user", ["updated_by"], ["id"])
    op.add_column(
        "ops_event_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column("package", sa.Column("updated_by", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "package", "user", ["updated_by"], ["id"])
    op.add_column(
        "package_snapshot", sa.Column("updated_by", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(None, "package_snapshot", "user", ["updated_by"], ["id"])
    op.add_column(
        "package_snapshot_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "package_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column("portfolio", sa.Column("updated_by", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "portfolio", "user", ["updated_by"], ["id"])
    op.add_column(
        "portfolio_team_leaders", sa.Column("updated_by", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(
        None, "portfolio_team_leaders", "user", ["updated_by"], ["id"]
    )
    op.add_column(
        "portfolio_team_leaders_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column("portfolio_url", sa.Column("updated_by", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "portfolio_url", "user", ["updated_by"], ["id"])
    op.add_column(
        "portfolio_url_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "portfolio_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "procurement_shop", sa.Column("updated_by", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(None, "procurement_shop", "user", ["updated_by"], ["id"])
    op.add_column(
        "procurement_shop_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "procurement_step", sa.Column("updated_by", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(None, "procurement_step", "user", ["updated_by"], ["id"])
    op.add_column(
        "procurement_step_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "product_service_code", sa.Column("updated_by", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(None, "product_service_code", "user", ["updated_by"], ["id"])
    op.add_column(
        "product_service_code_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column("project", sa.Column("updated_by", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "project", "user", ["updated_by"], ["id"])
    op.add_column("project_cans", sa.Column("updated_by", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "project_cans", "user", ["updated_by"], ["id"])
    op.add_column(
        "project_cans_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "project_team_leaders", sa.Column("updated_by", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(None, "project_team_leaders", "user", ["updated_by"], ["id"])
    op.add_column(
        "project_team_leaders_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "project_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column("role", sa.Column("updated_by", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "role", "user", ["updated_by"], ["id"])
    op.add_column(
        "role_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "services_component", sa.Column("updated_by", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(None, "services_component", "user", ["updated_by"], ["id"])
    op.add_column(
        "services_component_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "shared_portfolio_cans", sa.Column("updated_by", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(None, "shared_portfolio_cans", "user", ["updated_by"], ["id"])
    op.add_column(
        "shared_portfolio_cans_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "step_approvers", sa.Column("updated_by", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(None, "step_approvers", "user", ["updated_by"], ["id"])
    op.add_column(
        "step_approvers_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column("user", sa.Column("updated_by", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "user", "user", ["updated_by"], ["id"])
    op.add_column("user_group", sa.Column("updated_by", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "user_group", "user", ["updated_by"], ["id"])
    op.add_column(
        "user_group_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column("user_role", sa.Column("updated_by", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "user_role", "user", ["updated_by"], ["id"])
    op.add_column(
        "user_role_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "user_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column("vendor", sa.Column("updated_by", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "vendor", "user", ["updated_by"], ["id"])
    op.add_column(
        "vendor_contacts", sa.Column("updated_by", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(None, "vendor_contacts", "user", ["updated_by"], ["id"])
    op.add_column(
        "vendor_contacts_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "vendor_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "workflow_instance", sa.Column("updated_by", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(None, "workflow_instance", "user", ["updated_by"], ["id"])
    op.add_column(
        "workflow_instance_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "workflow_step_dependency", sa.Column("updated_by", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(
        None, "workflow_step_dependency", "user", ["updated_by"], ["id"]
    )
    op.add_column(
        "workflow_step_dependency_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "workflow_step_template", sa.Column("updated_by", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(
        None, "workflow_step_template", "user", ["updated_by"], ["id"]
    )
    op.add_column(
        "workflow_step_template_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "workflow_template", sa.Column("updated_by", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(None, "workflow_template", "user", ["updated_by"], ["id"])
    op.add_column(
        "workflow_template_version",
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("workflow_template_version", "updated_by")
    op.drop_constraint(None, "workflow_template", type_="foreignkey")
    op.drop_column("workflow_template", "updated_by")
    op.drop_column("workflow_step_template_version", "updated_by")
    op.drop_constraint(None, "workflow_step_template", type_="foreignkey")
    op.drop_column("workflow_step_template", "updated_by")
    op.drop_column("workflow_step_dependency_version", "updated_by")
    op.drop_constraint(None, "workflow_step_dependency", type_="foreignkey")
    op.drop_column("workflow_step_dependency", "updated_by")
    op.drop_column("workflow_instance_version", "updated_by")
    op.drop_constraint(None, "workflow_instance", type_="foreignkey")
    op.drop_column("workflow_instance", "updated_by")
    op.drop_column("vendor_version", "updated_by")
    op.drop_column("vendor_contacts_version", "updated_by")
    op.drop_constraint(None, "vendor_contacts", type_="foreignkey")
    op.drop_column("vendor_contacts", "updated_by")
    op.drop_constraint(None, "vendor", type_="foreignkey")
    op.drop_column("vendor", "updated_by")
    op.drop_column("user_version", "updated_by")
    op.drop_column("user_role_version", "updated_by")
    op.drop_constraint(None, "user_role", type_="foreignkey")
    op.drop_column("user_role", "updated_by")
    op.drop_column("user_group_version", "updated_by")
    op.drop_constraint(None, "user_group", type_="foreignkey")
    op.drop_column("user_group", "updated_by")
    op.drop_constraint(None, "user", type_="foreignkey")
    op.drop_column("user", "updated_by")
    op.drop_column("step_approvers_version", "updated_by")
    op.drop_constraint(None, "step_approvers", type_="foreignkey")
    op.drop_column("step_approvers", "updated_by")
    op.drop_column("shared_portfolio_cans_version", "updated_by")
    op.drop_constraint(None, "shared_portfolio_cans", type_="foreignkey")
    op.drop_column("shared_portfolio_cans", "updated_by")
    op.drop_column("services_component_version", "updated_by")
    op.drop_constraint(None, "services_component", type_="foreignkey")
    op.drop_column("services_component", "updated_by")
    op.drop_column("role_version", "updated_by")
    op.drop_constraint(None, "role", type_="foreignkey")
    op.drop_column("role", "updated_by")
    op.drop_column("project_version", "updated_by")
    op.drop_column("project_team_leaders_version", "updated_by")
    op.drop_constraint(None, "project_team_leaders", type_="foreignkey")
    op.drop_column("project_team_leaders", "updated_by")
    op.drop_column("project_cans_version", "updated_by")
    op.drop_constraint(None, "project_cans", type_="foreignkey")
    op.drop_column("project_cans", "updated_by")
    op.drop_constraint(None, "project", type_="foreignkey")
    op.drop_column("project", "updated_by")
    op.drop_column("product_service_code_version", "updated_by")
    op.drop_constraint(None, "product_service_code", type_="foreignkey")
    op.drop_column("product_service_code", "updated_by")
    op.drop_column("procurement_step_version", "updated_by")
    op.drop_constraint(None, "procurement_step", type_="foreignkey")
    op.drop_column("procurement_step", "updated_by")
    op.drop_column("procurement_shop_version", "updated_by")
    op.drop_constraint(None, "procurement_shop", type_="foreignkey")
    op.drop_column("procurement_shop", "updated_by")
    op.drop_column("portfolio_version", "updated_by")
    op.drop_column("portfolio_url_version", "updated_by")
    op.drop_constraint(None, "portfolio_url", type_="foreignkey")
    op.drop_column("portfolio_url", "updated_by")
    op.drop_column("portfolio_team_leaders_version", "updated_by")
    op.drop_constraint(None, "portfolio_team_leaders", type_="foreignkey")
    op.drop_column("portfolio_team_leaders", "updated_by")
    op.drop_constraint(None, "portfolio", type_="foreignkey")
    op.drop_column("portfolio", "updated_by")
    op.drop_column("package_version", "updated_by")
    op.drop_column("package_snapshot_version", "updated_by")
    op.drop_constraint(None, "package_snapshot", type_="foreignkey")
    op.drop_column("package_snapshot", "updated_by")
    op.drop_constraint(None, "package", type_="foreignkey")
    op.drop_column("package", "updated_by")
    op.drop_column("ops_event_version", "updated_by")
    op.drop_constraint(None, "ops_event", type_="foreignkey")
    op.drop_column("ops_event", "updated_by")
    op.drop_column("ops_db_history_version", "updated_by")
    op.drop_constraint(None, "ops_db_history", type_="foreignkey")
    op.drop_column("ops_db_history", "updated_by")
    op.drop_column("notification_version", "updated_by")
    op.drop_constraint(None, "notification", type_="foreignkey")
    op.drop_column("notification", "updated_by")
    op.drop_column("group_version", "updated_by")
    op.drop_constraint(None, "group", type_="foreignkey")
    op.drop_column("group", "updated_by")
    op.drop_column("funding_source_version", "updated_by")
    op.drop_constraint(None, "funding_source", type_="foreignkey")
    op.drop_column("funding_source", "updated_by")
    op.drop_column("funding_partner_version", "updated_by")
    op.drop_constraint(None, "funding_partner", type_="foreignkey")
    op.drop_column("funding_partner", "updated_by")
    op.drop_column("division_version", "updated_by")
    op.drop_constraint(None, "division", type_="foreignkey")
    op.drop_column("division", "updated_by")
    op.drop_column("contact_version", "updated_by")
    op.drop_constraint(None, "contact", type_="foreignkey")
    op.drop_column("contact", "updated_by")
    op.drop_column("clin_version", "updated_by")
    op.drop_constraint(None, "clin", type_="foreignkey")
    op.drop_column("clin", "updated_by")
    op.drop_column("can_version", "updated_by")
    op.drop_column("can_funding_sources_version", "updated_by")
    op.drop_constraint(None, "can_funding_sources", type_="foreignkey")
    op.drop_column("can_funding_sources", "updated_by")
    op.drop_column("can_fiscal_year_version", "updated_by")
    op.drop_column("can_fiscal_year_carry_forward_version", "updated_by")
    op.drop_constraint(None, "can_fiscal_year_carry_forward", type_="foreignkey")
    op.drop_column("can_fiscal_year_carry_forward", "updated_by")
    op.drop_constraint(None, "can_fiscal_year", type_="foreignkey")
    op.drop_column("can_fiscal_year", "updated_by")
    op.drop_constraint(None, "can", type_="foreignkey")
    op.drop_column("can", "updated_by")
    op.drop_column("budget_line_item_version", "updated_by")
    op.drop_constraint(None, "budget_line_item", type_="foreignkey")
    op.drop_column("budget_line_item", "updated_by")
    op.drop_column("agreement_version", "updated_by")
    op.drop_column("agreement_team_members_version", "updated_by")
    op.drop_constraint(None, "agreement_team_members", type_="foreignkey")
    op.drop_column("agreement_team_members", "updated_by")
    op.drop_constraint(None, "agreement", type_="foreignkey")
    op.drop_column("agreement", "updated_by")
    # ### end Alembic commands ###
