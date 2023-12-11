# Import the dependencies.
import numpy as np
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with = engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )

# Create the precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    most_recent = dt.date(2017,8,23)
    year_ago = most_recent - dt.timedelta(days=365)
    query = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= year_ago).all()
    session.close()
    prcp_list = {date:prcp for date, prcp in query}
    return jsonify(prcp_list)

# Create the station route
@app.route("/api/v1.0/stations")
def stations():
    query2 = session.query(Station.station).all()
    session.close()
    stations = list(np.ravel(query2))
    return jsonify(stations = stations)

# Create the tobs route
@app.route("/api/v1.0/tobs")
def tobs():
    most_recent = dt.date(2017,8,23)
    year_ago = most_recent - dt.timedelta(days=365)
    query3 = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= year_ago).all()
    session.close()
    temperature = list(np.ravel(query3))
    return jsonify(temperature = temperature)

#Create the start route
@app.route("/api/v1.0/start")
def start():
    start_date = dt.date(2015,1,1)
    query4 = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs),
        func.avg(Measurement.tobs)).filter(Measurement.date >= start_date).all()
    session.close()
    starting_date = list(np.ravel(query4))
    return jsonify(starting = starting_date)

# Create the end route
@app.route("/api/v1.0/start/end")
def end():
    start_date = dt.date(2015,1,1)
    end_date = dt.date(2015,12,31)
    query5 = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs),
        func.avg(Measurement.tobs)).filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    session.close()
    start_end = list(np.ravel(query5))
    return jsonify(start_end = start_end)

# Run in debug mode
if __name__ == "__main__":
    app.run(debug=True)