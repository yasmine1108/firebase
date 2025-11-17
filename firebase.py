import firebase_admin
from firebase_admin import credentials, firestore

from datetime import datetime
import os

print(os.getcwd())

# Load key file (must be in the same folder)
cred = credentials.Certificate("smart-bus-9e53c-firebase-adminsdk-fbsvc-da46176502.json")

# Initialize
firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()

# # --- Test write ---
# doc_ref = db.collection("testCollection").document("testDoc")
# doc_ref.set({
#     "message": "Firestore connected successfully!",
# })

# print("Done! Check your Firestore console.")

def create_bus(bus_id, plate_number, route_id, capacity_max):
    doc_ref = db.collection("buses").document(bus_id)
    doc_ref.set({
        "busId": bus_id,
        "plateNumber": plate_number,
        "routeId": route_id,
        "capacityMax": capacity_max
    })
    print(f"Bus {bus_id} created.")
    
def add_telemetry(bus_id, gps_lat, gps_lng, speed, temperature,
                  people_in, people_out, occupancy,
                  acc, gyro, magnetic, status):
    
    timestamp = datetime.utcnow().isoformat()

    data = {
        "timestamp": firestore.SERVER_TIMESTAMP,
        "gps": { "lat": gps_lat, "lng": gps_lng },
        "speed": speed,
        "temperature": temperature,
        "peopleIn": people_in,
        "peopleOut": people_out,
        "currentOccupancy": occupancy,
        "acceleration": acc,
        "gyro": gyro,
        "magnetic": magnetic,
        "status": status
    }

    telemetry_ref = db.collection("buses") \
                       .document(bus_id) \
                       .collection("telemetry") \
                       .document(timestamp)

    telemetry_ref.set(data)

    print(f"Telemetry added for {bus_id} at {timestamp}")

def create_route(route_id, name, start_point, end_point, stops):
    route_ref = db.collection("routes").document(route_id)
    route_ref.set({
        "routeId": route_id,
        "name": name,
        "startPoint": start_point,
        "endPoint": end_point,
        "stops": stops
    })
    print(f"Route {route_id} created.")

def update_bus_status(bus_id, gps, speed, temperature, occupancy, next_stop, eta):
    status_ref = db.collection("busStatus").document(bus_id)
    status_ref.set({
        "gps": gps,
        "speed": speed,
        "temperature": temperature,
        "currentOccupancy": occupancy,
        "nextStop": next_stop,
        "eta": eta,
        "lastUpdate": firestore.SERVER_TIMESTAMP
    })
    print(f"Status updated for {bus_id}")

def update_predictions(bus_id, eta_map):
    pred_ref = db.collection("predictions").document(bus_id)
    pred_ref.set({
        "etaToEachStop": eta_map,
        "lastModelUpdate": firestore.SERVER_TIMESTAMP
    })
    print(f"Predictions stored for {bus_id}")


# create_bus("BUS_01", "TN-1234", "R01", 50)

# add_telemetry(
#     bus_id="BUS_01",
#     gps_lat=36.8,
#     gps_lng=10.17,
#     speed=42.7,
#     temperature=31.2,
#     people_in=2,
#     people_out=1,
#     occupancy=27,
#     acc={"x":0.01, "y":-0.12, "z":9.81},
#     gyro={"x":0.002, "y":0.001, "z":-0.008},
#     magnetic={"x":30, "y":-15, "z":42},
#     status="moving"
# )

# create_route(
#     route_id="R01",
#     name="Main Line",
#     start_point={"lat": 36.80, "lng": 10.10},
#     end_point={"lat": 36.90, "lng": 10.20},
#     stops=[
#         {"name": "Station A", "lat": 36.81, "lng": 10.15},
#         {"name": "Station B", "lat": 36.85, "lng": 10.18}
#     ]
# )