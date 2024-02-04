#!/usr/bin/python3
'''The blueprint for the AirBnB clone's API.'''
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
'''The blueprint for the AirBnB clone API.'''


from api.v1.views.cities import *
from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.places_amenities import *
