# Overview
The project use the API presented [here](https://github.com/ricardotachinardi/ifood-scrapper/blob/main/explorando_api_ifood.ipynb) to scrape data about all the restaurants in iFood using an Scrapy Spider.

# Download the datasets with the all the restaurants in iFood
I uploaded to Kaggle the datasets corresponding to November 2020 and February 2021, see [here](https://www.kaggle.com/ricardotachinardi/ifood-restaurants-data)

# Installation and use of the scrapper

***Remember to install lista_coordenadas.csv and put in the same folder as the spider***

Install it using `pip` (preferably on an virtual environment):
```shell
$ pip install -r requirements.txt
```

Then, you can run the spider with:
```shell
$ scrapy runspider ifood-spider.py -o output.csv
```

You can use other output formats. More info on [this link](https://docs.scrapy.org/en/latest/topics/feed-exports.html#serialization-formats).
