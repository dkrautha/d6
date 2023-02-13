# based on code from https://github.com/kevinwlu/iot/tree/master/lesson3
import time


def main():
    while True:
        try:
            nowtime = time.time()
            print(time.asctime(time.localtime(nowtime)))
            time.sleep(10)
        except KeyboardInterrupt:
            exit()


if __name__ == "__main__":
    main()
