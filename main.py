from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import PlainTextResponse
from security import verify_auth_and_rate_limit
from data_scraper import fetch_market_data
from ai_service import generate_market_report
import time

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
    # Analyzes the specificed market sector and returns a structured markdown report
    
    # Staring the stopwatch
    start_time = time.time()
    
    # Formatting the sector identifier to be lower case & stripping whitespaces tohave cleaner data
    clean_sector = sector.lower().strip()

    if not clean_sector:
        raise HTTPException(status_code=400, detail="'Sector Name' cannot be empty!")

    # Collecting the Data: Fetching live market data from DuckDuckGo 
    scraped_data = fetch_market_data(clean_sector)

    # Analyzing the Data: Passing the scraped_data to Gemini AI for analysis
    markdown_report = generate_market_report(clean_sector, scraped_data)

    # Stopwatch stopped & we return the total time elapsed time in seconds
    process_time = time.time() - start_time

    # Appending the runtime to the end of the Markdown Report
    final_report = f"{markdown_report}\n\n---\n*Report generated in {process_time:.2f} seconds*"
    
    # Returning the Report: We use PlainTextResponse, so the markdown formatting renders
    # perfectly and can be saved directly as a '.md' file
    return PlainTextResponse(content=final_report, media_type="text/markdown")