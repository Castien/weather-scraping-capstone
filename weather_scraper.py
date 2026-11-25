
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import csv

cities = {
    "New York": (40.7128, -74.0060),
    "Chicago": (41.8781, -87.6298),
    "Denver": (39.7392, -104.9903),
    "Los Angeles": (34.0522, -118.2437)
}

weather_data = []

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# tested with one city
# driver.get("https://forecast.weather.gov/MapClick.php?lat=40.7128&lon=-74.0060")

for city, coordinates in cities.items():
    latitude, longitude = coordinates

    url = f"https://forecast.weather.gov/MapClick.php?lat={latitude}&lon={longitude}"

    driver.get(url)

    # print(f"\n{'=' * 40}")
    # print(city)
    # print(f"{'=' * 40}")

    forecast_periods = driver.find_elements(By.CSS_SELECTOR, "#detailed-forecast-body .row-forecast")

    for period in forecast_periods:
        forecast_name = period.find_element(By.CSS_SELECTOR, ".forecast-label").text
        forecast_description = period.find_element(By.CSS_SELECTOR, ".forecast-text").text

        weather_record = {"city": city, "forecast_period": forecast_name, "forecast_description": forecast_description}
        weather_data.append(weather_record)

        # print(forecast_name)
        # print(forecast_description)
        # print()

    #print(driver.title)

driver.quit()

#print(weather_data)

with open("weather_data.csv", "w", newline="") as csv_file:
    fieldnames = ["city", "forecast_period", "forecast_description"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(weather_data)
