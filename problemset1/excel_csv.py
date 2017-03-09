'''
Find the time and value of max load for each of the regions
COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
and write the result out in a csv file, using pipe character | as the delimiter.

Example:
Station|Year|Month|Day|Hour|Max Load
COAST|2013|01|01|10|12345.6
EAST|2013|01|01|10|12345.6
FAR_WEST|2013|01|01|10|12345.6
NORTH|2013|01|01|10|12345.6
NORTH_C|2013|01|01|10|12345.6
SOUTHERN|2013|01|01|10|12345.6
SOUTH_C|2013|01|01|10|12345.6
WEST|2013|01|01|10|12345.6

'''

import xlrd
import os
import csv
from zipfile import ZipFile

datafile = "C:\\Users\\zieft\\Dropbox\\PyCharmProjects_WIN\\MongoDB\\lesson_1\\2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = [["Station", "Year", "Month", "Day", "Hour", "Max Load"]]
    stations = sheet.row_values(0, start_colx=1, end_colx=-1)

    station_values_dict = dict()
    counter = 0
    for station in stations:
        if counter <= len(sheet.row_values(0, start_colx=1, end_colx=-1)):
            station_values_dict[station] = sheet.col_values(counter, start_rowx=1, end_rowx=None)
            counter += 1

    counter2 = 1
    for key in station_values_dict:
        if counter2 < len(stations) + 1:
            _ = []
            _.append(stations[counter2 - 1])
            station_max_load = max(station_values_dict[key])
            max_load_index = station_values_dict[key].index(station_max_load)
            max_time = xlrd.xldate_as_tuple(max_load_index, 0)
            year, month, day, hour, _1, _2 = max_time
            _.append(year)
            _.append(month)
            _.append(hour)
            _.append(max(station_values_dict[key]))
            data.append(_)
        counter2 += 1
    # YOUR CODE HERE
    # Remember that you can use xlrd.xldate_as_tuple(sometime, 0) to convert
    # Excel date to Python tuple of (year, month, day, hour, minute, second)
    return data


def save_file(data, filename):
    with open(outfile, 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


# YOUR CODE HERE


def test():
    open_zip(datafile)
    data = parse_file(datafile)
    save_file(data, outfile)

    number_of_rows = 0
    stations = []

    ans = {'FAR_WEST': {'Max Load': '2281.2722140000024',
                        'Year': '2013',
                        'Month': '6',
                        'Day': '26',
                        'Hour': '17'}}
    correct_stations = ['COAST', 'EAST', 'FAR_WEST', 'NORTH',
                        'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']
    fields = ['Year', 'Month', 'Day', 'Hour', 'Max Load']

    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            station = line['Station']
            if station == 'FAR_WEST':
                for field in fields:
                    # Check if 'Max Load' is within .1 of answer
                    if field == 'Max Load':
                        max_answer = round(float(ans[station][field]), 1)
                        max_line = round(float(line[field]), 1)
                        assert max_answer == max_line

                    # Otherwise check for equality
                    else:
                        assert ans[station][field] == line[field]

            number_of_rows += 1
            stations.append(station)

        # Output should be 8 lines not including header
        assert number_of_rows == 8

        # Check Station Names
        assert set(stations) == set(correct_stations)


if __name__ == "__main__":
    test()

import csv

with open('eggs.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
