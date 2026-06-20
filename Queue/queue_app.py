from flask import Blueprint, render_template, request, redirect, url_for

queue_app = Blueprint("queue_app", __name__, template_folder="templates")

# Queue data structure
class CustomerServiceQueue:
    def __init__(self):
        self.queue = []

    def arrive(self, customer_name):
        self.queue.append(customer_name)

    def serve(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def get_queue(self):
        return self.queue

# Global queue instance
csq = CustomerServiceQueue()

@queue_app.route("/")
def home():
    return render_template("queue.html", queue=csq.get_queue(), next_customer=csq.peek())

@queue_app.route("/arrive", methods=["POST"])
def arrive():
    name = request.form.get("name")
    if name:
        csq.arrive(name)
    return redirect(url_for("queue_app.home"))

@queue_app.route("/serve")
def serve():
    csq.serve()
    return redirect(url_for("queue_app.home"))
