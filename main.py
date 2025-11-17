from fastapi import FastAPI
from firebase import db
from datetime import datetime

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Smart Bus API running"}

# Create a bus document (just an example)
@app.post("/bus/{bus_id}")
def create_bus(bus_id: str):
    bus_ref = db.collection("buses").document(bus_id)
    bus_ref.set({
        "status": "active",
        "created_at": datetime.utcnow()
    })
    return {"message": f"Bus {bus_id} created"}

# Add telemetry
@app.post("/bus/{bus_id}/telemetry")
def add_telemetry(bus_id: str, data: dict):
    telemetry_ref = (
        db.collection("buses")
          .document(bus_id)
          .collection("telemetry")
          .document()
    )
    telemetry_ref.set({
        **data,
        "timestamp": datetime.utcnow()
    })
    return {"message": "Telemetry added"}
