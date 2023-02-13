# based on code from https://github.com/kevinwlu/iot/tree/master/lesson3
import sys
from datetime import date

import pytz
from astral import LocationInfo
from astral.geocoder import database, lookup
from astral.sun import sun


def main():
    city_name = sys.argv[1]
    city = lookup(city_name, database())

    assert isinstance(city, LocationInfo)
    print(f"Information for {city.name}/{city.region}\n")

    timezone = city.timezone
    print(f"Timezone: {timezone}")
    print(f"Latitude: {city.latitude:.02f}; Longitude: {city.longitude:.02f}\n")

    s = sun(city.observer, date=date.today(), tzinfo=pytz.timezone(timezone))
    print(f"Dawn:    {s['dawn']}")
    print(f"Sunrise: {s['sunrise']}")
    print(f"Noon:    {s['noon']}")
    print(f"Sunset:  {s['sunset']}")
    print(f"Dusk:    {s['dusk']}")


if __name__ == "__main__":
    main()
