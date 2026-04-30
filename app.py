from fastapi import FastAPI
from main import run_engine

app = FastAPI()

@app.get("/v1/healthz")
def health():
    return {"status": "ok"}

@app.get("/v1/metadata")
def metadata():
    return {
        "name": "vera-message-engine",
        "version": "1.0",
        "description": "Context-aware message engine for merchant growth"
    }

@app.post("/v1/context")
def context(data: dict):
    return {"accepted": True}

@app.post("/v1/tick")
def tick(data: dict):
    output = run_engine(data)

    return {
        "message": output["message"],
        "rationale": output["why_now"],
        "message_type": output["message_type"],
        "cta": "Push offer to customers",
        "send_as": "vera",
        "suppression_key": f"{output['message_type']}_{data.get('merchant', {}).get('merchant_id', '')}"
    }

@app.post("/v1/reply")
def reply(data: dict):
    return {
        "response": "Great, launching this for you now 🚀"
    }
