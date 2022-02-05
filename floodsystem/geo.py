# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from os import name
from .utils import sorted_by_key  # noqa
from haversine import haversine
from . import datafetcher
from .station import MonitoringStation
from floodsystem.stationdata import build_station_list

def stations_by_distance(stations, p):
    stations = build_station_list()
    names = []
    distance = []
    for station in stations:
        names.append(station.name)
        distance.append(haversine(p, station.coord))
    tuples = list(zip(names, distance))
    tuples = sorted_by_key(tuples,1)
    return tuples

def stations_within_radius(stations, centre, r):
    stations = build_station_list()
    names = []
    for station in stations:
        if haversine(centre, station.coord) <= r:
            names.append(station.name)
        else:
            pass
    return names


def rivers_by_station_number(stations, N):
    stations = build_station_list()
    names= []

# list of station objects that returns a set with names of the rivers with a monitoring station 
def rivers_with_station(stations):
    stationRivers= set()
    for station in stations:
        stationRivers.add(station.river)
    stationRivers = sorted(stationRivers)
    return stationRivers

# using a dictionary mapping river names to a list of station objects on a given river  
def stations_by_river(stations):
    stationRivers = set(rivers_with_station(stations)) 
    riversStations = {} #empty dictionary 
    for stations in stations:
        if not station.river in riversStations: 
            riversStations.update({station.river: list})