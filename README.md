# COVID-19 Data Retrieval System

This Python project interacts with the COVID-19 API to fetch and display global and country-specific COVID-19 statistics. The program is menu-driven and allows users to retrieve data in real-time.

## Features

1. **Global Statistics**:
   - Fetches and displays global COVID-19 statistics, including total cases, deaths, and recoveries.

2. **Country-Specific Statistics**:
   - Retrieves and displays data for a specific country.

3. **Historical Data by Date**:
   - Fetches COVID-19 data for a specific country on a specified date, including cases, deaths, and recoveries.

4. **User-Friendly Menu**:
   - Provides an interactive menu system for easy navigation.

---

## Prerequisites

- Python 3.6 or higher
- `requests` library

To install the required library, run:
```bash
pip install requests
```

---

## How to Use

1. Clone the repository or download the script.
2. Run the script using:
   ```bash
   python covid.py
   ```
3. Use the menu options to interact with the program:
   - Option 1: Display global statistics.
   - Option 2: Retrieve statistics for a specific country.
   - Option 3: Fetch historical data by date for a country.
   - Option 4: Exit the program.

---

## Code Explanation

### `Covid19API` Class
Handles interactions with the COVID-19 API.

- **`__init__`**: Initializes the base URL of the API.
- **`get_global_data`**: Fetches global COVID-19 statistics.
- **`get_country_data`**: Retrieves statistics for a specific country.
- **`get_data_by_date`**: Fetches historical data for a specific country and date.

### `Covid19Menu` Class
Provides a menu-driven interface for the user.

- **`__init__`**: Initializes the `Covid19API` class.
- **`display_global_stats`**: Displays global COVID-19 statistics.
- **`display_country_stats`**: Shows data for a specific country.
- **`display_data_by_date`**: Displays data for a specific date and country.
- **`main_menu`**: Implements the interactive menu system.

### Main Function
Runs the program by instantiating `Covid19Menu` and invoking the menu.

---

## Example

### Sample Interaction
```
COVID-19 Patient Record System
1. Display Global COVID-19 Statistics
2. Display COVID-19 Statistics for a Country
3. Display COVID-19 Data by Date for a Country
4. Exit
Choose an option (1-4): 1

Global COVID-19 Statistics:
Total Cases: 123456789
Total Deaths: 987654
Total Recovered: 567890
```

---

## Error Handling

- **API Connectivity Issues**: Displays an error message if the API request fails.
- **Invalid Country or Date**: Notifies the user if the entered country or date is incorrect or data is unavailable.

---

## API Reference

This project uses the [COVID-19 API](https://disease.sh/) for fetching data. Ensure you have a stable internet connection for the script to work.

---


## Author

Developed by [Sinare Darshan And Team].

