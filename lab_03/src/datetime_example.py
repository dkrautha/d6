# based on code from https://github.com/kevinwlu/iot/tree/master/lesson3
import datetime
import time


def main():
    print(datetime.datetime.today())
    print(datetime.datetime.now())
    print(datetime.datetime.utcnow())
    print(time.time())
    print(time.asctime(time.localtime(time.time())))
    print(datetime.datetime.fromtimestamp(time.time()))
    print(datetime.datetime.utcfromtimestamp(time.time()))


if __name__ == "__main__":
    main()
