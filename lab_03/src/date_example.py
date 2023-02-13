# based on code from https://github.com/kevinwlu/iot/tree/master/lesson3
from datetime import date


def main():
    now = date.today()

    print(f"Date: {now.isoformat()}")
    print(f"Date: {now.strftime('%m-%d-%y')}")
    print(f"Day of Week: {now.strftime('%A')}")
    print(f"Month: {now.strftime('%B')}")
    print(f"Year: {now.strftime('%Y')}")

    first = date(2023, 1, 18)
    last = date(2023, 5, 4)

    timediff = now - first
    print(f"{timediff.days:d} days after the first day of classes")

    timediff = last - now
    print(f"{timediff.days:d} days before the last day of classes")


if __name__ == "__main__":
    main()
