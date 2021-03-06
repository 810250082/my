"""empty message

Revision ID: 280a123f0d87
Revises: c162d9374466
Create Date: 2018-06-02 18:43:24.572670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '280a123f0d87'
down_revision = 'c162d9374466'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def upgrade_my_dom():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('teacher', sa.Column('school_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'teacher', 'school', ['school_id'], ['id'])
    # ### end Alembic commands ###


def downgrade_my_dom():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'teacher', type_='foreignkey')
    op.drop_column('teacher', 'school_id')
    # ### end Alembic commands ###

