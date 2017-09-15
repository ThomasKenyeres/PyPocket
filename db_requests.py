from init_db import *

def get_connection():
    return sqlite3.connect(DB_PATH)

def load_all_snippets():
    connection = get_connection()
    result = connection.execute("SELECT * FROM Snippets")
    return result.fetchall()

def load_snippet_by_id(snippet_id):
    connection = get_connection()
    query_params = (snippet_id,)
    sql = "SELECT * FROM Snippets WHERE snippetID=?"
    result = connection.execute(sql, query_params)
    return result.fetchall()

def load_snippet_by_key(key):
    connection = get_connection()
    query_params = (key,)
    sql = "SELECT * FROM Snippets WHERE snippetKey=?"
    result = connection.execute(sql, query_params)
    return result.fetchall()

def add_snippet_to_db(key, description, value):
    connection = get_connection()
    query_params = (key, description, value)
    sql = "INSERT INTO Snippets(snippetKey, snippetDescription, snippetValue) VALUES(?, ?, ?)"
    connection.cursor().execute(sql, query_params)
    connection.commit()

def remove_snippet_from_db_by_id(snippet_id):
    connection = get_connection()
    query_params = (snippet_id,)
    sql = "DELETE FROM Snippets WHERE snippetID=?"
    connection.cursor().execute(sql, query_params)
    connection.commit()

def remove_snippet_from_db_by_key(key):
    connection = get_connection()
    query_params = (key,)
    sql = "DELETE FROM Snippets WHERE snippetKey=?"
    connection.cursor().execute(sql, query_params)
    connection.commit()

def update_snippet_by_key(key, description, value):
    print("upd")
    connection = get_connection()
    query_params = (key, description, value)
    sql = "UPDATE Snippets SET snippetDescription=?, snippetValue=? WHERE snippetKey=?"
    connection.cursor().execute(sql, query_params)
    connection.commit()
