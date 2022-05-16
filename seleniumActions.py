import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

DRIVER_PATH = "../../Coding/Chrome Driver/chromedriver.exe"
GOOGLE_FORM_LINK = "https://forms.gle/5u4d9YQUidPR3f1R8"
SPREADSHEET_CREATION_LINK = "https://docs.google.com/forms/d/" \
                            "1DFF1MCo3yENFtQq-Vhb0evtaVJSPob4clyUOiZ_I7ag/edit?usp=sharing"


class SeleniumActions:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        s = Service(DRIVER_PATH)
        self.driver = webdriver.Chrome(service=s, options=options)
        self.driver.implicitly_wait(120)
        self.driver.get(GOOGLE_FORM_LINK)

    def fill_in_forms(self, address, price, link):
        time.sleep(3)

        address_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/'
                                                           'div/div/div[2]/div/div[1]/div/div[1]/input')
        address_input.send_keys(address)

        price_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]'
                                                         '/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_input.send_keys(price)

        link_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/'
                                                        'div/div[2]/div/div[1]/div/div[1]/input')
        link_input.send_keys(link)

        submit_button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/'
                                                           'div[1]/div[1]/div/span')
        submit_button.click()

        send_another_answer_btn = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
        send_another_answer_btn.click()

    def open_spreadsheet(self):
        self.driver.get(SPREADSHEET_CREATION_LINK)
        time.sleep(3)

        answers_button = self.driver.find_element(By.XPATH, '//*[@id="tJHJj"]/div[3]/div[1]/div/div[2]/span/div')
        answers_button.click()

        google_sheets = self.driver.find_element(By.XPATH, '//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/'
                                                           'div[1]/div/div/span')
        google_sheets.click()
