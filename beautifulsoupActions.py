from bs4 import BeautifulSoup
import requests
import json

URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2" \
      "C%22mapBounds%22%3A%7B%22west%22%3A-122.74884261083984%2C%22east%22%3A-122.11781538916016%2C%2" \
      "2south%22%3A37.55733345439207%2C%22north%22%3A37.99260877508996%7D%2C%22mapZoom%22%3A11%2C%22i" \
      "sMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22bed" \
      "s%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%" \
      "3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22" \
      "fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%2" \
      "2value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%" \
      "7D"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                  " AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/97.0.4692.99 Safari/537.36",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
}


class BeautifulSoupActions:
    """Live Urls, Addresses and Prices data to use:
     .urls_list - for urls, .prices_list - for prices, .addresses_list - for addresses."""

    def __init__(self):
        response = requests.get(url=URL, headers=HEADERS)
        self.soup = BeautifulSoup(response.text, "html.parser")

        self.urls_list = []
        self.prices_list = []
        self.addresses_list = []

        self.data_scraping()

    def data_scraping(self):
        data_dictionary = json.loads(self.soup.select_one("script[data-zrr-shared-data-key]").getText().strip("-<>!"))

        for data_piece in data_dictionary["cat1"]["searchResults"]["listResults"]:
            if "https://www.zillow.com" not in data_piece["detailUrl"]:
                self.urls_list.append("https://www.zillow.com" + data_piece["detailUrl"])
            else:
                self.urls_list.append(data_piece["detailUrl"])

        for data_piece in data_dictionary["cat1"]["searchResults"]["listResults"]:
            try:
                self.prices_list.append(data_piece["price"].split("/mo")[0])
            except KeyError:
                self.prices_list.append(data_piece["units"][0]["price"])

        for data_piece in data_dictionary["cat1"]["searchResults"]["listResults"]:
            self.addresses_list.append(data_piece["addressStreet"] + ", " + data_piece["addressCity"])
