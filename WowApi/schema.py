#!/usr/bin/python3

from sqlalchemy import Column, Integer, BigInteger, SmallInteger, String, Boolean, JSON, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Realm(Base):
    __tablename__ = 'realm'
    id = Column(Integer)
    name = Column(String(255))
    slug = Column(String(255), primary_key=True)
    locale = Column(String(255))
    category = Column(String(255))
    timezone = Column(String(255))
    is_tournament = Column(Boolean)
    type_name = Column('type_name',String(255))
    type_type = Column('type',String(255))
    _links_self_href = Column('href',String(255))
    region_id = Column('region_id',Integer)
    region_key_href = Column('region_href',String(255))
    region_name = Column('region_hame',String(255))
    connected_realm_href = Column(String(255))

    def __repr__(self):
        return self.slug


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    _links = Column(JSON)
    name = Column(String(255))
    quality = Column(JSON)
    level = Column(SmallInteger)
    required_level = Column(SmallInteger)
    media = Column(JSON)
    item_class = Column(JSON)
    item_subclass = Column(JSON)
    inventory_type = Column(JSON)
    purchase_price = Column(BigInteger)
    sell_price = Column(BigInteger)
    max_count = Column(Integer)
    is_equippable = Column(Boolean)
    is_stackable = Column(Boolean)
    preview_item = Column(JSON)
    purchase_quantity = Column(Integer)


class CharacterPet(Base):
    __tablename__ = 'character_pet'
    id = Column(Integer, primary_key=True, autoincrement=False)
    species = Column(JSON)
    level = Column(SmallInteger)
    quality = Column(JSON)
    stats = Column(JSON)
    creature_display = Column(JSON)
    is_favorite = Column(Boolean)
    is_active = Column(Boolean)
    active_slot = Column(SmallInteger)


class Pet(Base):
    __tablename__ = 'pet'
    id = Column(Integer, primary_key=True, autoincrement=False)
    icon = Column(String(255))
    name = Column(String(255))
    abilities = Column(JSON)
    description = Column(String(2047))
    is_tradable = Column(Boolean)
    is_battlepet = Column(Boolean)
    is_capturable = Column(Boolean)
    is_horde_only = Column(Boolean)
    is_alliance_only = Column(Boolean)
    is_random_creature_display = Column(Boolean)
    media_id = Column(Integer)
    media_key_href = Column('media_href',String(255))
    _links_self_href = Column('href',String(255))
    source_name = Column('source_name',String(255))
    source_type = Column('source_type',String(255))
    creature_id = Column('creature_id',Integer)
    creature_key_href = Column('creature_href',String(255))
    creature_name = Column('creature_name',String(255))
    battle_pet_type_id = Column('type_id',Integer)
    battle_pet_type_name = Column('type_name',String(255))
    battle_pet_type_type = Column('type',String(255))

#class Auction(Base):
#    __tablename__ = 'auction'
#    id = Column(Integer, primary_key=True)
#    buyout
#    quantity
#    time_left
#    item.id
#    item.context
#    item.modifiers
#    item.bonus_lists
#    bid
#    unit_price
#    item.pet_level
#    item.pet_breed_id
#    item.pet_quality_id
#    item.pet_species_id

def initialize_database(conn_string, args):
    engine = sqlalchemy.create_engine(conn_string, echo=True)
    if args.force:
        Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    import argparse
    import sqlalchemy
    from config import CONN_STRING

    parser=argparse.ArgumentParser(
        prog='''WoWapi.schema''',
        description ='''Database configuration tool'''
    )
    parser.add_argument('-I', '--initialize', action='store_true', help='initialize database tables')
    parser.add_argument('-F', '--force', action='store_true', help='drop existing tables')

    args = parser.parse_args()

    if args.initialize:
        initialize_database(CONN_STRING, args)
