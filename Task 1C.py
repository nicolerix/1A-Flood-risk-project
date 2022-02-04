from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 10

    list = stations_within_radius(stations, centre, r)
    print(sorted(list))
if __name__ == "__main__":
    print("***Task 1C: CUED Part 1A Flood Warning System***")
    run()