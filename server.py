from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from main import run_med_agent
import os

app = Flask(__name__, static_folder=".", static_url_path="")
CORS(app)

# --- Serve Frontend Files ---
@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/<path:path>")
def serve_file(path):
    return send_from_directory(".", path)

# --- Chat Endpoint ---
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        query = data.get("query", "")

        if not query:
            return jsonify({"error": "Query missing"}), 400

        response = run_med_agent(query)
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("🚀 Server running at http://127.0.0.1:5501")
    app.run(host="127.0.0.1", port=5501, debug=True)
