SOLAR_POWER_KW = 2.5
PANEL_EFFICIENCY = 0.2

WEATHER_CODE_DESCRIPTIONS = {
    "en": {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        56: "Light freezing drizzle",
        57: "Dense freezing drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        66: "Light freezing rain",
        67: "Heavy freezing rain",
        71: "Slight snow fall",
        73: "Moderate snow fall",
        75: "Heavy snow fall",
        77: "Snow grains",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        85: "Slight snow showers",
        86: "Heavy snow showers",
        95: "Thunderstorm",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail"
    },
    "pl": {
        0: "Bezchmurnie",
        1: "Przeważnie bezchmurnie",
        2: "Częściowe zachmurzenie",
        3: "Pochmurno",
        45: "Mgła",
        48: "Mgła osadzająca szadź",
        51: "Lekka mżawka",
        53: "Umiarkowana mżawka",
        55: "Gęsta mżawka",
        56: "Lekka marznąca mżawka",
        57: "Gęsta marznąca mżawka",
        61: "Słaby deszcz",
        63: "Umiarkowany deszcz",
        65: "Silny deszcz",
        66: "Lekki marznący deszcz",
        67: "Silny marznący deszcz",
        71: "Słabe opady śniegu",
        73: "Umiarkowane opady śniegu",
        75: "Silne opady śniegu",
        77: "Ziarna śniegu",
        80: "Słabe przelotne opady deszczu",
        81: "Umiarkowane przelotne opady deszczu",
        82: "Gwałtowne przelotne opady deszczu",
        85: "Słabe przelotne opady śniegu",
        86: "Silne przelotne opady śniegu",
        95: "Burza",
        96: "Burza z lekkim gradem",
        99: "Burza z silnym gradem"
    }
}

PRECIPITATION_CODES = [51, 53, 55, 56, 57, 61, 63, 65, 66, 67, 71, 73, 75, 77, 80, 81, 82, 85, 86, 95, 96, 99]

OPEN_METEO_API_URL = "https://api.open-meteo.com/v1/forecast"

WEATHER_PARAMS = [
    "weather_code",
    "temperature_2m_max",
    "temperature_2m_min",
    "sunshine_duration",
    "pressure_msl_mean"
]