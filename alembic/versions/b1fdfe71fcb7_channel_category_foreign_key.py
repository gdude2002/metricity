"""channel category foreign key

Revision ID: b1fdfe71fcb7
Revises: 38085c8f1099
Create Date: 2020-08-25 15:00:38.666504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1fdfe71fcb7'
down_revision = '38085c8f1099'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'channels', 'categories', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'channels', type_='foreignkey')
    # ### end Alembic commands ###