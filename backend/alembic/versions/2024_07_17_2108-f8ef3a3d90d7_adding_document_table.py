"""Adding document table

Revision ID: f8ef3a3d90d7
Revises: 5d3916a592a6
Create Date: 2024-07-17 21:08:10.094647+00:00

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'f8ef3a3d90d7'
down_revision: Union[str, None] = '5d3916a592a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    sa.Enum(
        'CERTIFICATION_OF_FUNDING',
        'STATEMENT_OF_REQUIREMENTS',
        'ITAR_CHECKLIST_FOR_ALL_IT_PROCUREMENT_ACTIONS',
        'INDEPENDENT_GOVERNMENT_COST_ESTIMATE',
        'SECTION_508_EXCEPTION_DOCUMENTATION',
        'COR_NOMINATION_AND_CERTIFICATION_DOCUMENT',
        'ADDITIONAL_DOCUMENT',
        name='documenttype'
    ).create(op.get_bind())

    op.create_table(
        'document_version',
        sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
        sa.Column('document_id', sa.String(), nullable=False),
        sa.Column('status', sa.String(), nullable=True),
        sa.Column('file_name', sa.String(), autoincrement=False, nullable=False),
        sa.Column(
            'document_type',
            postgresql.ENUM(
                'CERTIFICATION_OF_FUNDING',
                'STATEMENT_OF_REQUIREMENTS',
                'ITAR_CHECKLIST_FOR_ALL_IT_PROCUREMENT_ACTIONS',
                'INDEPENDENT_GOVERNMENT_COST_ESTIMATE',
                'SECTION_508_EXCEPTION_DOCUMENTATION',
                'COR_NOMINATION_AND_CERTIFICATION_DOCUMENT',
                'ADDITIONAL_DOCUMENT',
                name='documenttype',
                create_type=False
            ),
            nullable=False
        ),
        sa.Column('agreement_id', sa.Integer(), autoincrement=False, nullable=False),
        sa.Column('created_by', sa.Integer(), autoincrement=False, nullable=True),
        sa.Column('updated_by', sa.Integer(), autoincrement=False, nullable=True),
        sa.Column('created_on', sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column('updated_on', sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
        sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
        sa.Column('operation_type', sa.SmallInteger(), nullable=False),
        sa.PrimaryKeyConstraint('id', 'transaction_id')
    )
    op.create_index(
        op.f('ix_document_version_end_transaction_id'),
        'document_version',
        ['end_transaction_id'],
        unique=False
    )
    op.create_index(
        op.f('ix_document_version_operation_type'),
        'document_version',
        ['operation_type'],
        unique=False
    )
    op.create_index(
        op.f('ix_document_version_transaction_id'),
        'document_version',
        ['transaction_id'],
        unique=False
    )

    op.create_table(
        'document',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('document_id', sa.String(), nullable=False),
        sa.Column('status', sa.String(), nullable=True),
        sa.Column('file_name', sa.String(), nullable=False),
        sa.Column(
            'document_type',
            postgresql.ENUM(
                'CERTIFICATION_OF_FUNDING',
                'STATEMENT_OF_REQUIREMENTS',
                'ITAR_CHECKLIST_FOR_ALL_IT_PROCUREMENT_ACTIONS',
                'INDEPENDENT_GOVERNMENT_COST_ESTIMATE',
                'SECTION_508_EXCEPTION_DOCUMENTATION',
                'COR_NOMINATION_AND_CERTIFICATION_DOCUMENT',
                'ADDITIONAL_DOCUMENT',
                name='documenttype',
                create_type=False
            ),
            nullable=False
        ),
        sa.Column('agreement_id', sa.Integer(), nullable=False),
        sa.Column('created_by', sa.Integer(), nullable=True),
        sa.Column('updated_by', sa.Integer(), nullable=True),
        sa.Column('created_on', sa.DateTime(), nullable=True),
        sa.Column('updated_on', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ['agreement_id'],
            ['agreement.id'],
        ),
        sa.ForeignKeyConstraint(
            ['created_by'],
            ['ops_user.id'],
        ),
        sa.ForeignKeyConstraint(
            ['updated_by'],
            ['ops_user.id'],
        ),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('document')
    op.drop_index(op.f('ix_document_version_transaction_id'), table_name='document_version')
    op.drop_index(op.f('ix_document_version_operation_type'), table_name='document_version')
    op.drop_index(op.f('ix_document_version_end_transaction_id'), table_name='document_version')
    op.drop_table('document_version')
    sa.Enum(
        'CERTIFICATION_OF_FUNDING',
        'STATEMENT_OF_REQUIREMENTS',
        'ITAR_CHECKLIST_FOR_ALL_IT_PROCUREMENT_ACTIONS',
        'INDEPENDENT_GOVERNMENT_COST_ESTIMATE',
        'SECTION_508_EXCEPTION_DOCUMENTATION',
        'COR_NOMINATION_AND_CERTIFICATION_DOCUMENT',
        'ADDITIONAL_DOCUMENT',
        name='documenttype'
    ).drop(op.get_bind())
    # ### end Alembic commands ###
