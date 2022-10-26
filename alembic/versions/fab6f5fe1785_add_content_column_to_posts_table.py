"""add content column to posts table

Revision ID: fab6f5fe1785
Revises: 057902662e67
Create Date: 2022-10-26 01:40:50.247825

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "fab6f5fe1785"
down_revision = "057902662e67"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
