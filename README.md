# Trade Opportunities API

A robust FastAPI service that analyzes market data and provides trade opportunity insights for specific sectors in India.

## System Architecture & Features
This project implements a clean separation of concerns across three main layers:
1. **API & Security Layer (`security.py`, `main.py`):** Handles routing, simple guest authentication via headers, and an in-memory IP-based rate limiter (max 5 requests per 60 seconds).
2. **Data Collection Layer (`data_scraper.py`):** Utilizes `ddgs` (DuckDuckGo Search) to scrape real-time, region-specific (`in-en`) market data without requiring paid search API keys.
3. **AI Analysis Layer (`ai_service.py`):** Integrates the latest `google-genai` Python SDK to pipe scraped data into the `gemini-2.5-flash` model, generating structured, markdown-formatted reports.

## Prerequisites
* Python 3.12+
* [uv](https://github.com/astral-sh/uv) (Extremely fast Python package manager)

## Setup Instructions

1. **Clone the repository and navigate to the directory:**
   ```bash
   git clone <your-repo-link>
   cd trade-api-project

```

2. **Install dependencies using `uv`:**
```bash
uv sync

```


*(Alternatively, use `pip install -r requirements.txt`)*
3. **Configure Environment Variables:**
Create a `.env` file in the root directory and add your Google Gemini API key:
```env
GEMINI_API_KEY=your_actual_api_key_here

```



## Running the Application

Start the Uvicorn server:

```bash
uv run uvicorn main:app

```

### API Documentation

Once the server is running, FastAPI automatically provides interactive documentation. Visit:

* **Swagger UI:** `http://127.0.0.1:8000/docs`
* **ReDoc:** `http://127.0.0.1:8000/redoc`

## Usage Example

Use `curl` to test the endpoint. Note that the custom `X-API-Key` header is required for authentication.

```bash
curl -H "X-API-Key: appscrip-guest-token" [http://127.0.0.1:8000/analyze/pharmaceuticals](http://127.0.0.1:8000/analyze/pharmaceuticals)

```

*The API will return a purely formatted Markdown string containing the market analysis, execution time, and insights.*

## Running Tests

This project includes automated tests for the security middleware and the core endpoint using `pytest`.

```bash
uv run pytest

```

```

### The Final Stretch

Once you have that file saved, you just need to do your final Git workflow:
```bash
git add README.md
git commit -m "docs: add comprehensive README with setup instructions and architecture overview"

```

How does that look to you? Are you ready to zip this up or push it to GitHub and draft that submission email?