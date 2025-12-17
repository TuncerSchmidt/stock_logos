from fastapi import FastAPI, Response
import requests

app = FastAPI()

BASE_URL = "https://raw.githubusercontent.com/davidepalazzo/ticker-logos/main/ticker_icons"

@app.get("/")
def home():
    return {"status": "Logo API running"}

@app.get("/logo/{ticker}")
def get_logo(ticker: str):
    ticker = ticker.upper()
    logo_url = f"{BASE_URL}/{ticker}.png"
    
    resp = requests.get(logo_url)

    if resp.status_code == 200:
        # PNG içerik döndür (binary)
        return Response(content=resp.content, media_type="image/png")
    else:
        return {
            "ticker": ticker,
            "error": "Logo not found",
            "status": resp.status_code,
            "url_checked": logo_url
        }
