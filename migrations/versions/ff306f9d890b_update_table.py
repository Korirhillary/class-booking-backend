"""update table

Revision ID: ff306f9d890b
Revises: 9a4fb53430e2
Create Date: 2023-12-20 17:03:32.692100

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ff306f9d890b'
down_revision: Union[str, None] = '9a4fb53430e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.Text(), nullable=False),
    sa.Column('last_name', sa.Text(), nullable=False),
    sa.Column('phone_number', sa.Text(), nullable=False),
    sa.Column('date', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('booklecturehalls',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lecturehall_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['lecturehall_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('booklecturehall')
    op.add_column('lecturehalls', sa.Column('Price', sa.Text(), nullable=False))
    op.drop_column('lecturehalls', 'price')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lecturehalls', sa.Column('price', sa.TEXT(), autoincrement=False, nullable=False))
    op.drop_column('lecturehalls', 'Price')
    op.create_table('booklecturehall',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('phone_number', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('date', sa.TEXT(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='booklecturehall_pkey')
    )
    op.drop_table('booklecturehalls')
    op.drop_table('users')
    # ### end Alembic commands ###
