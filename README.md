# Scrap.TF Raffle Bot
### NOTE: This tool was created for educational purposes and is not intended for personal use which may harm the health of the Scrap.TF raffle system. Use may result in a permanent ban of your Steam account from the Scrap.TF service.
---
Automation tool that enters item raffles on Scrap.TF, a bot trading site for Valve's Team Fortress 2.

## Installation & Usage
This project requires Python 3 and Selenium's Python library implementation which can be found on the [PyPI](https://pypi.org/project/selenium/). It can be installed using pip using `pip3 install selenium`. More conveniently, the library may also be included in your distributions repository, such as on Debian based systems, it can be installed using, `apt install python3-selenium`.

Additionally, a web driver is also required. This project was tested using Mozilla's [geckodriver](https://github.com/mozilla/geckodriver/releases), but can conceivably function using ChromeDriver as well.

By default, the script will look for geckdriver in the same directory as where the script is being run.
```
python3 main.py
```
or
```
python3 main.py path/to/webdriver   # if web driver is stored elsewhere
```

Finally, once running, you will be prompted to login through Steam on your own. Once completed, and returned to the main raffle page, press enter to begin entering raffles.

Developed and tested using:
* Debian 11
* geckodriver 0.30.0
* Python 3.9.2
* Selenium 4.0.0

## Planned Features
* Save cookies to retain persistent login
* Option to run for long periods of time with new raffle detection
* Detect raffles that have been won, skip them and inform user
