from flask import Blueprint, render_template, request, Response
import csv, io

# Define the Blueprint
array_app = Blueprint("array_app", __name__, template_folder="templates")

last_results = {}

@array_app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        n = int(request.form["num_students"])
        return render_template("marks.html", num_students=n)
    return render_template("index.html")

@array_app.route("/results", methods=["POST"])
def results():
    students = []
    n = int(request.form["num_students"])
    for i in range(n):
        name = request.form.get(f"name{i}")
        mark = int(request.form.get(f"mark{i}"))
        students.append((name, mark))

    marks = [m for (_, m) in students]
    average = sum(marks) / len(marks)
    high = max(marks)
    low = min(marks)
    pass_count = sum(1 for m in marks if m >= 35)
    fail_count = len(marks) - pass_count
    sorted_marks = sorted(marks)
    median = (sorted_marks[n//2 - 1] + sorted_marks[n//2]) / 2 if n % 2 == 0 else sorted_marks[n//2]
    ranked = sorted(students, key=lambda x: x[1], reverse=True)

    global last_results
    last_results = {
        "students": ranked,
        "average": average,
        "high": high,
        "low": low,
        "median": median,
        "pass_count": pass_count,
        "fail_count": fail_count
    }

    return render_template("results.html", students=ranked,
                           average=average, high=high, low=low,
                           pass_count=pass_count, fail_count=fail_count,
                           median=median)

@array_app.route("/download")
def download():
    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow(["Rank", "Name", "Mark", "Status"])
    for i, (name, mark) in enumerate(last_results["students"], start=1):
        status = "Pass" if mark >= 35 else "Fail"
        writer.writerow([i, name, mark, status])

    writer.writerow([])
    writer.writerow(["Average", last_results["average"]])
    writer.writerow(["Highest", last_results["high"]])
    writer.writerow(["Lowest", last_results["low"]])
    writer.writerow(["Median", last_results["median"]])
    writer.writerow(["Pass Count", last_results["pass_count"]])
    writer.writerow(["Fail Count", last_results["fail_count"]])

    response = Response(output.getvalue(), mimetype="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=results.csv"
    return response

