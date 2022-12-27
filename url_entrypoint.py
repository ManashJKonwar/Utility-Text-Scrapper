__author__ = "konwar.m"
__copyright__ = "Copyright 2022, AI R&D"
__credits__ = ["konwar.m"]
__license__ = "Individual Ownership"
__version__ = "1.0.1"
__maintainer__ = "konwar.m"
__email__ = "rickykonwar@gmail.com"
__status__ = "Development"

import time
import pandas as pd

from multiprocessing import cpu_count

from url_validator import validate_all
from url_scrapping import scrap_all

class URLValidator:
    def __init__(self, url_list, no_of_workers=2*cpu_count()):
        self._url_list = url_list
        self._no_of_workers = no_of_workers
        self._active_urls = []
        self._inactive_urls = []
        self._unreachable_urls = []

    @property
    def get_active_urls(self):
        return self._active_urls

    @property
    def get_inactive_urls(self):
        return self._inactive_urls

    @property
    def get_unreachable_links(self):
        return self._unreachable_urls

    def run_validation(self):
        results = validate_all(
                        urls=self._url_list, 
                        no_of_workers=self._no_of_workers
                    )

        self._active_urls = [result['active_links'][0] for result in results if len(result['active_links'])>0]
        self._inactive_urls = [result['inactive_links'][0] for result in results if len(result['inactive_links'])>0]
        self._unreachable_urls = [result['unreachable_links'][0] for result in results if len(result['unreachable_links'])>0]


class URLScrapper:
    def __init__(self, url_list, no_of_workers=2*cpu_count()):
        self._url_list = url_list
        self._no_of_workers = no_of_workers
        self._metadata_cols = ['url_id', 'url', 'text', 'title', 'author', 'hostname', 'date', 'categories']
        self._scrapped_df = pd.DataFrame(columns=self._metadata_cols)

    @property
    def get_scrapped_df(self):
        return self._scrapped_df

    def run_scrapping(self):
        results = scrap_all(
                        urls=self._url_list, 
                        no_of_workers=self._no_of_workers
                    )

        results_df = pd.DataFrame(results)
        results_df['url_id'] = range(len(results_df))

        self._scrapped_df = results_df.copy()

if __name__ == "__main__":
    data = pd.read_csv('url_data.csv').head(500)
    url_list = data.PERMALINK.tolist()
    n_cores = cpu_count()

    # Trigerring the validation process
    start_validation = time.time()
    validator_instance = URLValidator(url_list=url_list, no_of_workers=2*cpu_count())
    validator_instance.run_validation()
    end_validation = time.time()

    # Triggering the scrapping process
    start_scrapping = time.time()
    scrapping_instance = URLScrapper(url_list=validator_instance.get_active_urls, no_of_workers=2*cpu_count())
    scrapping_instance.run_scrapping()
    end_scrapping = time.time()

    # Summarizing the pipeline
    print(f'{len(url_list)} links are validated in {end_validation - start_validation} seconds')
    print(f'{len(validator_instance.get_active_urls)} links are scrapped in {end_scrapping - start_scrapping} seconds')