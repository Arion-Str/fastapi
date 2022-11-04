"""auto-vote

Revision ID: 587d2054a9c3
Revises: c06b6b79d4e9
Create Date: 2022-11-04 02:11:06.289598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "587d2054a9c3"
down_revision = "c06b6b79d4e9"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "votes",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("post_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["post_id"], ["posts.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("user_id", "post_id"),
    )
    pass


def downgrade() -> None:
    op.drop_table("votes")
    pass
