import time
from art import *


def checking_the_time(func):
    def wrapper():
        t = time.time()
        func()
        t = time.time() - t
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print(f'Вркемя: {t}')
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        tprint("i am gul".upper(), "larry3d ")
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    return wrapper()


@checking_the_time
def i_am_gul():
    n: int = 1000
    while n > 0:
        time.sleep(.3)
        print(f'{n} - 7 = {n - 7}')
        n -= 7


def main():
    i_am_gul()


if __name__ == '__main__':
    main()
