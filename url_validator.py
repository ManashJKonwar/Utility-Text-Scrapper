__author__ = "konwar.m"
__copyright__ = "Copyright 2022, AI R&D"
__credits__ = ["konwar.m"]
__license__ = "Individual Ownership"
__version__ = "1.0.1"
__maintainer__ = "konwar.m"
__email__ = "rickykonwar@gmail.com"
__status__ = "Development"

import time
import requests
import warnings
import pandas as pd

from tqdm import tqdm
from threading import Thread, local
from requests.sessions import Session
from concurrent.futures import ThreadPoolExecutor

warnings.filterwarnings('ignore')

thread_local = local()

def get_session() -> Session:
    if not hasattr(thread_local,'session'):
        thread_local.session = requests.Session()
    return thread_local.session

def validate_link(url:str) -> dict:
    active_links, inactive_links, unreachable_links = [], [], []
    session = get_session()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
    try:
        with session.get(url, timeout=10, verify=False, headers=headers, allow_redirects=False) as response:
            # print(f'Read {len(response.content)} from {url}')
            if response.status_code == 200:
                active_links.append(url)
            else:
                inactive_links.append(url)
    except requests.ConnectionError:
        unreachable_links.append(url)
        pass
    except requests.exceptions.MissingSchema:
        unreachable_links.append(url)
        pass
    except Exception:
        unreachable_links.append(url)
        pass

    return {
        'active_links': active_links,
        'inactive_links': inactive_links,
        'unreachable_links': unreachable_links
    }

def validate_all(urls:list, no_of_workers:int) -> dict:
    with ThreadPoolExecutor(max_workers=no_of_workers) as executor:
        results = list(tqdm(executor.map(validate_link, urls), total=len(urls)))
    return results

if __name__ == "__main__":
    data = pd.read_csv('url_data.csv').head(500)
    url_list = data.PERMALINK.tolist()
    start = time.time()
    results = validate_all(url_list, 4)
    print(len(results))
    print(results[0])
    end = time.time()
    print(f'{len(url_list)} links are validated in {end - start} seconds')