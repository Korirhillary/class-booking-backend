"""updated tables

Revision ID: 54c460000a95
Revises: 349a1ebba9d8
Create Date: 2023-12-20 22:30:24.195471

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '54c460000a95'
down_revision: Union[str, None] = '349a1ebba9d8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('booklecturehalls', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('booklecturehalls_lecturehall_id_fkey', 'booklecturehalls', type_='foreignkey')
    op.create_foreign_key(None, 'booklecturehalls', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'booklecturehalls', 'lecturehalls', ['lecturehall_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'booklecturehalls', type_='foreignkey')
    op.drop_constraint(None, 'booklecturehalls', type_='foreignkey')
    op.create_foreign_key('booklecturehalls_lecturehall_id_fkey', 'booklecturehalls', 'users', ['lecturehall_id'], ['id'])
    op.drop_column('booklecturehalls', 'user_id')
    # ### end Alembic commands ###