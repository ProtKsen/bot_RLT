import datetime
import json


ALLOWED_GROUP_TYPE = ['hour', 'day', 'month']


def is_input_valid(message):

    try:
        data = json.loads(message)
    except json.JSONDecodeError:
        return False

    is_fields_valid = ('dt_from' in data) and ('dt_upto' in data) and ('group_type' in data)

    if is_fields_valid:
        try:
            datetime.datetime.fromisoformat(data['dt_from'])
            datetime.datetime.fromisoformat(data['dt_from'])
            if data['group_type'] not in ALLOWED_GROUP_TYPE:
                raise ValueError
        except ValueError:
            return False

    return True
