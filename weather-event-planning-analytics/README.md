# D493 JGN1 Task 1: Weather Prediction Python Application
# Josie Mikita
### Student ID: 012153910

## Project Goal
This application was built to simulate a typical data analyst task: retrieving, processing, storing, and reporting on historical climate data for a specific event location. I used Python, an external Weather API, and SQLAlchemy to manage a local SQLite database.
The location featured in this application is Raymond, WA on Christmas day (December 25), but it can be customized to any location and desired data.

---

### Setup and Dependencies

#### 1. Requirements File (Required for Competence - E)
Before running the main program or tests, please ensure all dependencies are installed from the `requirements.txt` file.

**Command:**
```bash
pip install -r requirements.txt
```


#### 2. Technical Dependencies (Comprehensive Module List)
This project relies on the following modules:

* **External Packages (Installed via pip):** requests, SQLAlchemy
* **Standard Python Libraries (Built-in):** datetime, collections, statistics, sys, unittest

---

### Running the Application and Tests

#### 1. Program Command (C3, C5, C6)
The program runs automatically using hardcoded inputs for Raymond, WA. No user interaction is required.

Command to Run Program:

```bash
python main.py
```

### III. Output Description (C6)

### III. Final Event Planning Data Report (C6)

The formatted report printed to the console (required for the Screenshot C6 submission) is the **final analysis** delivered to the event planning team. It provides a quick, consolidated view of the most critical historical weather risks, directly retrieved from the database.

| Category | Variables Retrieved (C1 & C6 Fields) |
| :--- | :--- |
| **Inputs** | Location Coordinates, Event Date (12/25) |
| **Temperature** | 5-year Average, Minimum, and Maximum Temperature in Fahrenheit |
| **Wind Speed** | 5-year Average, Minimum, and Maximum Wind Speed (MPH) |
| **Precipitation** | 5-year Total Sum, Minimum Daily, and Maximum Daily Precipitation (Inches) |





