from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://scrap.tf/raffles")

print("Please sign in through Steam, then press enter to begin...")
input()

anchorList = driver.find_elements_by_xpath("//div[@class='raffle-name']/a")

raffles = []
for anchor in anchorList:
    raffles.append(anchor.get_attribute("href"))

print("Got first page of raffle URLs!")
print(raffles)
