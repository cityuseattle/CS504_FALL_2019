import time
import datetime

def schedule():
    
    newyear = datetime.datetime(2020, 1, 1, 0, 0, 0)
    while datetime.datetime.now() < newyear:
        try:
            print(datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"), end='\r')
            time.sleep(1)
        except KeyboardInterrupt:
            break
    else:
        print("####### HAPPY NEW YEAR #######")

if __name__ == "__main__":
  schedule()