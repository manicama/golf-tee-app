# scraper.py
import requests
from bs4 import BeautifulSoup

def get_forecast():
    # The URL we inspected
    url = "https://forecast.weather.gov/MapClick.php?CityName=San+Francisco&state=CA&site=MTR&textField1=37.7772&textField2=-122.4168"
    
    # Step 1: Fetch the page — same requests.get() you already know
    response = requests.get(url)
    
    # Step 2: Parse the HTML — this is new
    # BeautifulSoup takes the raw HTML text and makes it navigable
    # "lxml" is the parser we installed — it reads the HTML structure
    soup = BeautifulSoup(response.text, "lxml")
    
    # Step 3: Find the forecast container
    # find() finds the FIRST matching element
    # find_all() finds ALL matching elements
    forecast_items = soup.find(id="seven-day-forecast-list")
    
    # Step 4: Get each individual forecast period
    periods = forecast_items.find_all(class_="forecast-tombstone")
    
    # Step 5: Extract data from each period
    forecasts = []
    for period in periods:
        # .find() drills into each period to find specific elements
        # .get_text() extracts just the text, stripping HTML tags
        name = period.find(class_="period-name").get_text(separator=" ")
        temp = period.find(class_="temp").get_text()
        desc = period.find(class_="short-desc").get_text(separator=" ")
        
        forecasts.append({
            "period": name,
            "temp": temp,
            "description": desc
        })
    
    return forecasts

# This lets us test the file directly
if __name__ == "__main__":
    forecasts = get_forecast()
    for f in forecasts:
        print(f)