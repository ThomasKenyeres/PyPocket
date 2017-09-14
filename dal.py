from db_requests import *

def get_all_snippets():
    return load_all_snippets()

def get_snippet_by_id(snippet_id):
    result = load_snippet_by_id(snippet_id)
    if len(result) > 0:
        return result[0]

def get_snippet_by_key(key):
    result = load_snippet_by_key(key)
    if len(result) > 0:
        return result[0]

def add_snippet(snippet):
    key = snippet["key"]
    description = snippet["description"]
    value = snippet["value"]
    add_snippet_to_db(key, description, value)

def remove_snippet_by_id(snippet_id):
    remove_snippet_from_db_by_id(snippet_id)

def remove_snippet_by_key(key):
    remove_snippet_from_db_by_key(key)
