# Utility-Text-Scrapper
The prime objective of this repository is to facilitate the extraction of texts from web URLs and also parallelize the extraction process so as to reduce the processing time  

## **Table of Contents**
* [General Information](#general-information)  
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [References](#references)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->

## **General Information**  
- The prime objective of this repository is to help developers / researchers / data enthusiasts in validating a list of URLs, classify them as active, inactive and unreachable links and also provide a way to scrap all textual content within those active URL links.  
- Use built in python libaries and apply concurrent workers (asyncronous operation) to perform validation as well as scrapping operations which would result in speeding up both these operations. 
- The validation process makes use of [requests](https://pypi.org/project/requests/2.28.1/) library whereas scrapping process is supported by [Trafilatura](https://pypi.org/project/trafilatura/1.4.0/) and [Beautiful Soup](https://pypi.org/project/beautifulsoup4/4.11.1/) libaries. The features of these libraries are mentioned below if you wnat to know as to why these were choosen.

## **Technologies Used**
- Python 
- Trafilatura
- Beautiful Soup  
- Concurrent Tasks

## **Features**  
- General features:  
    1. Leverage 3rd party libraries and helps in optimum level of text scrapping even if any one of the library fails to perform.  
    2. Asynchronous URL validation and text scrapping resulting in reduced operational time.
- Trafilatura features (as per [official documentation](https://trafilatura.readthedocs.io/en/latest/index.html#) of Trafilatura):
    1. Web crawling and text discovery  
        * Focused crawling and politeness rules  
        * Support for sitemaps (TXT, XML) and feeds (ATOM, JSON, RSS)  
        * URL management (blacklists, filtering and de-duplication)
    2. Seamless and parallel processing, online and offline  
        * URLs, HTML files or parsed HTML trees usable as input  
        * Efficient and polite processing of download queues  
        * Conversion of previously downloaded files
    3. Robust and efficient extraction  
        * Main text (with LXML, common patterns and generic algorithms: jusText, fork of readability-lxml)  
        * Metadata (title, author, date, site name, categories and tags)  
        * Formatting and structural elements: paragraphs, titles, lists, quotes, code, line breaks, in-line text formatting  
        * Comments (if applicable)
    4. Output formats  
        * Text (minimal formatting or Markdown)  
        * CSV (with metadata, tab-separated values)  
        * JSON (with metadata)  
        * XML (with metadata, text formatting and page structure) and TEI-XML
    5. Optional add-ons  
        * Language detection on extracted content  
        * Graphical user interface (GUI)  
        * Speed optimizations  

## **Screenshots**  

## **Setup:**
- git clone https://github.com/ManashJKonwar/Utility-Text-Scrapper.git (Clone the repository)
- python3 -m venv scrappingVenv (Create virtual environment from existing python3)
- activate the "scrappingVenv" (Activating the virtual environment)
- pip install -r requirements.txt (Install all required python modules)