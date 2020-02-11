# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CityRankItem(scrapy.Item):
    # define the fields for your item here like:
    city_name = scrapy.Field()
    inOrout_city_province_name = scrapy.Field()
    inOrOUt_city = scrapy.Field()
    value = scrapy.Field()
    inOrout = scrapy.Field()
    date = scrapy.Field()
    # pass


class ProvinceRankItem(scrapy.Item):
    # define the fields for your item here like:
    city_name = scrapy.Field()
    province_name = scrapy.Field()
    value = scrapy.Field()
    inOrout = scrapy.Field()
    date = scrapy.Field()