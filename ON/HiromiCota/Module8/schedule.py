import time
import datetime


def schedule():
    # datetime format -> datetime(year,month,day,hour,minute,second)
    newyear = datetime.datetime(2020, 1, 1, 0, 0, 0,)
    while datetime.datetime.now() < newyear:
        try:
            #this will spew text every second until stopped or the clock reads after New Year's Eve 2020
            print(datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"), end='\r')
            time.sleep(1)
            # I still don't think sleeping the thread is a great idea, but OK
        except KeyboardInterrupt:
            break
    else:
        print("###### HAPPY NEW YEAR ########")

if __name__ == "__main__":
    schedule()