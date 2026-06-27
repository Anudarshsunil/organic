from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():

    user_question = request.json["question"]

    prompt = f"""
You are an Organic Farm Statistics Assistant.

Answer only questions related to:

• Organic Farming
• Crop Yield
• Fertilizers
• Soil Health
• Water Usage
• Farm Income
• Organic Certification
• Farm Statistics

Question:
{user_question}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "tinyllama",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()

    return jsonify({
        "answer": data.get("response")
    })


if __name__ == "__main__":
    app.run(debug=True)