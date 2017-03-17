# -*- coding: utf-8 -*-
"""
Your task in this exercise is to modify 'extract_carrier()` to get a list of
all airlines. Exclude all of the combination values like "All U.S. Carriers"
from the data that you return. You should return a list of codes for the
carriers.

All your changes should be in the 'extract_carrier()' function. The
'options.html' file in the tab above is a stripped down version of what is
actually on the website, but should provide an example of what you should get
from the full file.

Please note that the function 'make_request()' is provided for your reference
only. You will not be able to to actually use it from within the Udacity web UI.
"""

from bs4 import BeautifulSoup as bs
import requests

URL = 'https://www.transtats.bts.gov/Data_Elements.aspx?Data=2'
html_page = requests.get(URL)


def extract_carriers(page):
    data = []
    soup = bs(page.text)
    carrier_list = soup.find(id='CarrierList')
    all_options = carrier_list.find_all('option')
    for i in range(3, len(all_options)):
        print all_options[i].text
        data.append(all_options[i]['value'])  # 将['value']替换成.text即可提取所有航空公司的全名

    return data


data = []
soup = bs(html_page.text)
carrier_list = soup.find(id='CarrierList')
all_options = carrier_list.find_all('option')
for i in range(3, len(all_options)):
    print all_options[i].text
    data.append(all_options[i].text)



def make_request(data):
    s = requests.Session()

    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]
    airport = data["airport"]
    viewstategenerator = data['viewstategenerator']
    carrier = data["carrier"]

    r = s.post("https://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
               data=(("__EVENTTARGET", ""),
                     ("__EVENTARGUMENT", ""),
                     ("__VIEWSTATE", viewstate),
                     ("__VIEWSTATEGENERATOR", viewstategenerator),
                     ("__EVENTVALIDATION", eventvalidation),
                     ("CarrierList", carrier),
                     ("AirportList", airport),
                     ("Submit", "Submit")))

    return r.text




def test():
    data = extract_carriers(html_page)
    assert len(data) == 16
    assert "FL" in data
    assert "NK" in data


if __name__ == "__main__":
    test()
