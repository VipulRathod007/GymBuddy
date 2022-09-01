# ----------------------------------------------------------------------------------------------------------------------
#  Contains the definition of Database Models
#  Copyright (c) 2022. By Vipul Rathod
#  All rights reserved
# ----------------------------------------------------------------------------------------------------------------------

from abc import ABC
from sqlalchemy import Table, MetaData, Column, Integer, String


class DBMetaData(ABC):
    """Represents DBMetaData class"""

    __sShared__ = None

    def __init__(self):
        raise Exception('Attempt to create an instance of Abstract class')

    @staticmethod
    def getInstance() -> MetaData:
        DBMetaData.__sShared__ = MetaData() if DBMetaData.__sShared__ is None else DBMetaData.__sShared__
        return DBMetaData.__sShared__


Streak = Table('Streak', DBMetaData.getInstance(),
               Column('ID', Integer, primary_key=True),
               Column('StartDate', String),
               Column('EndDate', String),
               Column('StreakPower', Integer)
               )
