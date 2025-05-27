from flask import Flask, request, jsonify
import subprocess
import uuid
import os

app = Flask(__name__)

@app.route("/research", methods=["POST"])
def handle_research():
    data = request.json
    topic = data.get("topic")
    duration = data.get("duration", "short")  # "short", "medium", or "long"

    if not topic:
        return jsonify({"error": "Missing topic"}), 400

    session_id = str(uuid.uuid4())[:8]
    os.environ["MCP_DURATION"] = duration

    try:
        subprocess.run(["python", "MCP_assistant.py", topic], check=True)
        subprocess.run(["python", "send_to_claude.py"], check=True)
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500

    filename = topic.lower().replace(" ", "_") + ".md"
    return jsonify({
        "session_id": session_id,
        "message": f"Research complete for '{topic}'",
        "markdown_file": f"/results/{filename}"
    })

@app.route("/")
def index():
    return "🧠 MCP Server Running"

if __name__ == "__main__":
    app.run(port=7001)
