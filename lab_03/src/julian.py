# based on code from https://github.com/kevinwlu/iot/tree/master/lesson3
from datetime import date

from jdcal import gcal2jd


def main():
    now = date.today()
    jd = gcal2jd(now.year, now.month, now.day)

    print(f"Calendar Date: {now.isoformat():s}")
    print(f"Julian Date: {jd[0] + jd[1]:0.1f}")
    print(f"Modified Julian Date: {jd[1]:0.1f}")


if __name__ == "__main__":
    main()
