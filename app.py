# app.py

from flask import Flask, request, jsonify
from transformers import pipeline
import os

# Flask uygulaması
app = Flask(__name__)

# Model yolu (macOS masaüstü yolu)
model_path = os.path.expanduser("~/Desktop/10_finetuned")

# Modeli yükle
summarizer = pipeline("summarization", model=model_path)

# Metni özetleyen API endpoint'i
@app.route("/summarize", methods=["POST"])
def summarize():
    # Post request'ten metni al
    data = request.get_json()
    text = data.get("text", "")
    
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    # Özetleme işlemi
    summary = summarizer(text)
    return jsonify({"summary": summary[0]['summary_text']}), 200

if __name__ == "__main__":
    app.run(debug=True)
