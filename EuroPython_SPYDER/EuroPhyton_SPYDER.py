#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scrapy import signals
from scrapy.item import Item, Field
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.settings import Settings
from scrapy.spiders import CrawlSpider, Rule
from scrapy.xlib.pydispatch import dispatcher


class EuropythonItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    author = Field()
    description = Field()
    date = Field()
    tags = Field()


class EuropythonSpyder(CrawlSpider):
    name = "europython_spyder"
    allowed_domains = ["ep2015.europython.eu"]
    start_urls = ['http://ep2015.europython.eu/en/events/sessions']

    # Pattern for entries that meet the conference / talks format
    rules = [Rule(LxmlLinkExtractor(allow=['conference/talks']), callback='process_response')]

    def process_response(self, response):
        item = EuropythonItem()
        print(response)
        item['title'] = response.xpath("//div[contains(@class, 'grid-100')]//h1/text()").extract()
        item['author'] = response.xpath("//div[contains(@class, 'talk-speakers')]//a[1]/text()").extract()
        item['description'] = response.xpath("//div[contains(@class, 'cms')]//p//text()").extract()
        item['date'] = response.xpath("//section[contains(@class, 'talk when')]/strong/text()").extract()
        item['tags'] = response.xpath("//div[contains(@class, 'all-tags')]/span/text()").extract()

        return item


def main():
    """"Main routine for the execution of the Spider"""

    # set up signal to catch items scraped
    def catch_item(sender, item, **kwargs):
        print("Item extracted:", item)

    dispatcher.connect(catch_item, signal=signals.item_passed)

    settings = Settings()
    settings.set("USER_AGENT",
                 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36")
    settings.set("LOG_ENABLED", False)

    # setup crawler
    from scrapy.crawler import CrawlerProcess

    crawler = CrawlerProcess(settings)

    # define the spider for the crawler
    crawler.crawl(EuropythonSpyder())

    # start scrapy
    print("STARTING ENGINE")
    crawler.start()  # start the crawler by calling the defined spider
    print("ENGINE STOPPED")


if __name__ == '__main__':
    main()