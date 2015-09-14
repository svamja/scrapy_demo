# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# The list of the fields to export from each Article
# This is used in ChemSpider
class ArticleItem(scrapy.Item):
    title = scrapy.Field()
    authors = scrapy.Field()
    number_of_citings = scrapy.Field()

