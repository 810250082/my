"""empty message

Revision ID: 232109869da6
Revises: b5faf07ed117
Create Date: 2018-06-02 16:12:35.763888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '232109869da6'
down_revision = 'b5faf07ed117'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'address', sa.Column('created_time', sa.DATETIME(), nullable=True))
    op.add_column(u'user', sa.Column('type', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'user', 'type')
    op.drop_column(u'address', 'created_time')
    op.drop_table('company')
    # ### end Alembic commands ###
