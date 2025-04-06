"""add Notifications

Revision ID: 251d6d915847
Revises: b5c47028bd12
Create Date: 2025-04-06 09:17:48.132723

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "251d6d915847"
down_revision: Union[str, None] = "b5c47028bd12"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "notifications",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("content", sa.String(), nullable=False),
        sa.Column(
            "status",
            sa.Enum("PENDING", "SENT", "FAILED", name="statusenum"),
            nullable=False,
        ),
        sa.Column(
            "type",
            sa.Enum("MASS", "REMINDER1", "REMINDER24", "OVERVIEW", name="typeenum"),
            nullable=False,
        ),
        sa.Column("scheduled_at", sa.DateTime(), nullable=False),
        sa.Column("sent_at", sa.DateTime(), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("notifications")
    op.execute("DROP TYPE")
