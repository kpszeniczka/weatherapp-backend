import httpx
import statistics
from typing import Dict, List, Any
from fastapi import HTTPException

from config import (
    SOLAR_POWER_KW, 
    PANEL_EFFICIENCY, 
    WEATHER_CODE_DESCRIPTIONS,
    PRECIPITATION_CODES,
    OPEN_METEO_API_URL,
    WEATHER_PARAMS
)
from models import ForecastDay, WeekSummary


class WeatherService:
    @staticmethod
    def calculate_solar_energy(sunshine_hours: float) -> float:
        return SOLAR_POWER_KW * sunshine_hours * PANEL_EFFICIENCY

    @staticmethod
    def is_precipitation_day(weather_code: int) -> bool:
        return weather_code in PRECIPITATION_CODES

    async def fetch_weather_data(self, latitude: float, longitude: float) -> Dict[str, Any]:
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "daily": WEATHER_PARAMS,
            "timezone": "auto",
            "forecast_days": 7
        }
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(OPEN_METEO_API_URL, params=params)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPError as e:
                raise HTTPException(status_code=500, detail=f"Error fetching weather data: {str(e)}")

    async def get_forecast(self, latitude: float, longitude: float) -> List[ForecastDay]:
        weather_data = await self.fetch_weather_data(latitude, longitude)
        daily_data = weather_data["daily"]
        forecast_days = []
        
        for i in range(7):
            date = daily_data["time"][i]
            weather_code = daily_data["weather_code"][i]
            temp_max = daily_data["temperature_2m_max"][i]
            temp_min = daily_data["temperature_2m_min"][i]
            sunshine_duration_seconds = daily_data["sunshine_duration"][i]
            
            sunshine_hours = sunshine_duration_seconds / 3600 if sunshine_duration_seconds else 0
            solar_energy = self.calculate_solar_energy(sunshine_hours)
            
            forecast_days.append(ForecastDay(
                date=date,
                weather_code=weather_code,
                weather_description=WEATHER_CODE_DESCRIPTIONS.get(weather_code, "Unknown"),
                temperature_max=temp_max,
                temperature_min=temp_min,
                sunshine_hours=round(sunshine_hours, 2),
                solar_energy_kwh=round(solar_energy, 2)
            ))
        
        return forecast_days

    async def get_week_summary(self, latitude: float, longitude: float) -> WeekSummary:
        weather_data = await self.fetch_weather_data(latitude, longitude)
        daily_data = weather_data["daily"]
        
        pressures = [p for p in daily_data["pressure_msl_mean"] if p is not None]
        sunshine_durations = [s / 3600 if s else 0 for s in daily_data["sunshine_duration"]]
        all_temps = daily_data["temperature_2m_max"] + daily_data["temperature_2m_min"]
        weather_codes = daily_data["weather_code"]
        
        avg_pressure = statistics.mean(pressures) if pressures else 0
        avg_sunshine_hours = statistics.mean(sunshine_durations)
        
        extreme_temps = {
            "min": min(all_temps),
            "max": max(all_temps)
        }
        
        precipitation_days = sum(1 for code in weather_codes if self.is_precipitation_day(code))
        weather_summary = "with precipitation" if precipitation_days >= 4 else "without precipitation"
        
        return WeekSummary(
            average_pressure=round(avg_pressure, 1),
            average_sunshine_hours=round(avg_sunshine_hours, 2),
            extreme_temperatures=extreme_temps,
            weather_summary=weather_summary,
            precipitation_days=precipitation_days
        )