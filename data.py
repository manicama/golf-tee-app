import requests

def get_tee_times():
    # This is still mock data for now
    # but notice it's sitting alongside a real API call below
    return [
        {"course": "Lincoln Park", "date": "2026-04-10", "time": "7:30 AM", "price": 52, "source": "GolfNow", "holes": 18},
        {"course": "Lincoln Park", "date": "2026-04-10", "time": "8:00 AM", "price": 55, "source": "GolfNow", "holes": 18},
        {"course": "Lincoln Park", "date": "2026-04-10", "time": "7:30 AM", "price": 50, "source": "Lincoln Park", "holes": 18},
        {"course": "Lincoln Park", "date": "2026-04-11", "time": "8:00 AM", "price": 54, "source": "Lincoln Park", "holes": 18},
        {"course": "Lincoln Park", "date": "2026-04-11", "time": "8:30 AM", "price": 56, "source": "Lincoln Park", "holes": 18},
        {"course": "Golden Gate Park GC", "date": "2026-04-11", "time": "8:30 AM", "price": 56, "source": "Lincoln Park", "holes": 18},
        {"course": "Golden Gate Park GC", "date": "2026-04-11", "time": "11:30 AM", "price": 56, "source": "Lincoln Park", "holes": 18},
        {"course": "Golden Gate Park GC", "date": "2026-04-10", "time": "9:30 AM", "price": 56, "source": "Lincoln Park", "holes": 18},
    ]

def get_weather():
    # Lincoln Park Golf Course coordinates
    url = "https://api.open-meteo.com/v1/forecast?latitude=37.7785&longitude=-122.4596&current_weather=true"
    
    # Make the API call
    response = requests.get(url)
    
    # Convert response to a Python dictionary
    data = response.json()
    
    # Pull out just what we need and return it
    weather = data["current_weather"]
    return {
        "temperature": round((weather["temperature"] * 9/5) + 32),  # convert C to F
        "windspeed": weather["windspeed"],
        "is_day": weather["is_day"]
    }