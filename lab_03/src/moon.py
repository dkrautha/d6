# based on code from https://github.com/kevinwlu/iot/tree/master/lesson3
from datetime import date, timedelta

from astral import moon


def main():
    now = date.today()
    for i in range(30):
        day = now + timedelta(days=i)
        moon_phase = moon.phase(day)
        print(f"{day.isoformat()} Moon Phase: {int(moon_phase)}")


if __name__ == "__main__":
    main()
