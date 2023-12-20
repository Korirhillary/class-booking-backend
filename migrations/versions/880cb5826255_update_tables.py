"""update tables

Revision ID: 880cb5826255
Revises: a39f31afe4a5
Create Date: 2023-12-19 18:30:17.093533

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '880cb5826255'
down_revision: Union[str, None] = 'a39f31afe4a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('booklecturehall',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.Text(), nullable=False),
    sa.Column('last_name', sa.Text(), nullable=False),
    sa.Column('phone_number', sa.Integer(), nullable=False),
    sa.Column('date', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('lecturehalls', sa.Column('price', sa.Text(), nullable=False))
    op.drop_column('lecturehalls', 'date')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lecturehalls', sa.Column('date', sa.TEXT(), autoincrement=False, nullable=False))
    op.drop_column('lecturehalls', 'price')
    op.drop_table('booklecturehall')
    # ### end Alembic commands ###