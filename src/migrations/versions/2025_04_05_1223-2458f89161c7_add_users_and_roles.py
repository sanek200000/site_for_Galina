"""add Users and Roles

Revision ID: 2458f89161c7
Revises: 7797bac756f1
Create Date: 2025-04-05 12:23:48.911741

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2458f89161c7"
down_revision: Union[str, None] = "7797bac756f1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "roles",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=20), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "users_roles",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("role_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["role_id"],
            ["roles.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.add_column("users", sa.Column("role_id", sa.Integer(), nullable=False))
    op.create_foreign_key(None, "users", "roles", ["role_id"], ["id"])
    op.drop_column("users", "role")


def downgrade() -> None:
    op.add_column(
        "users",
        sa.Column("role", sa.VARCHAR(length=6), autoincrement=False, nullable=False),
    )
    op.drop_constraint(None, "users", type_="foreignkey")
    op.drop_column("users", "role_id")
    op.drop_table("users_roles")
    op.drop_table("roles")
