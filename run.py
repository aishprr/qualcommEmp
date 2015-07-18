#!flask/bin/python
from app import app
from flask_googlemaps import GoogleMaps
GoogleMaps(app)
app.run(debug=True,port = 8000)
