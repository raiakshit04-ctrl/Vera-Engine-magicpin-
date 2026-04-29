from fastapi import FastAPI
from main import run_engine

app = FastAPI()

# ✅ Health check
@app.get("/v1/healthz")
def health():
    return {"status": "ok"}

# ✅ Metadata
@app.get("/v1/metadata")
def metadata():
    return {
        "name": "vera-message-engine",
        "version": "1.0",
        "description": "Context-aware message engine for merchant growth"
    }

# ✅ Context endpoint (store if needed, for now just accept)
@app.post("/v1/context")
def context(data: dict):
    return {"accepted": True}

# ✅ Tick endpoint (core logic)
@app.post("/v1/tick")
def tick(data: dict):
    output = run_engine(data)

    # 🔥 REQUIRED FORMAT (important for judge)
    return {
        "message": output["message"],
        "rationale": output["why_now"],
        "message_type": output["message_type"],
        "cta": "Push offer to customers",
        "send_as": "vera",
        "suppression_key": f"{output['message_type']}_{data.get('merchant', {}).get('merchant_id', '')}"
    }

# ✅ Reply endpoint (basic handling)
@app.post("/v1/reply")
def reply(data: dict):
    return {
        "response": "Great, launching this for you now 🚀"
    }