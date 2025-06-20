from pydantic import BaseModel, validator
from typing import Dict, Optional


class LocationParams(BaseModel):
    latitude: float
    longitude: float
    
    @validator('latitude')
    def validate_latitude(cls, v):
        if not -90 <= v <= 90:
            raise ValueError('Latitude must be between -90 and 90')
        return v
    
    @validator('longitude')
    def validate_longitude(cls, v):
        if not -180 <= v <= 180:
            raise ValueError('Longitude must be between -180 and 180')
        return v


class PushSubscription(BaseModel):
    endpoint: str
    keys: Dict[str, str]


class NotificationRequest(BaseModel):
    subscription: PushSubscription
    latitude: float
    longitude: float
    user_id: Optional[str] = None


class ForecastDay(BaseModel):
    date: str
    weather_code: int
    weather_description: str
    temperature_max: float
    temperature_min: float
    sunshine_hours: float
    solar_energy_kwh: float


class WeekSummary(BaseModel):
    average_pressure: float
    average_sunshine_hours: float
    extreme_temperatures: Dict[str, float]
    weather_summary: str
    precipitation_days: int


class WeatherAlert(BaseModel):
    date: str
    message: str
    severity: str
    weather_code: int
    temp_max: float
    temp_min: float