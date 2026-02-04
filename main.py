from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

API_KEY = "test123"

@app.post("/honeypot")
def honeypot(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    return {
        "scam_detected": False,
        "confidence": 0.5,
        "agent_status": "idle",
        "engagement": {
            "turns": 1,
            "duration_seconds": 1
        },
        "extracted_intelligence": {
            "bank_accounts": [],
            "upi_ids": [],
            "phishing_links": []
        }
    }
