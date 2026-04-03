import logging
import os
import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.INFO)

MAPS_API_KEY = os.getenv("MAPS_API_KEY", "")
CSV_URL = os.getenv(
    "CSV_URL",
    "https://docs.google.com/spreadsheets/d/e/YOUR_SHEET_ID/pub?output=csv",
)


@app.route("/api/heritage-sites", methods=["GET"])
def get_heritage_sites():
    try:
        df = pd.read_csv(CSV_URL)
        expected_columns = ["TenDiTich", "KinhDo", "ViDo", "MoTa", "PlaceID"]
        for col in expected_columns:
            if col not in df.columns:
                df[col] = None
        df = df[expected_columns]
        df = df.where(pd.notnull(df), None)
        sites = df.to_dict(orient="records")
        return jsonify({"status": "success", "data": sites})
    except Exception as e:
        app.logger.error("Failed to load heritage sites: %s", e)
        return jsonify({"status": "error", "message": "Failed to load heritage sites data."}), 500


@app.route("/api/config", methods=["GET"])
def get_config():
    return jsonify({"mapsApiKey": MAPS_API_KEY})


if __name__ == "__main__":
    debug = os.getenv("FLASK_DEBUG", "False").lower() in ("1", "true", "yes")
    app.run(debug=debug)
