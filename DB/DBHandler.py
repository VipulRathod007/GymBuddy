# ----------------------------------------------------------------------------------------------------------------------
#  Contains the definition of DBHandler class
#  Copyright (c) 2022. By Vipul Rathod
#  All rights reserved
# ----------------------------------------------------------------------------------------------------------------------

from enum import Enum
from sqlalchemy import create_engine, MetaData


class DataBase(Enum):
    SQLite = 'sqlite'


class DBHandler:
    """Represents DBHandler class"""

    def __init__(self, inDBType: DataBase, inDBName: str, inUID: str = '', inPWD: str = ''):
        self.__mDBEngine = create_engine(f'{inDBType.value}:///{inDBName}')

    def createTables(self, inMetaData: MetaData):
        try:
            inMetaData.create_all(self.__mDBEngine)
            return True
        except Exception as error:
            print(f'Error: {error}')
            return False

    def execute(self, inQuery: str):
        if inQuery is None or len(inQuery) == 0:
            return False
        with self.__mDBEngine.connect() as conn:
            try:
                conn.execute(inQuery)
                return True
            except Exception as error:
                print(f'Error: {error}')
