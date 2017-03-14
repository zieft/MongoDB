from bs4 import BeautifulSoup as bs
import requests

URL = 'https://www.transtats.bts.gov/Data_Elements.aspx?Data=2'
file = requests.get(URL)


def options(soup, id):
    options_values = []
    carrier_list = soup.find(id=id)
    for option in carrier_list.findall('option'):
        options_values.append(option['value'])
    return options_values


def print_list(label, codes):
    print "\n{}".format(label)
    for c in codes:
        print c


def main():
    soup = bs(file.text)

    codes = options(soup, 'CarrierList')
    print_list('Carriers', codes)

    codes = options(soup, 'AirportList')
    print_list("Airports", codes)
