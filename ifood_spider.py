# run the file using scrapy runspider ifood-spider.py
# inspired by https://github.com/nathan-cruz77/ifood/blob/master/ifood_spider.py
import json
import scrapy
import pandas as pd


BASE_IFOOD_URL = 'https://www.ifood.com.br/delivery/'
BASE_AVATAR_URL = 'https://static-images.ifood.com.br/image/upload/f_auto,t_high/logosgde/'
#BASE_URL = 'https://marketplace.ifood.com.br/v1/merchants?latitude=-23.19529&longitude=-45.90321&channel=IFOOD'


class Restaurant(scrapy.Item):

    name = scrapy.Field()
    rating = scrapy.Field()
    price_range = scrapy.Field()
    delivery_time = scrapy.Field()
    delivery_fee = scrapy.Field()
    distance = scrapy.Field()
    category = scrapy.Field()
    avatar = scrapy.Field()
    url = scrapy.Field()
    tags = scrapy.Field()
    paymentCodes = scrapy.Field()
    minimumOrderValue = scrapy.Field()
    regionGroup = scrapy.Field()
    catalogGroup = scrapy.Field()
    ibge = scrapy.Field()
    # schedule removed due to errors and not being able to extract useful data
    #schedule = scrapy.Field()

    @staticmethod
    def parse_avatar(item):
        avatar = ''

        for resource in item['resources']:
            if resource['type'].lower() == 'logo':
                avatar = resource['fileName']

        if avatar:
            return ''.join([BASE_AVATAR_URL, avatar])

        return avatar

    # make it easier to split the lists later
    @staticmethod
    def parse_list(lista):
        return " $$ ".join(str(e) for e in lista)


class IfoodSpider(scrapy.Spider):
    name = 'ifood'

    def start_requests(self):
        df = pd.read_csv("lista_coordenadas.csv")

        # you can use an smaller part of the df
        #df = df.iloc[5573:5660]
        # print(df)

        for i in range(len(df)):
            lat = df['latitude'].iloc[i]
            ibge = df['codigo_ibge'].iloc[i]
            long = df['longitude'].iloc[i]

            BASE_URL = f"https://marketplace.ifood.com.br/v1/merchants?latitude={lat}&longitude={long}&channel=IFOOD"

            yield scrapy.Request(f'{BASE_URL}&size=0', callback=self.parse_core, meta={"ibge": ibge, "base_url": BASE_URL})

    def parse_core(self, response):
        data = json.loads(response.text)

        total = data['total']
        pages_count = total // 100

        if total / 100 != total // 100:
            pages_count += 1

        for page in range(pages_count):
            yield scrapy.Request(f'{response.meta["base_url"]}&size={100}&page={page}', callback=self.parse_page, meta={"ibge": response.meta['ibge']})

    def parse_page(self, response):
        data = json.loads(response.text)

        for item in data['merchants']:
            yield Restaurant({
                'name': item['name'],
                'rating': item['userRating'],
                'price_range': item['priceRange'],
                'delivery_time': item['deliveryTime'],
                'delivery_fee': item['deliveryFee']['value'],
                'distance': item['distance'],
                'category': item['mainCategory']['name'],
                'avatar': Restaurant.parse_avatar(item),
                'url': "{}{}/{}".format(BASE_IFOOD_URL, item['slug'], item['id']),
                'tags': Restaurant.parse_list(item['tags']),
                'paymentCodes': Restaurant.parse_list(item['paymentCodes']),
                'minimumOrderValue': item['minimumOrderValue'],
                'regionGroup': item['contextSetup']['regionGroup'],
                'catalogGroup': item['contextSetup']['catalogGroup'],
                'ibge': response.meta['ibge']
            })
