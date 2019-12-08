#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jmartorell
"""

import requests

url = "http://finance.yahoo.com/quote/AAPL?p=AAPL"
wikiURL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

response = requests.get(url)
wikiResponse = requests.get(wikiURL)
htmlText = response.text

print("\ntarget url: ", url)
print("status code: ", response.status_code, "\n")

data = {
    "Company": []}

# We split from the last CIK and index it in position 0, which will give us the previous part
# of the first fractionation, where we will get all the names (or other associated data)
# of the 505 companies that make up the stock.
# wikiFirstParse = wikiResponse.text.split("contains 505 stocks")[1].split("0001555280")[0] # TRACER
# hyperLinkSplitWiki = wikiFirstParse.split("href=") # TRACER
# hyperLinkSplitWiki = wikiFirstParse.split("href=")[1] # TRACER (skip)
wikiFirstParse = wikiResponse.text.split("0001555280")[0]
wikiDataTable = wikiFirstParse.split("component stocks")[3]
hyperLinkSplitWiki = wikiDataTable.split("href=")


# 5->9->13 Extracting Company Ticker Symbols at shown positions
start = 4
tracker = 0
for position in range(len(hyperLinkSplitWiki)):
    if position > start:
        tracker = (position - (start + 1)) % 4
        if tracker == 0:
            tempData = hyperLinkSplitWiki[position].split('">')[1].split("</")[0]
            data["Company"].append(tempData)

# print(wikiFirstParse[5:20]) # TRACER (the brackets contain the range of chars to be displayed)
# print(hyperLinkSplitWiki[5:20]) # TRACER

print("data extraction:\n")
#5->9->13
print(data)


Indicators = {"Previous Close": [],
              "Open": [],
              "Bid": [],
              "Ask": [],
              "Day&#x27;s Range": [],
              "52 Week Range": [],
              "Volume": [],
              "Avg. Volume": [],
              "Market Cap": [],
              "Beta": [],
              "PE Ratio (TTM)": [],
              "EPS (TTM)": [],
              "Earnings Date": [],
              "Dividend &amp; Yield": [],
              "Ex-Dividend Date": [],
              "1y Target Est": []}

for indicator in Indicators:
    print(indicator)
    splitList = htmlText.split(indicator)
    if indicator in ['Day&#x27;s Range',
                     '52 Week Range',
                     'Dividend &amp; Yield']:
        afterFirstSplit = splitList[1].split("\">")[1]
        afterSecondSplit = afterFirstSplit.split("</td>")
    else:
        afterFirstSplit = splitList[1].split("\">")[2]
        afterSecondSplit = afterFirstSplit.split("<")
    data = afterSecondSplit[0]
    Indicators[indicator].append(data)

print(Indicators)




