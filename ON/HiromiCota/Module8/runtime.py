import time


def fac(num):
    # returns factorial sums e.g. fac(3) == 1 + 2 + 3
    value = 1
    for i in range(1 , num):
        value = value * i
    return value

if __name__ == "__main__":
    print('Waiting for 3 seconds before calculating.')
    # why?
    time.sleep(3)
    # sleeping threads seems like a bad idea, but OK
    start_time = time.time()
    prod = fac(100000)
    end_time = time.time()
    print('Took {} seconds to calculate.'.format(round(end_time - start_time, 5)))