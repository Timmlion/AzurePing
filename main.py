from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

# Counter to track the number of calls
call_counter = 0

@app.get("/status")
def get_status():
    global call_counter
    call_counter += 1  # Increment the counter on each call
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {
        "datetime": current_datetime,
        "message": "still here",
        "call_count": call_counter
    }