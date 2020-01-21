from flask import escape
def triangle_P(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    request_args = request.args
    if request.args and 'a' and 'b' and 'c' in request.args:
        a = request_args['a']
        b = request_args['b']
        c = request_args['c']
        P = a + b + c
    elif request_json and 'a' and 'b' and 'c' in request_json:
        a = request_json['a']
        b = request_json['b']
        c = request_json['c']
        P = a + b + c
    else:
        P = 'undefined'
    return escape(P)
