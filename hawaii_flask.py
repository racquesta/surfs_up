from flask import Flask, jsonify

import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database Set up
engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect = True)

#save tables as variables
Measurements = Base.classes.measurements
Stations = Base.classes.stations

session = Session(engine)

##### Set up Flask
app = Flask(__name__)

@app.route("/")
def home():
    return ("Hawaii Weather Data API<br/>"
    "/api/v1.0/precipitation<br/>"
    "/api/v1.0/stations<br/>"
    "/api/v1.0/tobs<br/>"
    "/api/v1.0/startdate/<br/>"
    "/api/v1.0/startdate/enddate/")



if __name__ == '__main__':
    app.run(debug=True)




