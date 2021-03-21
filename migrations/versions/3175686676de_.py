"""empty message

Revision ID: 3175686676de
Revises: 8375f4702d70
Create Date: 2021-03-21 03:41:36.636911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3175686676de'
down_revision = '8375f4702d70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Tasks', sa.Column('list_id', sa.Integer(), nullable=True))
    op.drop_constraint('Tasks_todolist_id_fkey', 'Tasks', type_='foreignkey')
    op.create_foreign_key(None, 'Tasks', 'ToDoList', ['list_id'], ['id'])
    op.drop_column('Tasks', 'todolist_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Tasks', sa.Column('todolist_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'Tasks', type_='foreignkey')
    op.create_foreign_key('Tasks_todolist_id_fkey', 'Tasks', 'ToDoList', ['todolist_id'], ['id'])
    op.drop_column('Tasks', 'list_id')
    # ### end Alembic commands ###
