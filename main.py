from fastapi import FastAPI, Depends
from security import verify_auth_and_rate_limit

# Initializing the Application!
app = FastAPI(
    title="Trade Opportuinites API",
    desription="Analyzes market data & provides trade opportunity insights for specific sectors in India",
    version="1.0.0",
)

# Creating the single GET Endpoint
# The 'dependencies' array forces the request to pass our security checks first
@app.get("/analyze/{sector}", dependencies=[Depends(verify_auth_and_rate_limit)])
async def analyze_sector(sector: str):
    # Analyzes the psecificed market sector and returns a structured markdown report
    # Formatting the sector identifier to be lower case & stripping whitespaces tohave cleaner data
    clean_sector = sector.lower().strip()

    """
    Next Tasks:
    1. Add Web Search for current Market Data
    2. Send data to Gemini for Analysis
    3. Return Markdown Report
    """

    return {
        "status": "success",
        "message": f"Security passed! ready to analyze the '{clean_sector}' sector."
    }