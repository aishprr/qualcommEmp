from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
event = Table('event', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('event_name', VARCHAR(length=120)),
    Column('event_date', VARCHAR(length=80)),
    Column('event_location', VARCHAR(length=120)),
    Column('event_hashtags', VARCHAR(length=120)),
    Column('event_zipcode', INTEGER),
)

event = Table('event', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('event_name', String(length=120)),
    Column('event_date', String(length=80)),
    Column('event_location', String(length=120)),
    Column('event_hashtags', String(length=120)),
    Column('user_list', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['event'].columns['event_zipcode'].drop()
    post_meta.tables['event'].columns['user_list'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['event'].columns['event_zipcode'].create()
    post_meta.tables['event'].columns['user_list'].drop()
