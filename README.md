### How to send it Using FastAPI Docs
- Go to: http://127.0.0.1:8000/docs
- Find POST /bus/{bus_id}/telemetry
- Click “Try it out”
- Enter bus_id = BUS_01
- Paste JSON into the Request body box
- Press Execute

### JSON example
{
  "gps": {"lat": 36.81, "lng": 10.15},
  "speed": 42.7,
  "temperature": 31.2,
  "peopleIn": 2,
  "peopleOut": 1,
  "currentOccupancy": 27,
  "acceleration": {"x":0.01, "y":-0.12, "z":9.81},
  "gyro": {"x":0.002, "y":0.001, "z":-0.008},
  "magnetic": {"x":30, "y":-15, "z":42},
  "status": "moving"
}
