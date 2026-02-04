# Agentic Honey-Pot for Scam Detection

This project is an AI-powered Agentic Honey-Pot system built for the **India AI Impact Buildathon**.

The system detects scam messages and autonomously engages scammers using a believable human persona to extract actionable intelligence such as bank account numbers, UPI IDs, and phishing links.

---

## 🚀 Features

- Scam intent detection from incoming messages  
- Autonomous agent handoff after scam detection  
- Multi-turn conversation handling  
- Extraction of structured scam intelligence  
- Secure API access using API key authentication  

---

## 🧠 How It Works (High Level)

1. Incoming messages are received via an API endpoint  
2. Messages are analyzed for scam intent  
3. Once a scam is detected, an autonomous agent takes over  
4. The agent engages the scammer without revealing detection  
5. Actionable intelligence is extracted and returned in JSON format  

---

## 🔐 API Security

- The API is protected using an `x-api-key` header  
- Requests without a valid API key are rejected  

---

## 📡 API Endpoint

**POST** `/honeypot`

### Headers
```

x-api-key: <your-api-key>

````

### Response (Example)
```json
{
  "scam_detected": false,
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
````

---

## ⚠️ Ethical Notice

* This system interacts only with **simulated scam environments**
* No real users or scammers are harmed
* Extracted data is intended solely for fraud prevention research

---

## 🛠 Tech Stack

* Python
* FastAPI
* Uvicorn

---

## 📌 Status

Initial working version deployed for endpoint validation.
Further agent intelligence and extraction logic will be extended in later stages.

```
