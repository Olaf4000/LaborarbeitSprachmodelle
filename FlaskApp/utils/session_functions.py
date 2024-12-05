from flask import session

def clear_except_flashes():
    keys_to_keep = ['_flashes']
    for key in list(session.keys()):
        if key not in keys_to_keep:
            session.pop(key)
