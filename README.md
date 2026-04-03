# Heritage-Maps

A Flask web server that exposes Vietnamese heritage sites data via a JSON API, reading from a published Google Sheets CSV.

## Project Structure

```
Heritage-Maps/
├── app.py            # Flask application
├── requirements.txt  # Python dependencies
├── .env.example      # Environment variable template
├── .env              # Your local secrets (not committed)
└── README.md
```

## Setup & Running

### 1. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Copy `.env.example` to `.env` and fill in your values:

```bash
cp .env.example .env
```

Edit `.env`:

```
MAPS_API_KEY=your_google_maps_api_key_here
CSV_URL=https://docs.google.com/spreadsheets/d/e/YOUR_SHEET_ID/pub?output=csv
```

> **How to get the CSV URL**: Open your Google Sheet → File → Share → Publish to web → choose **Comma-separated values (.csv)** → click **Publish** and copy the URL.

### 4. Run the server

```bash
python app.py
```

The server starts at `http://127.0.0.1:5000` by default.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/heritage-sites` | Returns all heritage sites as JSON |
| GET | `/api/config` | Returns the Google Maps API key for the front-end |

### Example response – `/api/heritage-sites`

```json
{
  "status": "success",
  "data": [
    {
      "TenDiTich": "Đại Nội Huế",
      "KinhDo": 107.5779,
      "ViDo": 16.4698,
      "MoTa": "Kinh thành Huế, công trình kiến trúc triều Nguyễn.",
      "PlaceID": "ChIJ..."
    }
  ]
}
```

### Expected CSV columns

| Column | Description |
|--------|-------------|
| `TenDiTich` | Name of the heritage site |
| `KinhDo` | Longitude |
| `ViDo` | Latitude |
| `MoTa` | Description |
| `PlaceID` | Google Maps Place ID |

## CORS

CORS is enabled for all origins so that any front-end application can call the API directly.
