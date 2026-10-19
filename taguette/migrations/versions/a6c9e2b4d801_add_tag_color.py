"""Add persistent tag colors with a soft yellow default."""
from alembic import op
import sqlalchemy as sa

revision = 'a6c9e2b4d801'
down_revision = 'db5e31a0233d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('tags', sa.Column(
        'color', sa.String(7), nullable=False, server_default='#fff2b3'))


def downgrade():
    with op.batch_alter_table('tags') as batch:
        batch.drop_column('color')
