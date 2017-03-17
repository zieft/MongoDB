# -*- coding: utf-8 -*-
"""
Complete the 'extract_airports()' function so that it returns a list of airport
codes, excluding any combinations like "All".

Refer to the 'options.html' file in the tab above for a stripped down version
of what is actually on the website. The test() assertions are based on the
given file.
"""

from bs4 import BeautifulSoup as bs
import requests

URL = 'https://www.transtats.bts.gov/Data_Elements.aspx?Data=2'
html_page = requests.get(URL)


def extract_airports(page):
    data = []
    soup = bs(html_page.text)
    all_airports = soup.find(id='AirportList')
    options = all_airports.find_all('option')
    for i in range(len(options)):
        if not 'All' in options[i]['value']:
            data.append(options[i]['value'])
    return data


data = []
soup = bs(html_page.text)
all_airports = soup.find(id='AirportList')
options = all_airports.find_all('option')
for i in range(len(options)):
    if not 'All' in options[i]['value']:
        data.append(options[i]['value'])


def test():
    data = extract_airports(html_page)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data


if __name__ == "__main__":
    test()
