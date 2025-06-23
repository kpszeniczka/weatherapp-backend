from fastapi import APIRouter, Query, HTTPException
from typing import Optional, Literal
from services import WeatherService
from models import WeekSummary

router = APIRouter(prefix="/api/weather", tags=["weather"])
weather_service = WeatherService()


@router.get("/forecast", response_model=dict)
async def get_weather_forecast(
    latitude: float = Query(..., ge=-90, le=90, description="Latitude coordinate"),
    longitude: float = Query(..., ge=-180, le=180, description="Longitude coordinate"),
    language: Optional[Literal["en", "pl"]] = Query("en", description="Language for weather descriptions")
):
    try:
        forecast_days = await weather_service.get_forecast(latitude, longitude, language)
        return {"forecast": [day.dict() for day in forecast_days]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.get("/summary", response_model=WeekSummary)
async def get_week_summary(
    latitude: float = Query(..., ge=-90, le=90, description="Latitude coordinate"),
    longitude: float = Query(..., ge=-180, le=180, description="Longitude coordinate"),
    language: Optional[Literal["en", "pl"]] = Query("en", description="Language for weather summary")
):
    try:
        return await weather_service.get_week_summary(latitude, longitude, language)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")