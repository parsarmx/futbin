import csv
import time
from selenium import webdriver

from urllib.parse import urljoin
from selenium.webdriver.common.by import By
from config import PLAYER_ROUTE, BASE_URL, PLAYER_VERSION, chrome_options
from functions import RequestHandler, update_prices


def get_price(player_name):
    driver = webdriver.Chrome(options=chrome_options)
    request = RequestHandler(path, {"version": PLAYER_VERSION, "search": player_name})
    driver.get(request.get_player_static_url())
    xpath = '//*[@id="repTb"]/tbody/tr[1]/td[6]/span'
    price = driver.find_element(By.XPATH, xpath)
    price = price.text.split("K")[0]
    driver.close()
    print(price)
    return price


if __name__ == "__main__":
    while True:
        start = time.time()
        path = urljoin(BASE_URL, PLAYER_ROUTE)
        players = []
        with open("client/log.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                player = []
                price = get_price(row[0])

                player.append(row[0])
                player.append(float(price) * 1000)
                player.append((float(price) * 1000) * 1.6)
                players.append(player)

        update_prices(players)
        end = time.time()
        print(end - start)
        time.sleep(300 - (end - start))
