from flask import Blueprint, render_template, request, jsonify

trees_app = Blueprint("trees_app", __name__, template_folder="templates")

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.key:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def to_dict(self, root):
        if root is None:
            return None
        children = []
        if root.left:
            children.append(self.to_dict(root.left))
        if root.right:
            children.append(self.to_dict(root.right))
        return {"name": root.key, "children": children}

bst = BST()

@trees_app.route("/", methods=["GET"])
def home():
    return render_template("tree.html")

@trees_app.route("/insert", methods=["POST"])
def insert():
    value = request.form.get("value")
    if value:
        bst.insert(int(value))
    return jsonify({"status": "ok"})

@trees_app.route("/tree", methods=["GET"])
def tree():
    return jsonify(bst.to_dict(bst.root))
