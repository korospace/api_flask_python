from collections import OrderedDict


# generate response api
def generate_response(status, message, data):

    if status == 200 or status == 201:
        status_bool = True
    else:
        status_bool = False

    res = {
        "status"  : status_bool,
        "message" : message,
        "data"    : data
    }

    return res, status