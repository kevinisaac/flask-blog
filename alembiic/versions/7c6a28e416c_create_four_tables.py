"""create_four_tables

Revision ID: 7c6a28e416c
Revises: None
Create Date: 2014-05-30 14:46:58.145138

"""

# revision identifiers, used by Alembic.
revision = '7c6a28e416c'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.create_table('categories',
        sa.Column('id', sa.Integer, primary_key = True),
        sa.Column('name', sa.Stringa(100), nullable = False),
        sa.Column('slug', sa.String(100), nullable = False),
        sa.Column('post_count', DateTime, nullable = False)
    )

    op.create_table('comments',
        sa.Column('id', sa.Integer, primary_key = True),
        sa.Column('post_id', sa.Integer, nullable = False),
        sa.Column('username', sa.String(50), nullable = False),
        sa.Column('mail', sa.String(80), nullable = False),
        sa.Column('content', sa.Unicode(2000), nullable = False),
        sa.Column('created', DateTime, nullable = False)
    )

    op.create_table('posts',
        sa.Column('id', sa.Integer, primary_key = True),
        sa.Column('category_id', sa.Integer, nullable = False),
        sa.Column('user_id', sa.Integer, nullable = False),
        sa.Column('name', sa.String(300), nullable = False),
        sa.Column('slug', sa.String(300), nullable = False),
        sa.Column('content', sa.Unicode(8000), nullable = False),
        sa.Column('created', DateTime, nullable = False)
    )

    op.create_table('users',
        sa.Column('id', sa.Integer, primary_key = True),
        sa.Column('username', sa.String(50), nullable = False),
        sa.Column('password', sa.String(80), nullable = False)
    )


def downgrade():
    op.drop_table('categories')
    op.drop_table('comments')
    op.drop_table('posts')
    op.drop_table('users')
