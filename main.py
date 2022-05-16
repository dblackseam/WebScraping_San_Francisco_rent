from seleniumActions import SeleniumActions
from beautifulsoupActions import BeautifulSoupActions
import time


bs_part = BeautifulSoupActions()
offers_list = tuple(zip(bs_part.addresses_list, bs_part.prices_list, bs_part.urls_list))

selenium_part = SeleniumActions()
time.sleep(2)

for tuple in offers_list:
    selenium_part.fill_in_forms(tuple[0], tuple[1], tuple[2])

selenium_part.open_spreadsheet()
time.sleep(60)
