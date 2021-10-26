import scrapy
from ..items import ScpItem, ScpNewsItem
from urllib.parse import urljoin


class IrnaNewsSpider(scrapy.Spider):

    name = 'irna'
    start_urls = [
        'https://www.irna.ir/archive?pl=2651'
    ]

    def parse(self, response):
        items = ScpItem()
        for news in response.css('li.news'):
            items['title'] = news.css('h3>a::text').get()
            items['description'] = news.css('p::text').get()
            items['category'] = news.css('p>span.category>span::text').get()
            items['time'] = news.css('time>a::text').get()
            img_relative_url = news.css('h3>a::attr(href)').get()
            items['url'] = urljoin('https://www.irna.ir/', img_relative_url)
            yield items


class FillFormSpider(scrapy.Spider):
    name = 'fill_form'

    def __init__(self, starturl, *args, **kwargs):
        self.start_urls = [starturl]
        super().__init__(*args, **kwargs)

    def parse(self, response):
        items = ScpNewsItem()
        items['title'] = response.css('h1.title>a::text').get()
        items['short_desc'] = response.css('p.introtext::text').get()
        items['desc'] = response.css('div.item-text>p::text').getall()
        yield items
