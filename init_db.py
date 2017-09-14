import os
import sqlite3

BASE_PATH = os.path.expanduser("~/pypocket/")
DB_PATH = BASE_PATH + "pocket.db"

def db_exists():
    if os.path.exists(os.path.expanduser(BASE_PATH)):
        return True
    return False

def _create_directory():
    if not os.path.exists(os.path.expanduser(BASE_PATH)):
        os.makedirs(BASE_PATH, 755)

def init_db():
    if not db_exists():
        _create_directory()
        db_file = open(os.path.expanduser(DB_PATH), "w+")
        db_file.close()
        db_script = open("init.sql", "r").read()
        conn = sqlite3.connect(DB_PATH)

        cursor = conn.cursor()

        cursor.executescript(db_script)
