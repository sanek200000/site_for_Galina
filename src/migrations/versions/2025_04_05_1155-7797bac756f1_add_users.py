"""add Users

Revision ID: 7797bac756f1
Revises: b9d1e0db391a
Create Date: 2025-04-05 11:55:35.264776

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7797bac756f1"
down_revision: Union[str, None] = "b9d1e0db391a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("phone", sa.String(length=12), nullable=False))
    op.add_column("users", sa.Column("telagram", sa.String(length=50), nullable=False))
    op.add_column("users", sa.Column("email", sa.String(length=50), nullable=True))
    op.add_column("users", sa.Column("name", sa.String(length=100), nullable=False))
    op.add_column(
        "users",
        sa.Column(
            "role",
            sa.Enum("ADMIN", "BARBER", "CLIENT", name="roleenum", native_enum=False),
            nullable=False,
        ),
    )
    op.add_column(
        "users", sa.Column("hashed_password", sa.String(length=64), nullable=False)
    )
    op.add_column(
        "users",
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
    )
    op.create_unique_constraint(None, "users", ["telagram"])
    op.create_unique_constraint(None, "users", ["phone"])


def downgrade() -> None:
    op.drop_constraint(None, "users", type_="unique")
    op.drop_constraint(None, "users", type_="unique")
    op.drop_column("users", "created_at")
    op.drop_column("users", "hashed_password")
    op.drop_column("users", "role")
    op.drop_column("users", "name")
    op.drop_column("users", "email")
    op.drop_column("users", "telagram")
    op.drop_column("users", "phone")
