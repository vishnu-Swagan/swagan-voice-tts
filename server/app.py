"""
Swagan Voice TTS - Backend Server
A Text-to-Speech API powered by Coqui TTS engine
"""

import argparse
import io
import os
from threading import Lock

from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from TTS.api import TTS

app = Flask(__name__)
CORS(app)

# Global lock for thread-safe TTS inference
lock = Lock()

# Initialize TTS model
MODEL_NAME = os.environ.get("TTS_MODEL", "tts_models/en/ljspeech/tacotron2-DDC")
print(f"Loading model: {MODEL_NAME}")
tts = TTS(model_name=MODEL_NAME, progress_bar=False)
print("Model loaded successfully!")


@app.route("/")
def index():
      return jsonify({
                "name": "Swagan Voice TTS API",
                "version": "1.0.0",
                "status": "running",
                "model": MODEL_NAME,
                "endpoints": {
                              "GET /": "API info",
                              "GET /api/tts?text=<text>": "Synthesize speech",
                              "POST /api/tts": "Synthesize speech (JSON body)",
                              "GET /api/models": "List available models",
                              "GET /health": "Health check"
                }
      })


@app.route("/health")
def health():
      return jsonify({"status": "healthy"})


@app.route("/api/models")
def list_models():
      return jsonify({"models": TTS().list_models()})


@app.route("/api/tts", methods=["GET", "POST"])
def synthesize():
      with lock:
                if request.method == "POST":
                              data = request.get_json(silent=True) or {}
                              text = data.get("text", "")
                              speaker = data.get("speaker", None)
                              language = data.get("language", None)
else:
            text = request.args.get("text", "")
            speaker = request.args.get("speaker", None)
              language = request.args.get("language", None)

        if not text:
                      return jsonify({"error": "No text provided"}), 400

                              if len(text) > 5000:
            return jsonify({"error": "Text too long. Maximum 5000 characters."}), 400

        print(f" > Synthesizing: {text[:100]}...")

                try:
                              wav = tts.tts(text=text)
                              out = io.BytesIO()
                      tts.synthesizer.save_wav(wav, out)
            out.seek(0)
            return send_file(out, mimetype="audio/wav")
except Exception as e:
            return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
      parser = argparse.ArgumentParser(description="Swagan Voice TTS Server")
                          parser.add_argument("--port", type=int, default=int(os.environ.get("PORT", 5002)))
    parser.add_argument("--host", type=str, default="0.0.0.0")
    args = parser.parse_args()

            print(f"Starting Swagan Voice TTS server on {args.host}:{args.port}")
    app.run(host=args.host, port=args.port, debug=False)
