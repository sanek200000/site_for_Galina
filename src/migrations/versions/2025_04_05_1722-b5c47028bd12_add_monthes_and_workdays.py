"""add Monthes and Workdays

Revision ID: b5c47028bd12
Revises: b521b4ac81d3
Create Date: 2025-04-05 17:22:02.160857

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b5c47028bd12"
down_revision: Union[str, None] = "b521b4ac81d3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "monthes",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("month", sa.Integer(), nullable=False),
        sa.Column("year", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.Date(), nullable=False),
        sa.CheckConstraint("month >= 1 AND month <= 12", name="valid_month"),
        sa.CheckConstraint("year >= 2025 AND year <= 2100", name="valid_year"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("month", "year", name="_month_year_uc"),
    )
    op.create_table(
        "workdays",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("schedule_id", sa.Integer(), nullable=False),
        sa.Column("day_date", sa.Date(), nullable=False),
        sa.Column("start_time", sa.Time(), nullable=False),
        sa.Column("end_time", sa.Time(), nullable=False),
        sa.ForeignKeyConstraint(
            ["schedule_id"],
            ["monthes.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("workdays")
    op.drop_table("monthes")
