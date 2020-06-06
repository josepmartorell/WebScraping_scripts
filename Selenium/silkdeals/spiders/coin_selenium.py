# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy_selenium import SeleniumRequest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from shutil import which


class CoinSpiderSelenium(scrapy.Spider):
    name = 'coin_selenium'
    allowed_domains = ['www.livecoin.net/en']
    start_url = [
        'https://www.livecoin.net/en'
    ]

    def __init__(self):
        firefox_options = Options()
        firefox_options.add_argument('--headless')
        firefox_path = 'geckodriver'
        driver = webdriver.Firefox(executable_path=firefox_path, options=firefox_options)
        driver.set_window_size(1920, 1080)
        driver.get('https://www.livecoin.net/en')

        rur_tab = driver.find_element_by_xpath('//article/div/div[2]/div/div[2]/div/div[1]')
        rur_tab.click()

        self.html = driver.page_source
        driver.close()

    def start_requests(self):
        yield SeleniumRequest(
            url='https://www.livecoin.net/en',
            wait_time=3,
            callback=self.parse
        )

    def parse(self, response):
        resp = Selector(text=self.html)
        for currency in resp.xpath("//div[contains(@class, 'ReactVirtualized__Table__row tableRow___3EtiS ')]"):
            yield {
                'currency pair': currency.xpath(".//div[1]/div/text()").get(),
                'volume(24h)': currency.xpath(".//div[2]/span/text()").get()
            }
