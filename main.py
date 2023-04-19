import requests
import selectorlib
from datetime import datetime
import sqlite3

connection = sqlite3.connect("data.db")

URL = "http://programmer100.pythonanywhere.com/"


def scrape(url):
    response = requests.get(url)
    source = response.text
    return source


def extract(data_info):
    extractor = selectorlib.Extractor.from_yaml_file("data.yaml")
    value = extractor.extract(data_info)["degrees"]
    return value


def store(temp):
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO weather VALUES(?,?)", (now, temp))
    connection.commit()
    # now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    # with open("data.txt", "a") as file:
    #     line = f"{now},{extr}\n"
    #     file.write(line)


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    store(extracted)
