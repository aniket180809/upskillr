from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    skill = data.get("skill", "")
    courses = [f"{skill} Beginner Course", f"{skill} Advanced Course"]
    return jsonify({"recommendations": courses})

if __name__ == "__main__":
    app.run(port=5001)
