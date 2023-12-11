# sqlalchemy-challenge
## SQL Alchemy Module 10 Challenge
This script contains code for a Jupyter notebook that analyzes data from a csv file and a python file that creates an app with jsonified data from the file.

### Precipitation Analysis
This code first uses SQLAlchemy to connect to a sqlite database. It then creates a base to reflect the tables from the file into classes called "measurement" and "stations" for the respective files. It then creates a session to link to the database. 
To start the analysis, the code first creates a query to find the latest date in the "measurement" data. It then creates another query using that date to find the date a year prior to the last date. Using both these dates, a third query is created to retrieve the date and precipitation scores for each date in between those two dates. Using that data, creates a DataFrame titled "prcp_df" and then creates a plot from the DataFrame using Pandas.

### Station Analysis
First creates a query to count the total number of different staitions from the "measurement" file. Then creates another query to find the most active station, which is the station listed the most times in the dataset. The query prints each station id along with its number of rows in the dataset in descending order from most active to least active. Then, taking the most active station id from the previous query, creates a third query to find the highest, lowest, and average recorded temperature for the most active station using min max, and average functions and filtering by the most active station id. The final query then obtaains the temperature for the most active query for the past year. Lastly, a DataFrame is created from the last query, and a histogram is created from the DataFrame, showing the temperature data for the last year in the dataset.

### Climate App
This python script designs a Flask API based on the queries just developed in the analyses. Starts at the homepage and there lists all the available routes:
/api/v1.0/precipitation (precipitation), /api/v1.0/stations (station), /api/v1.0/tobs(tobs), /api/v1.0/start(start) and /api/v1.0/start/end(start/end).
The precipitation route converts the query results from the precipitation analysis (the last 12 months of data) to a dictionary using date as the key and prcp as the value, then returns the JSON representation of the dictionary.
The station route returns a JSON list of stations from the dataset.
The tobs route queries the dates and temperature observations of the most-active station for the previous year of data, then returns a JSON list of temperature observations for the previous year.
The start route returns a JSON list of the minimum temperature, the average temperature, and the maximum temperature up to specified start date (1/1/2015). The start/end route lists the same information from the start date to a specified end date (12/31/2015).
The last part of the code tells it to run the Flask app in debug mode.
