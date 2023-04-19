import requests
import selectorlib
from datetime import datetime

URL = "http://programmer100.pythonanywhere.com/"


def scrape(url):
    response = requests.get(url)
    source = response.text
    return source


def extract(data_info):
    extractor = selectorlib.Extractor.from_yaml_file("data.yaml")
    value = extractor.extract(data_info)["degrees"]
    return value


def store(extracted):
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    with open("data.txt", "a") as file:
        line = f"{now},{extracted}\n"
        file.write(line)


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    store(extracted)
