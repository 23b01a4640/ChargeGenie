from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.auth.routes import router as auth_router
from app.maps.routes import router as maps_router
from app.preferences.routes import router as preferences_router
from app.vehicle.routes import router as vehicle_router
from app.history.routes import router as history_router
from app.stations.routes import router as stations_router
from app.recommendations.routes import router as recommendation_router

app = FastAPI(title="ChargeGenie API")

# 🔐 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Routers
app.include_router(auth_router)
app.include_router(maps_router)
app.include_router(preferences_router)
app.include_router(vehicle_router)
app.include_router(history_router)
app.include_router(stations_router)
app.include_router(recommendation_router)


@app.get("/")
def health():
    return {"status": "ChargeGenie backend running"}
