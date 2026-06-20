from flask import Flask, render_template
from Arrays.array_app import array_app
from Linked_list.playlist_app import playlist_app
from Stack.stack_app import stack_app
from Trees.trees_app import trees_app
from Queue.queue_app import queue_app
from Graphs.graphs_app import graphs_app

app = Flask(__name__)

@app.route("/")
def hub():
    return render_template("hub.html")

# Register all apps
app.register_blueprint(array_app, url_prefix="/arrays")
app.register_blueprint(playlist_app, url_prefix="/playlist")
app.register_blueprint(stack_app, url_prefix="/stack")
app.register_blueprint(trees_app, url_prefix="/trees")
app.register_blueprint(queue_app, url_prefix="/queue")
app.register_blueprint(graphs_app, url_prefix="/graphs")

if __name__ == "__main__":
    app.run(debug=True)
