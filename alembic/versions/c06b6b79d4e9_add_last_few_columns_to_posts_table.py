"""add last few columns to posts table

Revision ID: c06b6b79d4e9
Revises: 0ba0bc0ce9b6
Create Date: 2022-11-04 02:02:18.230181

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c06b6b79d4e9"
down_revision = "0ba0bc0ce9b6"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
