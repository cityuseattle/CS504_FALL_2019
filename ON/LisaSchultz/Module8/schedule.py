import time
import datetime


def schedule():
    #datetime formats -> datetime(year, month, day, hour, minute, second)
    newyear = datetime.datetime(2020, 1, 1, 0, 0, 0)
    while datetime.datetime.now() < newyear:
        try:
            #this will keep printing time counding down with yyyy-mm-dd hh:ss format
            # '\r' means return to beginning of the the line
            print(datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"), end='\r')
            time.sleep(1)
        except KeyboardInterrupt:
            break
    else:
        print("###### HAPPY NEW YEAR #####")


if __name__ == "__main__":
    schedule()