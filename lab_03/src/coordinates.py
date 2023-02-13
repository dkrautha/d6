# based on code from https://github.com/kevinwlu/iot/tree/master/lesson3
import sys

from geopy.geocoders import Nominatim
from geopy.location import Location


def main():
    geolocator = Nominatim(user_agent="iot-application")
    address = sys.argv[1]

    assert isinstance(location := geolocator.geocode(address), Location)

    print(location.address)
    print((location.latitude, location.longitude))


if __name__ == "__main__":
    main()
