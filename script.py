import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import time


def site_scraper(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return "Failed to retrieve the page, status code:", response.status_code
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def extract_info(scraper_datas, msec):
    datas = []
    for data in tqdm(scraper_datas, "- Extracting"):
        try:
            _data = site_scraper(data)
            datas.append(_data)
        except Exception as e:
            print(f"- Error with {data} and error is {e}")
        time.sleep(msec) ## Keep connstant time lag before hitting another End Point.
    return datas