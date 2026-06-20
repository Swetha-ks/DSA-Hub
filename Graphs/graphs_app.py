from flask import Blueprint, render_template, request, jsonify

graphs_app = Blueprint("graphs_app", __name__, template_folder="templates")

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        # Undirected graph: add reverse
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(u)

    def to_dict(self):
        nodes = [{"id": node} for node in self.graph]
        links = []
        for u in self.graph:
            for v in self.graph[u]:
                links.append({"source": u, "target": v})
        return {"nodes": nodes, "links": links}

g = Graph()

@graphs_app.route("/", methods=["GET"])
def home():
    return render_template("graph.html")

@graphs_app.route("/add_edge", methods=["POST"])
def add_edge():
    u = request.form.get("u")
    v = request.form.get("v")
    if u and v:
        g.add_edge(u, v)
    return jsonify({"status": "ok"})

@graphs_app.route("/graph", methods=["GET"])
def graph_data():
    return jsonify(g.to_dict())
