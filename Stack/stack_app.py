from flask import Blueprint, render_template, request

stack_app = Blueprint("stack_app", __name__, template_folder="templates")

stack = []

@stack_app.route("/", methods=["GET"])
def index():
    return render_template("stack.html", stack=stack)

@stack_app.route("/push", methods=["POST"])
def push():
    item = request.form["item"]
    stack.append(item)
    return render_template("stack.html", stack=stack)

@stack_app.route("/pop")
def pop():
    if stack:
        stack.pop()
    return render_template("stack.html", stack=stack)

@stack_app.route("/peek")
def peek():
    top = stack[-1] if stack else None
    return render_template("stack.html", stack=stack, top=top)
