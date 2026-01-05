from flask import Flask, jsonify, request
from flask_cors import CORS
from scheduler import generate_timetable

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "EduScheduler Flask server running 🚀"

@app.route("/api/timetable", methods=["POST"])
def timetable():
    data = request.get_json()

    subjects = data.get("subjects", [])
    periods_per_day = data.get("periods_per_day", 4)

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    # TEMP constraint: each subject max once per day
    subject_limits = {s: len(days) for s in subjects}

    timetable = generate_timetable(
        subjects=subjects,
        periods_per_day=periods_per_day,
        days=days,
        subject_limits=subject_limits
    )

    return jsonify({"timetable": timetable})

if __name__ == "__main__":
    app.run(debug=True, port=5000)