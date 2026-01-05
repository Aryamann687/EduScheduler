from flask import Flask, request, jsonify
from flask_cors import CORS
from scheduler import generate_timetable

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "EduScheduler backend running"

@app.route("/api/timetable", methods=["POST"])
def timetable():
    data = request.get_json()
    result = generate_timetable(data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
