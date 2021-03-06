"""adding source_id to station table

Revision ID: 6564e31adc72
Revises: 12675ba27402
Create Date: 2022-02-15 12:28:39.611146

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "6564e31adc72"
down_revision = "12675ba27402"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("stations", sa.Column("source_id", sa.String(), nullable=True))
    op.create_index(
        op.f("ix_stations_source_id"), "stations", ["source_id"], unique=False
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_stations_source_id"), table_name="stations")
    op.drop_column("stations", "source_id")
    # ### end Alembic commands ###
