# sqlalchemy-challenge
## SQL Alchemy Module 10 Challenge
This script contains code for a Jupyter notebook that analyzes data from a csv file and a python file that creates an app with jsonified data from the file.

### Precipitation Analysis
This code first uses SQLAlchemy to connect to a sqlite database. It then creates a base to reflect the tables from the file into classes called "measurement" and "stations" for the respective files. It then creates a session to link to the database. 
To start the analysis, the code first creates a query to find the latest date in the "measurement" data. It then creates another query using that date to find the date a year prior to the last date. Using both these dates, a third query is created to retrieve the date and precipitation scores for each date in between those two dates. Using that data, creates a DataFrame titled "prcp_df" and then creates a plot from the DataFrame using Pandas.

### Station Analysis
First creates a query to count the total number of different staitions from the "measurement" file. Then creates another query to find the most active station, which is the station listed the most times in the dataset. The query prints each station id along with its number of rows in the dataset in descending order from most active to least active. Then, taking the most active station id from the previous query, creates a third query to find the highest, lowest, and average recorded temperature for the most active station using min max, and average functions and filtering by the most active station id. The final query then obtaains the temperature for the most active query for the past year. Lastly, a DataFrame is created from the last query, and a histogram is created from the DataFrame, showing the temperature data for the last year in the dataset.

### Climate App
