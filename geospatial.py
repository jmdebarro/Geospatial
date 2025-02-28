import requests


class Geospatial:
    """Class responsible for collecting API data"""

    station_map = {9410660: "LA", 9415020: "SF", 9414863: "SF", 9410840: "LA"}

    def __init__(self):
        self.interval = "h"
        self.units = "english"
        self.format = "json"
        self.timezone = "lst"
        self.date = "today"
        self.endpoint = "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter"

    # Cannot do all stations and readings in all methods as stations vary with capabilities

    # Method collects water level data from hardcoded stations
    def waterLevels(self):
        readings = []
        water_stations= [9415020, 9410660]
        product = "water_level"
        datum = "MLLW"

        # Iterates through stations and preferred reading
        for station in water_stations:
            queries = (
                f"?date={self.date}&station={station}&product={product}"
                f"&interval={self.interval}&units={self.units}&format={self.format}"
                f"&time_zone={self.timezone}&datum={datum}"
                )
            endpoint = self.endpoint + queries

            try:
                response = requests.get(endpoint)
                data = response.json()
                readings.append(data)

            except requests.exceptions.RequestException as e:
                print(f"Failed request for station: {station} {product} reading")
                print(f"Error: {e}")


    # Method collects water level data from hardcoded stations
    def airWaterTemps(self):
        readings = []
        temp_stations= [9414863, 9410840]
        products = ["air_temperature", "water_temperatur"]

        # Iterates through stations and preferred reading
        for station in temp_stations:
            for product in products:
                queries = (
                    f"?date={self.date}&station={station}&product={product}"
                    f"&interval={self.interval}&units={self.units}&format={self.format}"
                    f"&time_zone={self.timezone}"
                )
                endpoint = self.endpoint + queries

                print(endpoint)
                try:
                    response = requests.get(endpoint)
                    data = response.json()
                    readings.append(data)

                except requests.exceptions.RequestException as e:
                    print(f"Failed request for station: {station} {product} reading")
                    print(f"Error: {e}")