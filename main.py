from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

origins = ["*"]
snickers = ["snickers"]

app = FastAPI()
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("get_snickers")
def get_snickers():
    return snickers

@app.post("/add_snickers")
def add_snickers(name: str):
    if name in snickers:
        return "Error: there is already such snickers"
    snickers.append(name)
    return "success"
#if __name__ == "__main__":
 #   uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8500)))
