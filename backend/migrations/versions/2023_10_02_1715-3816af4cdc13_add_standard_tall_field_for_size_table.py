"""add standard_tall field for size table

Revision ID: 3816af4cdc13
Revises: 26cb0c91ce56
Create Date: 2023-10-02 17:15:01.374327+00:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3816af4cdc13'
down_revision: Union[str, None] = '26cb0c91ce56'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('clothes_size', sa.Column('standard_tall', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('clothes_size', 'standard_tall')
    # ### end Alembic commands ###