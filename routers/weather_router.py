from fastapi import APIRouter, Query, HTTPException
from services import WeatherService
from models import WeekSummary

router = APIRouter(prefix="/api/weather", tags=["weather"])
weather_service = WeatherService()

@router.get("/forecast", response_model=dict)
async def get_weather_forecast(
    latitude: float = Query(..., ge=-90, le=90, description="Latitude coordinate"),
    longitude: float = Query(..., ge=-180, le=180, description="Longitude coordinate")
):
    try:
        forecast_days = await weather_service.get_forecast(latitude, longitude)
        return {"forecast": [day.dict() for day in forecast_days]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.get("/summary", response_model=WeekSummary)
async def get_week_summary(
    latitude: float = Query(..., ge=-90, le=90, description="Latitude coordinate"),
    longitude: float = Query(..., ge=-180, le=180, description="Longitude coordinate")
):
    try:
        return await weather_service.get_week_summary(latitude, longitude)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")