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

# Some info on the list of coordinates
I used the coordinate - city pair present in [this repo](https://github.com/kelvins/Municipios-Brasileiros/) to obtain the coordinates of all the cities in Brazil. Then, I slightly moved the coordinates of the 100 biggest cities to generate more points (making it possible to find restaurants that would not be available in the center of the city). The bigger the city, the more points I generated. The population data can be found [here](http://blog.mds.gov.br/redesuas/wp-content/uploads/2018/06/Lista-de-Munic%C3%ADpios-com-IBGE-Brasil.xlsx)
