"""add Monthes and Workdays

Revision ID: 5e7f671dd008
Revises: 9df5d9530701
Create Date: 2025-04-08 15:33:40.586241

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5e7f671dd008"
down_revision: Union[str, None] = "9df5d9530701"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "monthes",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("month", sa.Integer(), nullable=False),
        sa.Column("year", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("TIMEZONE('utc', now())"),
            nullable=False,
        ),
        sa.CheckConstraint("month >= 1 AND month <= 12", name="valid_month"),
        sa.CheckConstraint("year >= 2025 AND year <= 2100", name="valid_year"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("month", "year", name="_month_year_uc"),
    )
    op.create_table(
        "workdays",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("month_id", sa.Integer(), nullable=False),
        sa.Column("day_date", sa.Date(), nullable=False),
        sa.Column("start_time", sa.Time(), nullable=False),
        sa.Column("end_time", sa.Time(), nullable=False),
        sa.ForeignKeyConstraint(["month_id"], ["monthes.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("workdays")
    op.drop_table("monthes")
