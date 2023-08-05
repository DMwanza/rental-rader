"""Create  tables

Revision ID: d1a702ba1094
Revises: ed8695906a6d
Create Date: 2023-08-05 10:27:53.569010

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1a702ba1094'
down_revision = 'ed8695906a6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('payments', schema=None) as batch_op:
        batch_op.drop_column('payment_method')

    with op.batch_alter_table('properties', schema=None) as batch_op:
        batch_op.add_column(sa.Column('country', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('city_town', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('neighborhood_area', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('address', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('property_rent', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('property_owner_name', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('property_owner_photo', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('contact_whatsapp', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('main_image', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('images', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('house_tour_video', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('property_documents', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('facebook', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('twitter', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('instagram', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('linkedin', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('other_social_media', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('amenities', sa.String(), nullable=True))
        batch_op.drop_column('media')
        batch_op.drop_column('landlord_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('properties', schema=None) as batch_op:
        batch_op.add_column(sa.Column('landlord_name', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('media', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('amenities')
        batch_op.drop_column('other_social_media')
        batch_op.drop_column('linkedin')
        batch_op.drop_column('instagram')
        batch_op.drop_column('twitter')
        batch_op.drop_column('facebook')
        batch_op.drop_column('property_documents')
        batch_op.drop_column('house_tour_video')
        batch_op.drop_column('images')
        batch_op.drop_column('main_image')
        batch_op.drop_column('contact_whatsapp')
        batch_op.drop_column('property_owner_photo')
        batch_op.drop_column('property_owner_name')
        batch_op.drop_column('property_rent')
        batch_op.drop_column('address')
        batch_op.drop_column('neighborhood_area')
        batch_op.drop_column('city_town')
        batch_op.drop_column('country')

    with op.batch_alter_table('payments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('payment_method', sa.VARCHAR(), nullable=True))

    # ### end Alembic commands ###