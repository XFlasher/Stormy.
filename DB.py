import sqlite3
import random


class DB():
    '''Оператор базы данных'''
    def __init__(self, db):
        self.db = sqlite3.connect(db)
        self.cursor = self.db.cursor()

    def Upd(self, table, column, value, key_name = None, key= None):
        """Обновление данных по заданным данным"""
        if key_name is None and key is None:
            self.cursor.execute(f"UPDATE {table} SET {column} = '{value}'")
            self.db.commit()
        else:
            self.cursor.execute(f"UPDATE {table} SET {column} = '{value}' WHERE {key_name} = {key}")
            self.db.commit()

    def F_all(self, table, key_name = None, key = None):
        '''Множественное нахождение данных'''
        try:
            if key_name is None and key is None:
                self.cursor.execute(f"SELECT * FROM {table}")
                row = self.cursor.fetchall()
                if row:
                    return row
                else:
                    return None
            else:
                self.cursor.execute(f"SELECT * FROM {table} WHERE {key_name} = {key}")
                row = self.cursor.fetchall()
                if row:
                    return row[0]
                else:
                    return None
        except Exception as e:
            print(f'[DB] error: \n {e}')

    def FallMorKeys(self, table, key_name, key):
        '''Множественное нахождение данных'''
        try:
            self.cursor.execute(f"SELECT * FROM {table} WHERE {key_name[0]} = {key[0]} AND {key_name[1]} = {key[1]}")
            row = self.cursor.fetchall()
            if row:
                return row
            else:
                return None
        except Exception as e:
            print(f'[DB] error: \n {e}')

    def F_one(self, table, column, key_name, key):
        '''Единичное нхождение данных'''
        try:
            self.cursor.execute(f"SELECT {column} FROM {table} WHERE {key_name} = {key}")
            row = self.cursor.fetchone()
            if row:
                if len(row)> 1:
                    return row
                else:
                    return row[0]
            else:
                return None
        except Exception as e:
            print(f'[DB] error\n {e}')

    def Ord_By(self, Table, OrdName, OrdBy, Limit):
        '''Сортировка данных по заданным критериям и лимиту'''
        self.cursor.execute(f"SELECT * FROM {Table} ORDER BY {OrdName} {OrdBy} LIMIT {Limit}")
        row = self.cursor.fetchall()
        if row:
            return row
        else:
            return

    def Ins(self, Table, colums, values):
        '''Установка данных в таблице'''
        self.cursor.execute(f"INSERT INTO {Table} {colums} VALUES {values}")
        self.db.commit()

    def Del(self, Table, key_name, key):
        '''Удаление данных в таблице'''
        self.cursor.execute(f"DELETE FROM {Table} WHERE {key_name} = {key}")
        self.db.commit()


SystemWay = 'Data/DB/System.sqlite'

SysDB = DB(SystemWay)


