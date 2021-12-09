"""empty message

Revision ID: 572da3397895
Revises: cddd4f5a4d15
Create Date: 2021-12-09 13:24:13.140090

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '572da3397895'
down_revision = 'cddd4f5a4d15'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('artists', 'artist_bio',
               existing_type=sa.VARCHAR(length=500),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('artists', 'artist_bio',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)
    # ### end Alembic commands ###