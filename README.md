# 📈 MarketIntel Engine: Real-Time Market Analysis

![CI/CD Build](https://img.shields.io/badge/build-passing-brightgreen)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)
![AWS](https://img.shields.io/badge/AWS-EC2-FF9900?logo=amazon-ec2)

## Description

Analyzing real-time market opportunities often requires expensive, rate-limited APIs or manual data aggregation across fragmented financial sources. To bridge the gap between unstructured web data and actionable market intelligence, I developed a robust FastAPI service capable of autonomously scraping, processing, and analyzing region-specific sector data. By implementing a clean, three-layer architecture, the service structurally maps raw DuckDuckGo Search results into an AI analysis pipeline, utilizing the latest `google-genai` Python SDK to generate structured, markdown-formatted reports with high precision.

Because exposing data collection and AI inference endpoints carries significant operational and financial risk, I engineered a custom security layer featuring simple header-based authentication and an in-memory, IP-based rate limiter to restrict users to 5 requests per 60 seconds. Once authenticated, the API utilizes asynchronous routing to fetch real-time market data without requiring paid search API keys, directly feeding the `gemini-2.5-flash` model to provide immediate, synthesized market insights safely and efficiently.

**🚀 Deployment Status & What's Next:** The core backend engine is fully containerized using **Docker** and is currently deployed live on an **AWS EC2** instance to ensure reliable, scalable compute.

* **🔮 Coming Soon:** We are putting the finishing touches on a dedicated frontend! A public link featuring a complete, interactive User Interface is coming very soon.

## Motivation

This project was built to demonstrate a modern, production-ready backend architecture using Python 3.12 and FastAPI. It highlights a clean separation of concerns across routing, data acquisition, and LLM integration. By leveraging `uv` for blazing-fast dependency management and engineering a custom scraping layer to bypass the need for paid search APIs, the project serves as a showcase of resourceful system design and AI integration.

## Quick Start

The project utilizes `uv` for extremely fast dependency management and environment setup. 

**1. Clone the repository:**
```bash
git clone https://github.com/Shreyansh15624/trade-api-project
cd trade-api-project
```

**2. Install dependencies using `uv`:**
```bash
uv sync
```
*(Alternatively, use `pip install -r requirements.txt`)*

**3. Configure Environment Variables:**
Create a `.env` file in the root directory and add your Google Gemini API key:
```env
GEMINI_API_KEY=your_actual_api_key_here
```

**4. Start the Application:**
```bash
uv run main.py
```

**5. Docker Setup (Alternatively):**
If you prefer to run this application via Docker, ensure docker is installed on your machine:
```bash
docker build -t marketintel-engine .
docker run -d -p 8000:8000 --env-file .env marketintel-engine
```

## Usage

Once the server is running, FastAPI automatically provides interactive documentation. You can view the endpoints and test the API directly via:
* **Swagger UI:** `http://127.0.0.1:8000/docs`
* **ReDoc:** `http://127.0.0.1:8000/redoc`

**Example API Request:**
Use `curl` to test the endpoint. The custom `X-API-Key` header is required to pass the security middleware.
```bash
curl -H "X-API-Key: guest-token" http://127.0.0.1:8000/analyze/pharmaceuticals
```
*The API will return a purely formatted Markdown string containing the market analysis, execution time, and insights.*

**Running the Automated Test Suite:**
This project includes automated tests for the security middleware and the core endpoint using `pytest`.
```bash
uv run pytest
```

## Contributing

Contributions are welcome! If you'd like to improve the analysis pipeline or add new data sources:
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/NewMarketSource`).
3. Commit your changes (`git commit -m 'Add new DuckDuckGo scraping parameters'`).
4. Push to the branch (`git push origin feature/NewMarketSource`).
5. Open a Pull Request.

Please ensure all new features pass the existing `pytest` suite before submitting a PR.