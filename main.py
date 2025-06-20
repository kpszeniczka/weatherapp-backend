from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import weather_router

app = FastAPI(
    title="Weather Forecast API",
    version="1.0.0",
    description="API for weather forecasting with solar energy calculations and push notifications"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(weather_router)

@app.get("/")
async def root():
    return {
        "message": "Weather Forecast API with Push Notifications", 
        "version": "1.0.0",
        "features": [
            "7-day weather forecast",
            "Solar energy predictions",
        ],
        "endpoints": {
            "weather": {
                "forecast": "/api/weather/forecast",
                "summary": "/api/weather/summary"
            },
        }
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "Weather Forecast API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)