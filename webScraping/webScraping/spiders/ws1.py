# -*- coding: utf-8 -*-

import logging

import scrapy


class Ws1Spider(scrapy.Spider):
    name = 'ws1'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.xpath('//td/a')
        for country in countries:
            name = country.xpath('.//text()').get(),
            self.country_name = name,
            link = country.xpath('.//@href').get()
            # yield response.follow(url=link)
            yield response.follow(url=link, callback=self.parse_country, meta={'country_name': name})

    def parse_country(self, response):
        # logging.info(response.url)
        self.country_name = response.request.meta['country_name']
        rows = response.xpath('//table')

        for row in rows:
            name = self.country_name,
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
            yearly_change = row.xpath('.//td[3]/text()').get()
            net_change = row.xpath('.//td[4]/text()').get()
            migrants = row.xpath('.//td[5]/text()').get()
            med_age = row.xpath('.//td[6]/text()').get()
            fert_rate = row.xpath('.//td[7]/text()').get()
            density = row.xpath('.//td[8]/text()').get()
            urban_pop = row.xpath('.//td[9]/text()').get()
            world_share = row.xpath('.//td[11]/text()').get()
            land_area = row.xpath('.//td[12]/text()').get()
            sorted = row.xpath('.//td[13]/text()').get()

            yield {
                'sorted': sorted,
                'country name': name,
                'population': population,
                'yearly change': yearly_change,
                'net change': net_change,
                'density': density,
                'land area': land_area,
                'migrants': migrants,
                'fert rate': fert_rate,
                'med age': med_age,
                'urban pop%': urban_pop,
                'world share': world_share,
                'year': year

            }