## Scrapy Demo

#### Usage

    git clone https://github.com/svamja/scrapy_demo
    cd scrapy_demo
    scrapy crawl article_spider -a keyword=dispersion --output-format=csv --output=output.csv

#### Overview

This demo takes as input a keyword from user from command line argument ("dispersion" in above case).
Then, it searches the same on http://pubs.acs.org/ using the HTTP GET query.

Each link of the search result is individually accessed by the spider and the data from the article page is gathered.
It gathers 3 fields: Title, Authors (all authors), Number of Citings

The output is formatted into csv using the built-in CSV exporter.
