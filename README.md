# Weather Forecast Backend API

FastAPI-based REST API for weather forecasting with solar energy production calculations.

## Features

- 7-day weather forecast using Open-Meteo API
- Solar energy production calculations for photovoltaic installations
- Weekly weather summary with statistics
- Comprehensive input validation
- CORS support for frontend integration
- Error handling for external API failures

## API Endpoints

### GET `/`
Root endpoint returning API information and available features.

### GET `/health`
Health check endpoint for monitoring service status.

### GET `/api/weather/forecast`
Returns 7-day weather forecast with solar energy calculations.

**Parameters:**
- `latitude` (float): Latitude coordinate (-90 to 90)
- `longitude` (float): Longitude coordinate (-180 to 180)

**Response:**
```json
{
  "forecast": [
    {
      "date": "2025-06-20",
      "weather_code": 0,
      "weather_description": "Clear sky",
      "temperature_max": 25.4,
      "temperature_min": 15.2,
      "sunshine_hours": 8.5,
      "solar_energy_kwh": 4.25
    }
  ]
}
```

### GET `/api/weather/summary`
Returns weekly weather summary with aggregated statistics.

**Parameters:**
- `latitude` (float): Latitude coordinate (-90 to 90)
- `longitude` (float): Longitude coordinate (-180 to 180)

**Response:**
```json
{
  "average_pressure": 1013.2,
  "average_sunshine_hours": 6.8,
  "extreme_temperatures": {
    "min": 12.1,
    "max": 28.9
  },
  "weather_summary": "bez opadów",
  "precipitation_days": 2
}
```

## Solar Energy Calculation

The API calculates estimated solar energy production using the formula:

```
Generated Energy [kWh] = Installation Power [kW] × Exposure Time [h] × Panel Efficiency
```

**Default Configuration:**
- Installation Power: 2.5 kW
- Panel Efficiency: 0.2 (20%)
- Exposure Time: Retrieved from Open-Meteo API (sunshine duration)

## Installation

### Local Development

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the development server:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### Docker Deployment

1. Build the Docker image:
```bash
docker build -t weather-api .
```

2. Run the container:
```bash
docker run -p 8000:8000 weather-api
```

## Project Structure

```
├── main.py              # FastAPI application entry point
├── config.py            # Configuration constants
├── models.py            # Pydantic data models
├── requirements.txt     # Python dependencies
├── Dockerfile          # Docker configuration
├── services/
│   ├── __init__.py
│   └── weather_service.py    # Weather data processing logic
└── routers/
    ├── __init__.py
    └── weather_router.py     # API route definitions
```

## Dependencies

- **FastAPI**: Modern web framework for building APIs
- **uvicorn**: ASGI server for running FastAPI applications
- **httpx**: Async HTTP client for external API calls
- **pydantic**: Data validation and settings management
- **python-multipart**: Form data parsing support

## External APIs

- **Open-Meteo API**: Free weather API providing forecast data
  - Documentation: https://open-meteo.com/en/docs

## Weather Codes

The API supports weather code interpretation based on WMO standards:
- 0: Clear sky
- 1-3: Mainly clear to overcast
- 45-48: Fog conditions
- 51-67: Drizzle and rain variations
- 71-86: Snow conditions
- 95-99: Thunderstorm conditions

## Error Handling

The API includes comprehensive error handling for:
- Invalid coordinate parameters
- External API failures
- Network connectivity issues
- Data validation errors

## CORS Configuration

The API is configured to accept requests from all origins for development purposes. For production deployment, configure specific allowed origins in the CORS middleware settings.