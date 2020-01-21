from flask import escape
def nameReturn(request):
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
    if request.args and 'name' in request.args:
        name = request_args['name']
        result = 'hello ' + name
    elif request_json and 'name' in request_json:
        name = request_json['name']
        result = 'hello ' + name
    else:
        result = 'there no parameter'
    return escape(result)