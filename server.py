from flask import Flask, request, jsonify, send_from_directory, abort
from flask_cors import CORS
import os

# Disable Flask's built-in static file handling so our custom handler runs
app = Flask(__name__, static_folder=None)
CORS(app)

# ------------------ PAGE ROUTES ------------------

@app.route("/")
def home():
    return send_from_directory("opening_page", "op.html")

@app.route("/chat")
def chat_page():
    return send_from_directory(".", "index.html")

# ------------------ API ROUTE ------------------

@app.route("/api/chat", methods=["POST"])
def chat_api():
    try:
        data = request.get_json()
        query = data.get("query", "")

        if not query:
            return jsonify({"error": "Query missing"}), 400

        try:
            from main import run_med_agent
        except Exception as e:
            return jsonify({"error": f"Failed importing agent: {e}"}), 500

        response = run_med_agent(query)
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ------------------ STATIC FILES ------------------

@app.route("/<path:path>")
def serve_file(path):
    # Serve from project root if file exists, otherwise try opening_page folder
    base_dir = os.path.dirname(__file__)
    root_path = os.path.join(base_dir, path)
    opening_path = os.path.join(base_dir, "opening_page", path)

    if os.path.exists(root_path):
        return send_from_directory(base_dir, path)
    if os.path.exists(opening_path):
        return send_from_directory(os.path.join(base_dir, "opening_page"), path)
    abort(404)


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5503))
    print(f"🚀 Server running at http://127.0.0.1:{port}")
    app.run(host="127.0.0.1", port=port, debug=True)
