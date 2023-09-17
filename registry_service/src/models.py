from datetime import datetime

from sqlalchemy import MetaData, Table, Column, String, Uuid, DateTime, create_engine, ForeignKey, Boolean
from database import DATABASE_URL
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy.ext.asyncio import AsyncSession


person_social_group = Table(
    'PersonSocialGroup',
    Base.metadata,
    Column('person_snils', ForeignKey('Person.snils')),
    Column('social_group_id', ForeignKey('SocialGroup.id')),
    Column('is_actual', Boolean(), default=True)
)


class Person(Base):
    __tablename__ = 'Person'
    snils = Column(String(14), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    patronimic = Column(String(50), nullable=False)
    gender = Column(String(1), nullable=False)
    birth_date = Column(DateTime(), nullable=False)
    social_groups = relationship('SocialGroup', secondary=person_social_group, back_populates='persons')
    email = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)


class Card(Base):
    __tablename__ = 'Card'
    id = Column(String(16), primary_key=True)
    bank_card_id = Column(String(16), nullable=False)
    owner_id = Column(String(14), ForeignKey('Person.snils'))
    owner = relationship('Person', backref='cards')
    emission_date = Column(DateTime(), nullable=False)
    expire_date = Column(DateTime(), nullable=False)

    async def get_all(self, session: AsyncSession):
        query = session.query(Card)
        query = query.join()


class SocialGroup(Base):
    __tablename__ = 'SocialGroup'
    id = Column(Uuid(), primary_key=True)
    name = Column(String(100), nullable=False)


class Complain(Base):
    __tablename__ = 'Complain'
    id = Column(Uuid(), primary_key=True)
    card_id = Column(String(16), ForeignKey('Card.id'))
    topic = Column(String(100), nullable=True)
    text = Column(String(500), nullable=True)
