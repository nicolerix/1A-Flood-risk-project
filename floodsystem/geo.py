# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine
from . import datafetcher
from .station import MonitoringStation
from floodsystem.stationdata import build_station_list


distance = haversine(p, station.coord)

def stations_by_distance(stations, p):
    stations = build_station_list()
    for station in stations:
        names.append()
        #coords = MonitoringStation.coord
        distance.append()
    turples = list(zip(names, distance))
    turples = sorted_by_key(turples, 1)
    return turples
