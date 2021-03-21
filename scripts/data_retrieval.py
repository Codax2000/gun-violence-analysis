'''
Alex Knowlton
3/21/2021

This file retrieves data and returns it in DataFrame or GeoDataFrame form,
as necessary
'''

import pandas as pd
import geopandas as gpd


def get_gun_data():
    '''
    Returns the gun violence dataset as a GeoDataFrame, with appropriate
    columns and geometry equal to the location of the incident. Other
    columns included are the latitude and longitude, included for later
    plotting, the number of people killed, # people injured
    '''
    pass


def get_population():
    '''
    Returns the population dataset from 2015 as a DataFrame, restricted to
    only the state and population
    '''
    pass


def get_retailers():
    '''
    returns the retailers dataset as a DataFrame
    '''
    pass


def get_us_map():
    '''
    returns a GeoDataFrame of the US, restricted to geometry, state name,
    county id
    '''
    pass


def get_income():
    '''
    returns the income dataset as a DataFrame, with only state and income
    included as columns
    '''
    pass