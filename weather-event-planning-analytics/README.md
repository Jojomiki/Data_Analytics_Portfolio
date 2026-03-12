# Weather Event Planning Analytics Tool

## Overview
This project analyzes historical weather patterns to support planning decisions for outdoor events.
The application retrieves historical weather data from the Open-Meteo API, aggregates five years of observations for a specific event date, and stores the results in a SQLite database for reporting and analysis.
The system demonstrates a complete analytics workflow, including:
- Data extraction from an external API
- Statistical aggregation of weather metrics
- Database storage using SQLAlchemy ORM
- Reporting through structured queries


## Business Problem
Outdoor event planners must anticipate weather risks when planning infrastructure such as tents, heating, cooling systems, and safety equipment.
However, historical weather insights are often difficult to access quickly.
This tool provides a lightweight analytics workflow that retrieves historical weather data and summarizes expected conditions for a given event date.
Example planning questions include:
- What temperatures are typical for this date?
- What is the historical precipitation risk?
- What wind conditions might affect outdoor equipment?

## Data Source
Weather data is retrieved from the **Open-Meteo Archive API**.

Data collected includes:
- Temperature (mean, min, max)
- Wind speed
- Precipitation totals
The program collects data for the same event date over the **past five years**.

## Methodology
The system implements a simplified **ETL pipeline**:

### Extract
Historical weather data is retrieved via HTTP requests to the Open-Meteo API.

### Transform
Daily weather values are aggregated into summary statistics, including averages, minimums, maximums, and totals.

### Load
Aggregated results are stored in a SQLite database using SQLAlchemy ORM models.

### Analyze
The database is queried to generate a formatted event planning report.


## Example Analysis
For the event date **December 25 (Christmas)** in **Raymond, Washington**, the system calculates:
- Five-year average temperature
- Minimum and maximum temperature
- Wind speed trends
- Total precipitation across five years  
These metrics help planners anticipate infrastructure needs such as heating, shelter, and weather protection.

## Technologies Used
- Python
- SQLAlchemy
- SQLite
- Requests
- REST APIs
- Unit Testing (unittest)

## How to Run the Project

Clone the repository:

```
git clone https://github.com/Jojomiki/Data_Analytics_Portfolio.git
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the program:

```
python main.py
```

The program will retrieve historical weather data, calculate aggregated metrics, store them in a SQLite database, and generate a report for event planning analysis.
