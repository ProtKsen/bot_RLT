import json


def is_input_valid(message):

    try:
        data = json.loads(message)
    except json.JSONDecodeError:
        return False

    if ('dt_from' in data) and ('dt_upto' in data) and ('group_type' in data):
        return True

    return False
