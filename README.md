# CODE THE DREAM - Weather Scraping Capstone

## Project Overview

This project uses Python and Selenium to collect weather forecast data from the National Weather Service (NWS) for four major U.S. cities representing different time zones.

The collected data is saved to a CSV file, loaded into a Pandas DataFrame, and checked for missing values and duplicate records. The dataset is also enhanced with time-zone information before being saved as a cleaned CSV file.

## Data Source

Weather data is collected from the National Weather Service:

https://forecast.weather.gov/

I chose four major U.S. cities representing different time zones so I could collect and compare forecasts from different regions of the country.

The scraper retrieves the detailed forecast for these four cities:
- New York, New York — Eastern Time
- Chicago, Illinois — Central Time
- Denver, Colorado — Mountain Time
- Los Angeles, California — Pacific Time

Why I Chose This Website:
I initially considered using the Weather Around The World website suggested in the assignment. 
However, the scraping permissions were not clear.

I decided to use the National Weather Service for the following reasons:
1. NWS forecast pages provided a more accessible source for collecting weather information.
3. Documentation explicitly says the data is open and free to use for any purpose, subject to reasonable rate limits. It requires an identifying User-Agent header.
3. NWS provides consistent forecast information across its city forecast pages.

## Data Collected

The scraper extracts the following information:

- **City:** The city associated with the forecast.
- **Forecast Period:** The forecast time period, such as Today or Tonight.
- **Forecast Description:** The weather conditions and forecast details.

The time-zone column is added during data transformation.

## Technologies Used

- Python
- Selenium
- WebDriver Manager
- Pandas
- CSV

The script retrieves the forecasts, saves the original data to `weather_data.csv`, loads the data into Pandas, performs data quality checks, adds time-zone information, and saves the transformed dataset to `weather_data_cleaned.csv`.

## Output Files

- **weather_data.csv:** Original scraped forecast data.
- **weather_data_cleaned.csv:** Transformed dataset with an additional time-zone column.

## Data Cleaning and Transformation

The project uses Pandas to:

- Remove leading and trailing whitespace from city names.
- Check for missing values.
- Check for duplicate records.
- Add time-zone information based on the city.

The original CSV is preserved separately from the transformed dataset.