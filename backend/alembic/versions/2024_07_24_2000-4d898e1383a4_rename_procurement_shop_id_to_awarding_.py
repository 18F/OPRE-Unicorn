"""Rename procurement_shop_id to awarding_entity_id

Revision ID: 4d898e1383a4
Revises: de9beb904925
Create Date: 2024-07-24 20:00:42.211808+00:00

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '4d898e1383a4'
down_revision: Union[str, None] = 'de9beb904925'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('agreement', sa.Column('awarding_entity_id', sa.Integer(), nullable=True))
    op.drop_constraint('agreement_procurement_shop_id_fkey', 'agreement', type_='foreignkey')
    op.create_foreign_key(None, 'agreement', 'procurement_shop', ['awarding_entity_id'], ['id'])
    op.drop_column('agreement', 'procurement_shop_id')
    op.add_column('agreement_version', sa.Column('awarding_entity_id', sa.Integer(), autoincrement=False, nullable=True))
    op.drop_column('agreement_version', 'procurement_shop_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('agreement_version', sa.Column('procurement_shop_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('agreement_version', 'awarding_entity_id')
    op.add_column('agreement', sa.Column('procurement_shop_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'agreement', type_='foreignkey')
    op.create_foreign_key('agreement_procurement_shop_id_fkey', 'agreement', 'procurement_shop', ['procurement_shop_id'], ['id'])
    op.drop_column('agreement', 'awarding_entity_id')
    # ### end Alembic commands ###
