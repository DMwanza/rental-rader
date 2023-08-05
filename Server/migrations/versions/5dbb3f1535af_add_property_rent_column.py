"""Add property_rent column

Revision ID: 5dbb3f1535af
Revises: 7803278bc81c
Create Date: 2023-08-04 19:11:44.941401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5dbb3f1535af'
down_revision = '7803278bc81c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('properties', schema=None) as batch_op:
        batch_op.add_column(sa.Column('property_rent', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('property_owner_photo', sa.String(), nullable=True))
        batch_op.drop_column('rent')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('properties', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rent', sa.FLOAT(), nullable=True))
        batch_op.drop_column('property_owner_photo')
        batch_op.drop_column('property_rent')

    # ### end Alembic commands ###
