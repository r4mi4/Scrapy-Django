# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScpItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    category = scrapy.Field()
    time = scrapy.Field()
    url = scrapy.Field()

class ScpNewsItem(scrapy.Item):
    title = scrapy.Field()
    short_desc = scrapy.Field()
    desc = scrapy.Field()
    # category = scrapy.Field()
    # time = scrapy.Field()