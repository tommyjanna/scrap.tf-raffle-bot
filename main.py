#!/usr/bin/env python3

'''
main.py
Tommy Janna
Oct. 7, 2021
'''

import sys
import time
import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium import webdriver

waitPageLoad = 10
waitBetweenRafflesMin = 2.5
waitBetweenRafflesMax = 7.5

def rSleep(minTime: float, maxTime: float):
    '''
    Sleep for a random amount of time within an interval

    Parameters:
        minTime (float): Lower time interval bound
        maxTime (float): Upper time interval bound
    '''

    timeToSleep = random.uniform(minTime, maxTime)
    time.sleep(timeToSleep)


if __name__ == '__main__':
    # User defined path to web driver
    driver_path = './geckodriver'
    if len(sys.argv) > 1:
        driver_path = sys.argv[1]

    driver = webdriver.Firefox(executable_path=driver_path)
    driver.get('https://scrap.tf/raffles')

    print('Please sign in through Steam, then press enter to begin...')
    input()

    # Make sure user is logged in
    if not driver.find_elements_by_xpath('//li[@class="dropdown nav-userinfo"]'):
        print('Steam login not detected!', file=sys.stderr)
        exit(1)

    # Scroll to the bottom of page until all raffles have loaded
    while not driver.find_elements_by_xpath('//*[contains(text(), "That\'s all, no more!")]'):
        print('Loading more raffles...')
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight - 200)')
        rSleep(0.5, 1.5)

    # Get the non-entered raffles
    # Entered raffle:      <... class="panel-raffle raffle-entered" ...>
    # Non-entered raffle:  <... class="panel-raffle " ...>
    anchorList = driver.find_elements_by_xpath('//div[@class="panel-raffle "]/div/div/a')

    # Get URL for each raffle element
    raffles = [anchor.get_attribute('href') for anchor in anchorList]

    print('Found', len(raffles), 'unentered raffles!') 

    # Loop through all raffle URLs
    for raffle in raffles:
        driver.get(raffle)

        # Attempt to find and click raffle entry button
        try:
            WebDriverWait(driver, waitPageLoad).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "enter-raffle-btns")][1]'))).click()
        except TimeoutException as exception:
            print('Raffle entry button could not be found...' + str(exception), file=sys.stderr)
        except Exception:
            print('Unexpected exception...')

        rSleep(waitBetweenRafflesMin, waitBetweenRafflesMax)

    print('Execution completed')
