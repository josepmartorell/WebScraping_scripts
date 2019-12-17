# -*- encoding: utf-8 -*-
# class for scraping

import os

import requests
from lxml import html
from bs4 import BeautifulSoup


class Scraping:

    def scrapingBeautifulSoup(self, url):

        try:
            print("Getting images with BeautifulSoup " + url)

            response = requests.get(url)
            bs = BeautifulSoup(response.text, 'lxml')

            # create directory for save images
            os.system("mkdir images")

            for tagImage in bs.find_all("img"):
                # print(tagImage['src'])
                if tagImage['src'].startswith("http") == False:
                    download = url + tagImage['src']
                else:
                    download = tagImage['src']
                print(download)
                # download images in img directory
                r = requests.get(download)
                f = open('images/%s' % download.split('/')[-1], 'wb')
                f.write(r.content)
                f.close()

        except Exception as e:
            print(e)
            print("Connection Error " + url)
            pass

    def scrapingImages(self, url):
        print("\nGetting images of the url:" + url)

        try:
            response = requests.get(url)
            parsed_body = html.fromstring(response.text)

            # regular expression to get images
            images = parsed_body.xpath('//img/@src')

            print('Images %s found' % len(images))

            # create directory for save images
            os.system("mkdir images")

            for image in images:
                if image.startswith("http") == False:
                    download = url + image
                else:
                    download = image
                print(download)
                # download images in images directory
                r = requests.get(download)
                f = open('images/%s' % download.split('/')[-1], 'wb')
                f.write(r.content)
                f.close()

        except Exception as e:
            print(e)
            print("Connection error with " + url)
            pass

    def scrapingPDF(self, url):
        print("\nGetting pdfs of the url:" + url)

        try:
            response = requests.get(url)
            parsed_body = html.fromstring(response.text)

            # regular expression to get pdf
            pdfs = parsed_body.xpath('//a[@href[contains(., ".pdf")]]/@href')

            # create directory for save pdfs
            if len(pdfs) > 0:
                os.system("mkdir pdfs")

            print('Found %s pdf' % len(pdfs))

            for pdf in pdfs:
                if pdf.startswith("http") == False:
                    download = url + pdf
                else:
                    download = pdf
                print(download)

                # download pdfs
                r = requests.get(download)
                f = open('pdfs/%s' % download.split('/')[-1], 'wb')
                f.write(r.content)
                f.close()

        except Exception as e:
            print(e)
            print("Connection error with " + url)
            pass

    def scrapingLinks(self, url):
        print("\nGetting links from the url:" + url)

        try:
            response = requests.get(url)
            parsed_body = html.fromstring(response.text)

            # regular expression to get links
            links = parsed_body.xpath('//a/@href')

            print('links% s found' % len(links))

            for link in links:
                print(link)

        except Exception as e:
            print(e)
            print("Connection error with " + url)
            pass