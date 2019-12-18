#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: maxschallwig
"""
# <html>
# <body>
#  <script>
#   data
#  </script>
#  <form>
#   data2
#  </form>
# </body>
# </html>
# dict["html"]
# {"html":{
#         "body":{
#                 "form":data
#                 }
#        }
# }
url = "https://finance.yahoo.com/quote/AAPL/key-statistics?p=AAPL"


def findXPath(element, target, path):
    if target in element.get_attribute("textContent") and element.tag_name == "script":
        return path
    newElements = element.find_elements_by_xpath("./*")
    for newElement in newElements:
        print(path + "/" + newElement.tag_name)
        final = findXPath(newElement, target, path + "/" + newElement.tag_name)
        if final != "":
            return final
    return ""


from selenium import webdriver

browser = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
browser.get(url)
# print(browser.page_source)
# elements = browser.find_elements_by_xpath("html/body/script")
# counter = 1
# for element in elements:
#    print(element.tag_name)
#    if "trailingPE" in element.get_attribute("textContent"):
#        print(counter)
##        break
#    counter +=1
# print("The final path is:",findXPath(element,"trailingPE","html"))
# elements = browser.find_elements_by_xpath("html/*")
# for element in elements: #[element1,element2] = [head,body]
#    newElements = element.find_elements_by_xpath("./*")
#    for newElement in newElements:
#        print(newElement.tag_name)
#    print(element.tag_name)
# print(element.text)
# print(element.get_attribute("textContent"))

element = browser.find_element_by_xpath("html/body/script[1]")
print(element.get_attribute("textContent"))
browser.quit()