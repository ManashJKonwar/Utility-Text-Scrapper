__author__ = "konwar.m"
__copyright__ = "Copyright 2022, AI R&D"
__credits__ = ["konwar.m"]
__license__ = "Individual Ownership"
__version__ = "1.0.1"
__maintainer__ = "konwar.m"
__email__ = "rickykonwar@gmail.com"
__status__ = "Development"

import json
import requests
import trafilatura
import numpy as np

from bs4 import BeautifulSoup
from requests.models import MissingSchema

def bs_extract_text(response_content):
    """
    This is a fallback function, so that we can always return a value for text content.
    Even for when both Trafilatura and BeautifulSoup are unable to extract the text from a 
    single URL.
    
    args: 
    - response_content (bs4 content): content extracted for url wherever trafilatura fails to extract

    return: 
    - cleaned_text (str): extracted text 
    """
    # Create the beautifulsoup object:
    soup = BeautifulSoup(response_content, 'html.parser')
    
    # Finding the text:
    text = soup.find_all(text=True)
    
    # Remove unwanted tag elements:
    cleaned_text = ''
    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head', 
        'input',
        'script',
        'style',]

    # Then we will loop over every item in the extract text and make sure that the beautifulsoup4 tag
    # is NOT in the blacklist
    for item in text:
        if item.parent.name not in blacklist:
            cleaned_text += '{} '.format(item)
            
    # Remove any tab separation and strip the text:
    cleaned_text = cleaned_text.replace('\t', '')
    return cleaned_text.strip()

def extract_text(url):
    """
    This is text extraction function which is responisble for mining the text from the input url. It uses
    trafilatura as well as beautiful soup to complete the extraction process. However, if both fails to extract any 
    text from the input url, we will return an empty variable
    
    args: 
    - response_content (bs4 content): content extracted for url wherever trafilatura fails to extract

    return: 
    - cleaned_text (str): extracted text 
    """
    downloaded_url = trafilatura.fetch_url(url)
    try:
        a = trafilatura.extract(downloaded_url, output_format='json', with_metadata=True, include_comments = False,
                            date_extraction_params={'extensive_search': True, 'original_date': True})
    except AttributeError:
        a = trafilatura.extract(downloaded_url, output_format='json', with_metadata=True,
                            date_extraction_params={'extensive_search': True, 'original_date': True})

    if a:
        json_output = json.loads(a)
        return json_output['text']
    else:
        try:
            resp = requests.get(url, timeout=120)
            # We will only extract the text from successful requests:
            if resp.status_code == 200:
                return bs_extract_text(resp.content)
            else:
                # This line will handle for any failures in both the Trafilature and BeautifulSoup4 functions:
                return np.nan
        # Handling for any URLs that don't have the correct protocol
        except MissingSchema:
            return np.nan

if __name__ == "__main__":
    url_list = [
        'https://en.wikipedia.org/wiki/Virat_Kohli', 
        'https://www.flipkart.com/apple-iphone-14-pro-max-space-black-256-gb/p/itm8a92b3d600e04?pid=MOBGHWFHSEZUKWDM&lid=LSTMOBGHWFHSEZUKWDM1LFARE&marketplace=FLIPKART&sattr[]=color&sattr[]=storage&st=storage'
    ]
    for url in url_list:
        print(extract_text(url))