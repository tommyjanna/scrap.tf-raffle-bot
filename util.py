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
    Sleep for a random amount of time within an interval.

    Parameters:
        time_min (float): Lower time interval bound
        time_max (float): Upper time interval bound
    '''

    time_to_sleep = random.uniform(time_min, time_max)
    time.sleep(time_to_sleep)


def cookie_read(filename: str) -> dict:
    '''
    Reads a dictionary representation of a browser cookie. If the file does
    not exist, the function will return None.

    Parameters:
        filename (str): Path to the cookie file
    
    Returns:
        dict: Cookie that can be loaded using Selenium's add_cookie()
    ''' 

    if not os.path.exists(filename):
        return None

    cookie_file = open(filename, 'r')
    cookie_data = eval(cookie_file.read())

    if not type(cookie_data) is dict:
        raise Exception('Cookie file ' + filename + ' could not be evaluated \
                        to a dictionary')
        return None

    return cookie_data
    

def cookie_write(filename: str, cookie: dict) -> None:
    '''
    Writes a dictionary representation of a cookie to a file. If the file does
    not exist, it will be created. If a file already exists, it will be
    overwritten.

    Parameters:
        filename (str): Path to the cookie file
        cookie (dict): Cookie data
    '''

    cookie_file = open(filename, 'w')
    cookie_file.write(str(cookie))
    cookie_file.close()
