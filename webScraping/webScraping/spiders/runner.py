import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from webScraping.webScraping.spiders.ws1 import Ws1Spider

process = CrawlerProcess(settings=get_project_settings())
process.crawl(Ws1Spider)
process.start()