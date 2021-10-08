#!/usr/bin/env python3

'''
main.py
Tommy Janna
Oct. 7, 2021
'''

import sys
import time
import random

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Time parameters
wait_page_load = 10
wait_between_raffles_min = 2.5
wait_between_raffles_max = 7.5

def random_sleep(time_min: float, time_max: float):
    '''
    Sleep for a random amount of time within an interval

    Parameters:
        time_min (float): Lower time interval bound
        time_max (float): Upper time interval bound
    '''

    time_to_sleep = random.uniform(time_min, time_max)
    time.sleep(time_to_sleep)


# User defined path to web driver
driver_path = './geckodriver'
if len(sys.argv) > 1:
    driver_path = sys.argv[1]

serv = Service(driver_path)
driver = webdriver.Firefox(service=serv)
driver.get('https://scrap.tf/raffles')

print('Please sign in through Steam, then press enter to begin...')
input()

# Make sure user is logged in
if not driver.find_elements_by_xpath('//li[@class="dropdown nav-userinfo"]'):
    print('Steam login not detected!', file=sys.stderr)
    sys.exit(1)

# Scroll to the bottom of page until all raffles have loaded
while not driver.find_elements_by_xpath('//*[contains(text(), "That\'s all, no more!")]')[0].is_displayed():
    print('Loading more raffles...')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight - 200)')
    random_sleep(0.5, 1.5)

# Get the non-entered raffles
# Entered raffle:      <... class="panel-raffle raffle-entered" ...>
# Non-entered raffle:  <... class="panel-raffle " ...>
anchor_list = driver.find_elements_by_xpath('//div[@class="panel-raffle "]/div/div/a')

# Get URL for each raffle element
raffles = [anchor.get_attribute('href') for anchor in anchor_list]

print('\nFound', len(raffles), 'unentered raffles!')

# Loop through all raffle URLs
for raffle in raffles:
    driver.get(raffle)

    # Attempt to find and click raffle entry button
    try:
        WebDriverWait(driver, wait_page_load).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "enter-raffle-btns")][1]'))).click()
    except TimeoutException:
        print('Raffle entry button could not be found...', file=sys.stderr)
        # Skip sleep step because program has already waited 10 seconds.
        continue
    except Exception as exception:
        print('Unexpected exception...', str(exception), file=sys.stderr)
    else:
        print('.', end='', flush=True)

    random_sleep(wait_between_raffles_min, wait_between_raffles_max)

print('\nExecution completed')
