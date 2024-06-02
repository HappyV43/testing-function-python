
import functions_framework


from markupsafe import escape

@functions_framework.http
def adding  (request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and "a" in request_json and "b" in request_json:
        a = request_json["a"]
        b = request_json["b"]
    elif request_args and "a" in request_args and "b" in request_args:
        a = request_args["a"]
        b = request_args["b"]
    else:
        return "Please provide both 'a' and 'b' parameters!", 400

    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return "Invalid input. Please provide numerical values for 'a' and 'b'.", 400

    result = a + b
    return f"The sum of {escape(a)} and {escape(b)} is {escape(result)}."
