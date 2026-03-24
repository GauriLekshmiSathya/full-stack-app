from flask import Flask, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

@app.route('/student-details', methods=['GET'])
def get_student_details():
    data = {
        "name": "Gauri Lekshmi Sathya",
        "roll_number": "2023BCS0034",
    }
    return jsonify(data)

@app.route('/')
def home():
    return "Backend is running!"

if __name__ == '__main__':
    app.run(debug=True)