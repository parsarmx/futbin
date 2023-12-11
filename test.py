import csv
import time
from selenium import webdriver
import asyncio
from urllib.parse import urljoin
from selenium.webdriver.common.by import By
from config import PLAYER_ROUTE, BASE_URL, PLAYER_VERSION, chrome_options
from functions import RequestHandler

players = []


def get_price(player_name, path):
    driver = webdriver.Chrome(options=chrome_options)
    request = RequestHandler(path, {"version": PLAYER_VERSION, "search": player_name})
    driver.get(request.get_player_static_url())
    xpath = '//*[@id="repTb"]/tbody/tr[1]/td[6]/span'
    price = driver.find_element(By.XPATH, xpath)
    price = price.text.split("K")[0]
    driver.close()

    return price


async def main():
    loop = asyncio.get_event_loop()

    with open("client/log.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        player_names = [row[0] for row in csv_reader]

    path = urljoin(BASE_URL, PLAYER_ROUTE)

    tasks = [
        loop.run_in_executor(None, get_price, player_name, path)
        for player_name in player_names
    ]
    results = await asyncio.gather(*tasks)

    for player_name, price in zip(player_names, results):
        player = [player_name, price, float(price) * 1.6]
        players.append(player)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)
