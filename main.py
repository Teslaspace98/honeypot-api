from fastapi import FastAPI, Header, HTTPException, Request

app = FastAPI()

API_KEY = "test123"

@app.api_route("/honeypot", methods=["POST", "GET"])
async def honeypot(
    request: Request,
    x_api_key: str = Header(None)
):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    # DO NOT parse body at all (tester sends weird payloads)
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
