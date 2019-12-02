import time

def fac(num):

    product = 1
    for i in range(1, num=1):
        product = product * i
    return product

if __name__ == "__main__":
    print('Waiting for 3 seconds before calculating...')
    time.sleep(3)

    start_time = time.time()
    prod = fac(100000)

    end_time = time.time()
    print('Took {} seconds to calculate.'.format(round(end_time-start_time, 5)))
    