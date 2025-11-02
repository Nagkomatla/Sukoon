from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from datetime import datetime
import json
import os

app = FastAPI(title="Sukoon AI Backend")

@app.get("/")
def root():
    return {"message": "Welcome to Sukoon AI Backend", "status": "online"}

@app.get("/api/sukoon/greeting")
async def dynamic_greeting(patient_name: str = "Patient"):
    message = f"Hello {patient_name}, I hope you are feeling well today. How are you?"
    return JSONResponse(content={"greeting_message": message})

@app.get("/api/sukoon/ending")
async def dynamic_ending(patient_name: str = "Patient"):
    message = f"Thank you {patient_name} for your time. Take care and stay safe!"
    return JSONResponse(content={"ending_message": message})

@app.post("/api/sukoon/postcall")
async def post_call_trigger(request: Request):
    data = await request.json()
    timestamp = datetime.now().isoformat()
    print(f"[{timestamp}] Received post-call data:")
    print(json.dumps(data, indent=2))

    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)
    
    log_file = "logs/post_call_logs.json"
    with open(log_file, "a") as f:
        f.write(json.dumps({"timestamp": timestamp, "data": data}) + "\n")

    return {"status": "success", "received": True}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

