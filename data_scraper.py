from duckduckgo_search import DDGS
import logging

# Simple logging setup to monitor the process via the Kubuntu Terminal
logging.baseConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_market_data(sector: str):
    """
    Searching for recent news & market data for a specifc sector in India.
    Returns a compiled string of data for the AI to analyze.
    """
    logger.info(f"Fetching market data for the '{sector}' sector in India.")

    # Tailoring the query strictly to the assignment requirements
    query = f"{sector} sector market trade opportunities in India current NEWS"

    scraped_data = []

    # Wrapping the logic in a try-except block to handle potential network / API failures
    try:
        with DDGS() as ddgs:
            results = ddgs.text(query, region='in-en', safesearch='moderate', timelimit='w', max_results=5)
            # Fecthing about 5 recent search results specifically from the Indian Region ('in-en')
            # This approach helps keep the API fast, while ensuring that the LLM has pletny context

            for resul in results:
                title = result.get('title', 'No Title')
                body =  result.get('body', 'No Content')
                scraped_data.append(f"Title: {title}\nSnippet: {body}\n")
            
        if not scraped_data:
            return "No recent market data found for this sector!"
        
        # Combining everything into a single text block that we can pass to Gemini later on!
        return "\n---\n".join(scraped_data)
    
    except Exception as e:
        logger.error(f"DuckDuckGo Search Failed! Reason: {str(e)}")
        return f"Error gathering market data: {str(e)}"