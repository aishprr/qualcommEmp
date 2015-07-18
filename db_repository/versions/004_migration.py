from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
event = Table('event', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('event_name', String(length=120)),
    Column('event_date', String(length=80)),
    Column('event_location', String(length=120)),
    Column('event_hashtags', String(length=120)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('first_name', String(length=80)),
    Column('last_name', String(length=80)),
    Column('fb_email', String(length=80)),
    Column('org_id', String(length=80)),
    Column('email_id', String(length=80)),
    Column('cell_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['event'].create()
    post_meta.tables['user'].columns['first_name'].create()
    post_meta.tables['user'].columns['last_name'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['event'].drop()
    post_meta.tables['user'].columns['first_name'].drop()
    post_meta.tables['user'].columns['last_name'].drop()
