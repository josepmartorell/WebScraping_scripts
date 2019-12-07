# -*- encoding: utf-8 -*-

from LXMLparser import Scraping

if __name__ == '__main__':
    url = 'https://www.google.es'
    scraping = Scraping()
    scraping.scrapingImages(url)
    scraping.scrapingPDF(url)
    scraping.scrapingLinks(url)
