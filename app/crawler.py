import re
import time
from typing import List

import requests
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
headers = {'Accept-Encoding': 'identity'}


def fetch_title(domain: str) -> [str, str]:
    url = f'https://www.{domain}/index.html'
    r = requests.get(url, headers=headers)

    matches = re.findall("(?:<title>)(.*)(?:</title>)", r.text)
    if matches:
        return matches[0]
    return None


def crawl_domains(domains: List[str]) -> [str]:
    titles = []
    start = time.time()
    for domain in domains:
        title = fetch_title(domain)
        if title:
            titles.append(title)

    end = time.time()
    print(f'Elapsed time {end-start}')

    return titles
