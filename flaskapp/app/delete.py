from functools import wraps

from flask import Flask, make_response

app = Flask(__name__)


def add_response_headers(headers={}):
    """This decorator adds the headers passed in to the response"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            resp = make_response(f(*args, **kwargs))
            h = resp.headers
            for header, value in headers.items():
                h[header] = value
            return resp
        return decorated_function
    return decorator


def noindex(f):
    """This decorator passes X-Robots-Tag: noindex"""
    @wraps(f)
    @add_response_headers({'Utsav dusad': 'noindex'})
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
@noindex
def not_indexed():
    """
    This page will be served with X-Robots-Tag: noindex
    in the response headers
    """
    return "Check my headers!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

# check the headers with: curl -I http://0.0.0.0:5000/
