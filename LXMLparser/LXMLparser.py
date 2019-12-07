# -*- encoding: utf-8 -*-
# class for scraping

import os
from os import strerror
import requests
from lxml import html
from bs4 import BeautifulSoup
import urllib.parse


class Scraping:

    def scrapingImages(self, url):
        print("Getting images of the url: " + url)

        try:
            response = requests.get(url)
            parsed_body = html.fromstring(response.text)

            # regular expression to get images
            images = parsed_body.xpath('//img/@src')
            print('images % found' % len(images))

            # create directory for save images
            os.system("mkdir images")

            for image in images:
                if not image.startswith("http"): # TRACE
                    download = url + image
                else:
                    download = image
                print(download) # TRACE
                # download images in img directory
                r = requests.get(download)
                f = open('images/%s' % download.split('/')[-1], 'wb')
                f.write(r.content)
                f.close()
#TRACE
        except IOError as e:
            print("I/O error occurred: ", strerror(e.errno))
            print("Connection Error " + url)
            pass
#

#################################################################VOY POR AQUI...

    def scrapingPDF(self, url):
        print("\nGetting pdfs from the url: " + url)

        try:
            response = requests.get(url)
            parsed_body = html.fromstring(response.text)

            # regular expression to get pdf
            pdfs = parsed_body.xpath('//a[@href[contains(., ".pdf")]]/@href')

            # create directory for save pdfs
            if len(pdfs) > 0:
                os.system("mkdir pdfs")

            print('Found %s pdf' % len(pdfs)) # TRACE

            for pdf in pdfs:
                if pdf.startswith("http") == False:
                    download = url + pdf
                else:
                    download = pdf
                print(download) # TRACE

                # download pdfs
                r = requests.get(download)
                f = open('pdfs/%s' % download.split('/')[-1], 'wb')
                f.write(r.content)
                f.close()


# TRACE
        except IOError as e:
            print("I/O error occurred: ", strerror(e.errno))
            print("Connection Error " + url)
            pass
#

#################################################################

    def scrapingLinks(self, url):
        print("\nGetting links from the url: " + url)

        try:
            response = requests.get(url)
            parsed_body = html.fromstring(response.text)

            # regular expression to get links
            links = parsed_body.xpath('//a/@href')

            print('links %s found' % len(links))

            for link in links:
                print(link)


# TRACE
        except IOError as e:
            print("I/O error occurred: ", strerror(e.errno))
            print("Connection Error " + url)
            pass
######