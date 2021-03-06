import re
import time
import requests
import concurrent.futures

from typing import List

from app.mongo import write_elapsed_time

headers = {'Accept-Encoding': 'identity'}


def fetch_title(domain: str) -> [str, str]:
    url = f'https://www.{domain}/index.html'
    print(f'fetching {url}')
    r = requests.get(url, headers=headers)
    matches = re.findall("(?:<title>)(.*)(?:</title>)", r.text)
    if matches:
        return matches[0]
    return None


def crawl_domains(domains: List[str]) -> [str]:
    try:
        start = time.time()
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            results = executor.map(fetch_title, domains, timeout=10)

            titles = [r for r in results if r is not None]

            elapsed_time = time.time() - start
            print(f'Elapsed time {elapsed_time}')
            write_elapsed_time(elapsed_time)

            return titles

    # Hack: For some reason can't catch asyncio.TimeoutException
    except Exception as e:
        print(e)
        return []


