import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
header = {'user-agent': ua.firefox}

google_page = 'https://www.google.com'
autocomplete = 'https://www.'


def target_url():
    input_url = input("BS4 PARSER."
                      "\n\t(Default display: google.com) "
                      "\n\nINPUT URL:")

    if input_url == "":
        input_url = google_page
    elif autocomplete not in input_url:
        input_url = autocomplete + input_url

    requested_url = requests.get(input_url, headers=header)
    soup = BeautifulSoup(requested_url.content, 'lxml')  # html.parser

    print(soup.prettify())


if __name__ == '__main__':
    target_url()
