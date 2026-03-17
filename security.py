from tests.test_main import client
from fastapi import HTTPException, Security, Request
from fastapi.security import APIKeyHeader
import time

# ---- 1. Simple Guest Authentication ----
# Lookingfor the header called as X-API-Key in the incoming request
API_KEY_HEADER = APIKeyHeader(name="X-API-Key", auto_error=False)
DUMMY_TOKEN = "appscrip-guest-token"


# ---- 2. In-memory Rate Limiting ----
# Using a dictionary data type & it will reset when the server restarts
RATE_LIMIT_DB = dict() # Format: {"ip_address": [timespamp1, timestamp2]}
MAX_REQUESTS = 5
TIME_WINDOW = 60 # seconds

async def verify_auth_and_rate_limit(request: Request, api_key: str = Security(API_KEY_HEADER)):
    # Middleware function that checks for the API Key & counts the request per IP
    if api_key != DUMMY_TOKEN: # Checking Auth
        raise HTTPException(status_code=401, detail="Unauthrized! Please provide a guest token in the X-API_Key Header!")
    
    # Check Rate Limit
    client_ip = request.client.host
    current_time = time.time()

    # Adding all the new IP Users to the dictionary
    if client_ip not in RATE_LIMIT_DB:
        RATE_LIMIT_DB[client_ip] = []
    
    # Filtering out the timestamps
    RATE_LIMIT_DB[client_ip] = [t for t in RATE_LIMIT_DB[client_ip] if current_time - t < TIME_WINDOW]

    # If there more than 5 requests in the last minute, block them!
    if len(RATE_LIMIT_DB[client_ip]) >= MAX_REQUESTS:
        raise HTTPException(status_code=429, detail="Rate Limit Exceeded! Please try again in a minute.")
    
    # If they pass the checks, log their current request time
    RATE_LIMIT_DB[client_ip].append(current_time)

    return True