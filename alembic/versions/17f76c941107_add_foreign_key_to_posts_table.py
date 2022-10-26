"""add foreign-key to posts table

Revision ID: 17f76c941107
Revises: b2be15100080
Create Date: 2022-10-26 03:24:17.424754

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "17f76c941107"
down_revision = "b2be15100080"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "post_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade() -> None:
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
