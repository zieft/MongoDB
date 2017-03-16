# -*- coding: utf-8 -*-
# Please note that the function 'make_request' is provided for your reference only.
# You will not be able to to actually use it from within the Udacity web UI.
# Your task is to process the HTML using BeautifulSoup, extract the hidden
# form field values for "__EVENTVALIDATION" and "__VIEWSTATE" and set the appropriate
# values in the data dictionary.
# All your changes should be in the 'extract_data' function
from bs4 import BeautifulSoup as bs
import requests
import json

URL = 'https://www.transtats.bts.gov/Data_Elements.aspx?Data=2'
html_page = requests.get(URL)


def my_extract_data(page):
    data = {}
    soup = bs(html_page.text)
    __VIEWSTATE = soup.find(id='__VIEWSTATE')
    data['viewstate'] = __VIEWSTATE['value']
    __EVENTVALIDATION = soup.find(id='__EVENTVALIDATION')
    data['eventvalidation'] = __EVENTVALIDATION['value']
    __VIEWSTATEGENERATOR = soup.find(id='__VIEWSTATEGENERATOR')
    data['viewstategenerator'] = __VIEWSTATEGENERATOR['value']

    return data


def extract_data(page):
    data = {"eventvalidation": "",
            "viewstate": ""}
    with open(page, "r") as html:  # 给出的答案是读取本地文件的例子，不再详细讨论
        soup = bs(html, "lxml")  # 这个lxml参数不能少，不知道为什么
        ev = soup.find(id="__EVENTVALIDATION")
        data["eventvalidation"] = ev["value"]

        vs = soup.find(id="__VIEWSTATE")
        data["viewstate"] = vs["value"]

    return data


def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]
    viewstategenerator = data["viewstategenerator"]

    r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                      data={'AirportList': "BOS",
                            'CarrierList': "VX",
                            'Submit': 'Submit',
                            "__EVENTTARGET": "",
                            "__EVENTARGUMENT": "",
                            "__EVENTVALIDATION": eventvalidation,
                            "__VIEWSTATE": viewstate,
                            "__VIEWSTATEGENERATOR": viewstategenerator
                            })

    return r.text


def test():
    data = extract_data(html_page)
    assert data["eventvalidation"] != ""
    assert data["eventvalidation"].startswith("/wEWjAkCoIj1ng0")
    assert data["viewstate"].startswith("/wEPDwUKLTI")


test()
