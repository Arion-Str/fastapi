"""add content column to posts table

Revision ID: 8bf5d377428a
Revises: 3a2e1e330957
Create Date: 2022-11-04 01:49:43.415366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8bf5d377428a"
down_revision = "3a2e1e330957"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")

    pass
