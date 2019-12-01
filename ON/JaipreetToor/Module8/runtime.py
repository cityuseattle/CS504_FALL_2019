import time

def fac(num):
    # this function does this, fac(5) -> 1 * 2 * 3 * 4 * 5... num
    product = 1
    for i in range(1, num+1):
        product = product * i
    return product

if __name__ == "__main__":
    print('Waiting for 3 seconds before calculating...')
    time.sleep(3)
    # capture time and store it in start_time
    start_time = time.time()
    prod = fac(100000)
    # capture another time and store it in end_time
    end_time = time.time()
    print('It took {} seconds to calculate.'.format(round(end_time-start_time, 5)))
  