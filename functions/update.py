import csv


def update_prices(players: dict):
    with open("client/log.csv", mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(players)
