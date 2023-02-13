# based on code from https://github.com/kevinwlu/iot/tree/master/lesson3
import psutil


def main():
    bat = psutil.sensors_battery()
    print(bat)


if __name__ == "__main__":
    main()
