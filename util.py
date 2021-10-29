'''
util.py
Tommy Janna
Oct. 28, 2021
'''

import random
import time
import os.path

def random_sleep(time_min: float, time_max: float) -> None:
    '''
    Sleep for a random amount of time within an interval

    Parameters:
        time_min (float): Lower time interval bound
        time_max (float): Upper time interval bound
    '''

    time_to_sleep = random.uniform(time_min, time_max)
    time.sleep(time_to_sleep)


def cookie_read(filename: str) -> dict:
    cookie = {}

    if os.path.exists(filename):
        cookie_file = open(filename, 'r')

        cookie['name'] = 'scr_session'
        cookie['value'] = cookie_file.readline()
        cookie['path'] = '/'
        cookie['domain'] = '.scrap.tf'
        cookie['secure'] = True
        cookie['httpOnly'] = True
        cookie['expiry'] = int(cookie_file.readline())

    return cookie


def cookie_write(filename: str, cookie: dict) -> None:
    cookie_file = open(filename, 'w')

    if cookie['value'] and cookie['expiry']:
        cookie_file.write(cookie['value'])
        cookie_file.write('\n')
        cookie_file.write(str(cookie['expiry']))
