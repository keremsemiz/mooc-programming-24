# Write your solution here
import math
def get_station_data(filename: str):
    stationsdict = {}
    stations = []
    with open(filename) as newFile:
        for line in newFile:
            parts = line.split(';')
            if parts[0] == "Longitude":
                continue
            stations.append((parts[3].strip(), parts[0].strip(), parts[1].strip()))
    
    for station in stations:
        name, longitude, latitude = station
        stationsdict[name] = float(longitude), float(latitude)
        #print(stationsdict)
    
    return stationsdict

def distance(stations: dict, station1: str, station2: str):
    x_km = (stations[station1][0] - stations[station2][0]) * 55.26
    y_km = (stations[station1][1] - stations[station2][1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    
    return distance_km

def greatest_distance(stations: dict):
    max_distance = 0
    station_pair = ("", "", 0)
    station_names = list(stations.keys())
    for i in range(len(station_names)):
        for j in range(i + 1, len(station_names)):
            station1 = stations[i]
            station2 = stations[j]
            dist = distance(stations, station1, station2)
            if dist > max_distance:
                max_distance = dist
                stationpair = (station1, station2, max_distance)

    return stationpair

if __name__ == "__main__":
    print(get_station_data("stations1.csv"))