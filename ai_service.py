import os
import google.generativeai as genai
from dotenv import load_dotenv
import logging

# Setting up Logging
logging.baseConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Loading the Environment Variables
load_dotenv()

# Configure the Gemini API Key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is missing, please check the .env file!")

genai.cofigure(api_key=api_key)

# Initialize the model (Using flash for speed, which is grate for API responses)
model = genai.GenerativeModel('genai-2.5-flash')

def generate_Market_Report(sector: str, scraped_data: str):
    """
    This function takes the raw scraped data and uses Gemini to generate a structured markfown report.
    """
    logger.info(f"Generating Ai report for the '{sector}' sector...")

    # This is our Main Prompt, engineered to serve a very specific purpose!
    # We give the AI a Persona, the raw data, and strict output instructions.
    prompt="""
    You are an expert market analyst focusing on the Indian Market.
    I will provide you with the target sector and some recent news snippets scraped from the web.
    Your task is to analyze this data and write a structured market analysis report highlighting current trade opportunities in India.

    Target Sector: {sector}

    Recent Market Data:
    {scraped_data}

    Requirements:
    1. Format the output STRICTLY as Markdown! Do not include HTML!
    2. Include the following sections,
        - Executive Summary
        - Current Market Trends
        - Trade Opportunities
        - Potential Risks
    3. Base your analysis primarily on the provided market data.
    """

    try:
        # Send the prompt to Gemini API
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        logger.error(f"Gemini API Generation Failed: {str(e)}")
        return f"# Erorr Generating Report\n\nAn error occurred while analyzing the data with the AI Model: {str(e)}"