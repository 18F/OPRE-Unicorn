"""model changes needed to load data

Revision ID: 8c9a30d8d6b4
Revises: 3d8237681112
Create Date: 2025-02-13 16:46:00.969438+00:00

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from alembic_postgresql_enum import TableReference
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "8c9a30d8d6b4"
down_revision: Union[str, None] = "d65ef7c69392"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "agreement_mod_version",
        sa.Column("id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("agreement_id", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column(
            "mod_type",
            postgresql.ENUM(
                "NEW",
                "ADMIN",
                "AMOUNT_TBD",
                "AS_IS",
                "REPLACEMENT_AMOUNT_FINAL",
                name="modtype",
                create_type=False,
            ),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column("number", sa.String(), autoincrement=False, nullable=True),
        sa.Column("mod_date", sa.Date(), autoincrement=False, nullable=True),
        sa.Column("created_by", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("created_on", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column("updated_on", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column(
            "transaction_id", sa.BigInteger(), autoincrement=False, nullable=False
        ),
        sa.Column("end_transaction_id", sa.BigInteger(), nullable=True),
        sa.Column("operation_type", sa.SmallInteger(), nullable=False),
        sa.PrimaryKeyConstraint("id", "transaction_id"),
    )
    op.create_index(
        op.f("ix_agreement_mod_version_end_transaction_id"),
        "agreement_mod_version",
        ["end_transaction_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_agreement_mod_version_operation_type"),
        "agreement_mod_version",
        ["operation_type"],
        unique=False,
    )
    op.create_index(
        op.f("ix_agreement_mod_version_transaction_id"),
        "agreement_mod_version",
        ["transaction_id"],
        unique=False,
    )
    op.create_table(
        "invoice_version",
        sa.Column("id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column(
            "budget_line_item_id", sa.Integer(), autoincrement=False, nullable=True
        ),
        sa.Column(
            "invoice_line_number", sa.Integer(), autoincrement=False, nullable=True
        ),
        sa.Column("created_by", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("created_on", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column("updated_on", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column(
            "transaction_id", sa.BigInteger(), autoincrement=False, nullable=False
        ),
        sa.Column("end_transaction_id", sa.BigInteger(), nullable=True),
        sa.Column("operation_type", sa.SmallInteger(), nullable=False),
        sa.PrimaryKeyConstraint("id", "transaction_id"),
    )
    op.create_index(
        op.f("ix_invoice_version_end_transaction_id"),
        "invoice_version",
        ["end_transaction_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_invoice_version_operation_type"),
        "invoice_version",
        ["operation_type"],
        unique=False,
    )
    op.create_index(
        op.f("ix_invoice_version_transaction_id"),
        "invoice_version",
        ["transaction_id"],
        unique=False,
    )
    op.create_table(
        "object_class_code_version",
        sa.Column("id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("code", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("description", sa.String(), autoincrement=False, nullable=True),
        sa.Column("created_by", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("created_on", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column("updated_on", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column(
            "transaction_id", sa.BigInteger(), autoincrement=False, nullable=False
        ),
        sa.Column("end_transaction_id", sa.BigInteger(), nullable=True),
        sa.Column("operation_type", sa.SmallInteger(), nullable=False),
        sa.PrimaryKeyConstraint("id", "transaction_id"),
    )
    op.create_index(
        op.f("ix_object_class_code_version_end_transaction_id"),
        "object_class_code_version",
        ["end_transaction_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_object_class_code_version_operation_type"),
        "object_class_code_version",
        ["operation_type"],
        unique=False,
    )
    op.create_index(
        op.f("ix_object_class_code_version_transaction_id"),
        "object_class_code_version",
        ["transaction_id"],
        unique=False,
    )
    op.create_table(
        "requisition_version",
        sa.Column("id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column(
            "budget_line_item_id", sa.Integer(), autoincrement=False, nullable=True
        ),
        sa.Column("zero_number", sa.String(), autoincrement=False, nullable=True),
        sa.Column("zero_date", sa.Date(), autoincrement=False, nullable=True),
        sa.Column("number", sa.String(), autoincrement=False, nullable=True),
        sa.Column("date", sa.Date(), autoincrement=False, nullable=True),
        sa.Column("group", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("check", sa.String(), autoincrement=False, nullable=True),
        sa.Column("created_by", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("updated_by", sa.Integer(), autoincrement=False, nullable=True),
        sa.Column("created_on", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column("updated_on", sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column(
            "transaction_id", sa.BigInteger(), autoincrement=False, nullable=False
        ),
        sa.Column("end_transaction_id", sa.BigInteger(), nullable=True),
        sa.Column("operation_type", sa.SmallInteger(), nullable=False),
        sa.PrimaryKeyConstraint("id", "transaction_id"),
    )
    op.create_index(
        op.f("ix_requisition_version_end_transaction_id"),
        "requisition_version",
        ["end_transaction_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_requisition_version_operation_type"),
        "requisition_version",
        ["operation_type"],
        unique=False,
    )
    op.create_index(
        op.f("ix_requisition_version_transaction_id"),
        "requisition_version",
        ["transaction_id"],
        unique=False,
    )
    op.create_table(
        "object_class_code",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("code", sa.Integer(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("created_by", sa.Integer(), nullable=True),
        sa.Column("updated_by", sa.Integer(), nullable=True),
        sa.Column("created_on", sa.DateTime(), nullable=True),
        sa.Column("updated_on", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["created_by"],
            ["ops_user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["updated_by"],
            ["ops_user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "agreement_mod",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("agreement_id", sa.Integer(), nullable=False),
        sa.Column(
            "mod_type",
            postgresql.ENUM(
                "NEW",
                "ADMIN",
                "AMOUNT_TBD",
                "AS_IS",
                "REPLACEMENT_AMOUNT_FINAL",
                name="modtype",
                create_type=False,
            ),
            nullable=True,
        ),
        sa.Column("number", sa.String(), nullable=False),
        sa.Column("mod_date", sa.Date(), nullable=False),
        sa.Column("created_by", sa.Integer(), nullable=True),
        sa.Column("updated_by", sa.Integer(), nullable=True),
        sa.Column("created_on", sa.DateTime(), nullable=True),
        sa.Column("updated_on", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["agreement_id"],
            ["agreement.id"],
        ),
        sa.ForeignKeyConstraint(
            ["created_by"],
            ["ops_user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["updated_by"],
            ["ops_user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "invoice",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("budget_line_item_id", sa.Integer(), nullable=True),
        sa.Column("invoice_line_number", sa.Integer(), nullable=True),
        sa.Column("created_by", sa.Integer(), nullable=True),
        sa.Column("updated_by", sa.Integer(), nullable=True),
        sa.Column("created_on", sa.DateTime(), nullable=True),
        sa.Column("updated_on", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["budget_line_item_id"],
            ["budget_line_item.id"],
        ),
        sa.ForeignKeyConstraint(
            ["created_by"],
            ["ops_user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["updated_by"],
            ["ops_user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "requisition",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("budget_line_item_id", sa.Integer(), nullable=True),
        sa.Column("zero_number", sa.String(), nullable=True),
        sa.Column("zero_date", sa.Date(), nullable=True),
        sa.Column("number", sa.String(), nullable=True),
        sa.Column("date", sa.Date(), nullable=True),
        sa.Column("group", sa.Integer(), nullable=True),
        sa.Column("check", sa.String(), nullable=True),
        sa.Column("created_by", sa.Integer(), nullable=True),
        sa.Column("updated_by", sa.Integer(), nullable=True),
        sa.Column("created_on", sa.DateTime(), nullable=True),
        sa.Column("updated_on", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["budget_line_item_id"],
            ["budget_line_item.id"],
        ),
        sa.ForeignKeyConstraint(
            ["created_by"],
            ["ops_user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["updated_by"],
            ["ops_user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.add_column(
        "budget_line_item", sa.Column("closed_by", sa.Integer(), nullable=True)
    )
    op.add_column(
        "budget_line_item", sa.Column("closed_date", sa.Date(), nullable=True)
    )
    op.add_column(
        "budget_line_item", sa.Column("extend_pop_to", sa.Date(), nullable=True)
    )
    op.add_column("budget_line_item", sa.Column("start_date", sa.Date(), nullable=True))
    op.add_column("budget_line_item", sa.Column("end_date", sa.Date(), nullable=True))
    op.add_column(
        "budget_line_item",
        sa.Column("object_class_code_id", sa.Integer(), nullable=True),
    )
    op.add_column("budget_line_item", sa.Column("mod_id", sa.Integer(), nullable=True))
    op.add_column(
        "budget_line_item", sa.Column("doc_received", sa.Boolean(), nullable=True)
    )
    op.add_column(
        "budget_line_item", sa.Column("psc_fee_doc_number", sa.String(), nullable=True)
    )
    op.add_column(
        "budget_line_item",
        sa.Column("psc_fee_pymt_ref_nbr", sa.String(), nullable=True),
    )
    op.add_column(
        "budget_line_item", sa.Column("obligation_date", sa.Date(), nullable=True)
    )
    op.create_foreign_key(
        None, "budget_line_item", "object_class_code", ["object_class_code_id"], ["id"]
    )
    op.create_foreign_key(None, "budget_line_item", "ops_user", ["closed_by"], ["id"])
    op.create_foreign_key(None, "budget_line_item", "agreement_mod", ["mod_id"], ["id"])
    op.drop_column("budget_line_item", "requisition_date")
    op.drop_column("budget_line_item", "requisition_number")
    op.drop_column("budget_line_item", "mod_type")
    op.add_column(
        "budget_line_item_version",
        sa.Column("closed_by", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "budget_line_item_version",
        sa.Column("closed_date", sa.Date(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "budget_line_item_version",
        sa.Column("extend_pop_to", sa.Date(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "budget_line_item_version",
        sa.Column("start_date", sa.Date(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "budget_line_item_version",
        sa.Column("end_date", sa.Date(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "budget_line_item_version",
        sa.Column(
            "object_class_code_id", sa.Integer(), autoincrement=False, nullable=True
        ),
    )
    op.add_column(
        "budget_line_item_version",
        sa.Column("mod_id", sa.Integer(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "budget_line_item_version",
        sa.Column("doc_received", sa.Boolean(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "budget_line_item_version",
        sa.Column(
            "psc_fee_doc_number", sa.String(), autoincrement=False, nullable=True
        ),
    )
    op.add_column(
        "budget_line_item_version",
        sa.Column(
            "psc_fee_pymt_ref_nbr", sa.String(), autoincrement=False, nullable=True
        ),
    )
    op.add_column(
        "budget_line_item_version",
        sa.Column("obligation_date", sa.Date(), autoincrement=False, nullable=True),
    )
    op.drop_column("budget_line_item_version", "requisition_date")
    op.drop_column("budget_line_item_version", "requisition_number")
    op.drop_column("budget_line_item_version", "mod_type")
    op.drop_column("contract_agreement", "invoice_line_nbr")
    op.drop_column("contract_agreement_version", "invoice_line_nbr")
    op.sync_enum_values(
        enum_schema="ops",
        enum_name="modtype",
        new_values=["NEW", "ADMIN", "AMOUNT_TBD", "AS_IS", "REPLACEMENT_AMOUNT_FINAL"],
        affected_columns=[
            TableReference(
                table_schema="ops", table_name="agreement_mod", column_name="mod_type"
            ),
            TableReference(
                table_schema="ops",
                table_name="agreement_mod_version",
                column_name="mod_type",
            ),
        ],
        enum_values_to_rename=[],
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.sync_enum_values(
        enum_schema="ops",
        enum_name="modtype",
        new_values=["ADMIN", "AMOUNT_TBD", "AS_IS", "REPLACEMENT_AMOUNT_FINAL"],
        affected_columns=[
            TableReference(
                table_schema="ops", table_name="agreement_mod", column_name="mod_type"
            ),
            TableReference(
                table_schema="ops",
                table_name="agreement_mod_version",
                column_name="mod_type",
            ),
        ],
        enum_values_to_rename=[],
    )
    op.add_column(
        "contract_agreement_version",
        sa.Column("invoice_line_nbr", sa.INTEGER(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "contract_agreement",
        sa.Column("invoice_line_nbr", sa.INTEGER(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "budget_line_item_version",
        sa.Column(
            "mod_type",
            postgresql.ENUM(
                "ADMIN",
                "AMOUNT_TBD",
                "AS_IS",
                "REPLACEMENT_AMOUNT_FINAL",
                name="modtype",
                create_type=False,
            ),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.add_column(
        "budget_line_item_version",
        sa.Column(
            "requisition_number", sa.INTEGER(), autoincrement=False, nullable=True
        ),
    )
    op.add_column(
        "budget_line_item_version",
        sa.Column("requisition_date", sa.DATE(), autoincrement=False, nullable=True),
    )
    op.drop_column("budget_line_item_version", "obligation_date")
    op.drop_column("budget_line_item_version", "psc_fee_pymt_ref_nbr")
    op.drop_column("budget_line_item_version", "psc_fee_doc_number")
    op.drop_column("budget_line_item_version", "doc_received")
    op.drop_column("budget_line_item_version", "mod_id")
    op.drop_column("budget_line_item_version", "object_class_code_id")
    op.drop_column("budget_line_item_version", "end_date")
    op.drop_column("budget_line_item_version", "start_date")
    op.drop_column("budget_line_item_version", "extend_pop_to")
    op.drop_column("budget_line_item_version", "closed_date")
    op.drop_column("budget_line_item_version", "closed_by")
    op.add_column(
        "budget_line_item",
        sa.Column(
            "mod_type",
            postgresql.ENUM(
                "ADMIN",
                "AMOUNT_TBD",
                "AS_IS",
                "REPLACEMENT_AMOUNT_FINAL",
                name="modtype",
                create_type=False,
            ),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.add_column(
        "budget_line_item",
        sa.Column(
            "requisition_number", sa.INTEGER(), autoincrement=False, nullable=True
        ),
    )
    op.add_column(
        "budget_line_item",
        sa.Column("requisition_date", sa.DATE(), autoincrement=False, nullable=True),
    )
    op.drop_constraint(None, "budget_line_item", type_="foreignkey")
    op.drop_constraint(None, "budget_line_item", type_="foreignkey")
    op.drop_constraint(None, "budget_line_item", type_="foreignkey")
    op.drop_column("budget_line_item", "obligation_date")
    op.drop_column("budget_line_item", "psc_fee_pymt_ref_nbr")
    op.drop_column("budget_line_item", "psc_fee_doc_number")
    op.drop_column("budget_line_item", "doc_received")
    op.drop_column("budget_line_item", "mod_id")
    op.drop_column("budget_line_item", "object_class_code_id")
    op.drop_column("budget_line_item", "end_date")
    op.drop_column("budget_line_item", "start_date")
    op.drop_column("budget_line_item", "extend_pop_to")
    op.drop_column("budget_line_item", "closed_date")
    op.drop_column("budget_line_item", "closed_by")
    op.drop_table("requisition")
    op.drop_table("invoice")
    op.drop_table("agreement_mod")
    op.drop_table("object_class_code")
    op.drop_index(
        op.f("ix_requisition_version_transaction_id"), table_name="requisition_version"
    )
    op.drop_index(
        op.f("ix_requisition_version_operation_type"), table_name="requisition_version"
    )
    op.drop_index(
        op.f("ix_requisition_version_end_transaction_id"),
        table_name="requisition_version",
    )
    op.drop_table("requisition_version")
    op.drop_index(
        op.f("ix_object_class_code_version_transaction_id"),
        table_name="object_class_code_version",
    )
    op.drop_index(
        op.f("ix_object_class_code_version_operation_type"),
        table_name="object_class_code_version",
    )
    op.drop_index(
        op.f("ix_object_class_code_version_end_transaction_id"),
        table_name="object_class_code_version",
    )
    op.drop_table("object_class_code_version")
    op.drop_index(
        op.f("ix_invoice_version_transaction_id"), table_name="invoice_version"
    )
    op.drop_index(
        op.f("ix_invoice_version_operation_type"), table_name="invoice_version"
    )
    op.drop_index(
        op.f("ix_invoice_version_end_transaction_id"), table_name="invoice_version"
    )
    op.drop_table("invoice_version")
    op.drop_index(
        op.f("ix_agreement_mod_version_transaction_id"),
        table_name="agreement_mod_version",
    )
    op.drop_index(
        op.f("ix_agreement_mod_version_operation_type"),
        table_name="agreement_mod_version",
    )
    op.drop_index(
        op.f("ix_agreement_mod_version_end_transaction_id"),
        table_name="agreement_mod_version",
    )
    op.drop_table("agreement_mod_version")
    # ### end Alembic commands ###
