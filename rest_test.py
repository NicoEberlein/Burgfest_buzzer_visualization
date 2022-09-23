from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Web-App Config
app = FastAPI()

origins = [
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/data")
async def data():
    return {"data":[5,8,2]}
