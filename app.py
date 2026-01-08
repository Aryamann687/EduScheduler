import traceback
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from scheduler import generate_timetable

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    # This will look for templates/index.html
    return render_template("index.html")

@app.route("/api/timetable", methods=["POST"])
def timetable():
    try:
        data = request.get_json()
        
        # We pass the entire 'data' object which now contains:
        # lab_subjects, fixed_slots, teacher_daily_limit, etc.
        result = generate_timetable(data)

        # If the scheduler logic returns a dictionary with an "error" key
        if "error" in result:
            return jsonify(result), 400

        # Return the generated timetable and summary directly to the frontend
        return jsonify(result)

    except Exception as e:
        print("❌ BACKEND ERROR:", str(e))
        traceback.print_exc()
        return jsonify({
            "error": "Internal server error",
            "reason": str(e)
        }), 500

if __name__ == "__main__":
    # Standard development port
    app.run(debug=True, port=5000)

