from db_requests import *

def dictify(tup):
    result = {
        "id": tup[0],
        "key": tup[1],
        "description": tup[2],
        "value": tup[3]
    }
    return result

def get_all_snippets():
    return [dictify(snippet) for snippet in load_all_snippets()]

def get_snippet_by_id(snippet_id):
    result = load_snippet_by_id(snippet_id)
    if len(result) > 0:
        return dictify(result[0])

def get_snippet_by_key(key):
    result = load_snippet_by_key(key)
    if len(result) > 0:
        return dictify(result[0])

def add_snippet(snippet):
    key = snippet["key"]
    description = snippet["description"]
    value = snippet["value"]
    add_snippet_to_db(key, description, value)

def modify_snippet(key, snippet):
    if get_snippet_by_key(key) is not None:
        description = snippet["description"]
        value = snippet["value"]
        update_snippet_by_key(key, description, value)
    else:
        raise ValueError

def remove_snippet_by_id(snippet_id):
    remove_snippet_from_db_by_id(snippet_id)

def remove_snippet_by_key(key):
    remove_snippet_from_db_by_key(key)
