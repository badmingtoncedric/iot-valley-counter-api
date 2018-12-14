import os
import sqlite3

DB_NAME = 'history.db'
DB_FULLPATH = os.path.dirname(__file__) + '/../data/' + DB_NAME

SQL_CREATE_TBL = """
CREATE TABLE IF NOT EXISTS history(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    action TEXT,
    input_value INTEGER,
    counter_previous_value INTEGER,
    counter_current_value INTEGER
)
"""

SQL_LIST_HISTORY = """SELECT * FROM history"""

SQL_INSERT_HISTORY = """
INSERT INTO history(action, input_value, counter_previous_value, counter_current_value)
VALUES(:action, :input_value, :counter_previous_value, :counter_current_value)
"""

SQL_DELETE_HISTORY = """DELETE FROM history"""

def map_sql_to_json(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class HistoryDAO(object):
    def __init__(self):
        self.db = sqlite3.connect(DB_FULLPATH, check_same_thread=False)
        self.db.row_factory = map_sql_to_json
        self.cur = self.db.cursor()
        self.cur.execute(SQL_CREATE_TBL)
        self.db.commit()
        self.list()

    def reset(self):
        self.cur.execute(SQL_DELETE_HISTORY)
        self.db.commit()

    def list(self):
        self.cur.execute(SQL_LIST_HISTORY)
        return self.cur.fetchall()

    def add(self, action, value, counter_previous, counter_current):
        self.cur.execute(SQL_INSERT_HISTORY, {
            "action": action,
            "input_value": value,
            "counter_previous_value": counter_previous,
            "counter_current_value": counter_current
        })
        self.db.commit()

    def __del__(self):
        self.db.close()
