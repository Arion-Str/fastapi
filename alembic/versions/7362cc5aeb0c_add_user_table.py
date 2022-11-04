"""add user table

Revision ID: 7362cc5aeb0c
Revises: 8bf5d377428a
Create Date: 2022-11-04 01:55:20.837880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7362cc5aeb0c"
down_revision = "8bf5d377428a"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
