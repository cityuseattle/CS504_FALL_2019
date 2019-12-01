import time
import datetime


def schedule():
    # datetime format -> datetime(year, month, day, hour, minute, second)
    newyear = datetime.datetime(2019, 11, 30, 12, 0, 0)
    while datetime.datetime.now() < newyear:
        try:
            # this will keep printing time, counting down with yyyy-mm-dd hh:mm:ss format
            # '\r' means return to the beginning of the line
            print(datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"), end='\r')
            time.sleep(1)
        except KeyboardInterrupt:
            break
    else:
        print("####### HAPPY NEW YEAR #######")


if __name__ == "__main__":
    schedule()