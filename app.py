from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.get("/add")
def do_add():
    """Adds queries a and b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    final = add(a,b)

    return str(final)


@app.get("/sub")
def do_sub():
    """Subtracts queries a and b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    final = sub(a,b)

    return str(final)

@app.get("/mult")
def do_mult():
    """Multiples queries a and b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    final = mult(a,b)

    return str(final)

@app.get("/div")
def do_div():
    """Divides queries a by b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    final = div(a,b)

    return str(final)

