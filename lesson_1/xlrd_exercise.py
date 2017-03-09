"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

import xlrd
from zipfile import ZipFile

datafile = "C:\\Users\\zieft\\Dropbox\\PyCharmProjects_WIN\\MongoDB\\lesson_1\\2013_ERCOT_Hourly_Load_Data.xls"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def my_parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    ### example on how you can get the data
    # sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

    ### other useful methods:
    # print "\nROWS, COLUMNS, and CELLS:"
    # print "Number of rows in the sheet:",
    # print sheet.nrows
    # print "Type of data in cell (row 3, col 2):",
    # print sheet.cell_type(3, 2)
    # print "Value in cell (row 3, col 2):",
    # print sheet.cell_value(3, 2)
    # print "Get a slice of values in column 3, from rows 1-3:"
    # print sheet.col_values(3, start_rowx=1, end_rowx=4)

    # print "\nDATES:"
    # print "Type of data in cell (row 1, col 0):",
    # print sheet.cell_type(1, 0)
    # exceltime = sheet.cell_value(1, 0)
    # print "Time in Excel format:",
    # print exceltime
    # print "Convert time to a Python datetime tuple, from the Excel float:",
    # print xlrd.xldate_as_tuple(exceltime, 0)

    data = {
        'maxtime': (0, 0, 0, 0, 0, 0),
        'maxvalue': 0,
        'mintime': (0, 0, 0, 0, 0, 0),
        'minvalue': 0,
        'avgcoast': 0
    }
    coast_values_in_col = sheet.col_values(1, start_rowx=1, end_rowx=sheet.nrows)
    enumerated_coast_values = enumerate(coast_values_in_col)

    max_index = 0
    max_value = 0
    for i in enumerated_coast_values:
        _index, _value = i
        if _value > max_value:
            max_value = _value
            max_index = int(_index) + 1  # add the title line
    data['maxvalue'] = max_value
    data['maxtime'] = xlrd.xldate_as_tuple(sheet.cell_value(max_index, 0), 0)

    enumerated_coast_values = enumerate(coast_values_in_col)  # enumerated data can be used only once?
    min_index = 0
    min_value = max_value
    for i in enumerated_coast_values:
        _index, _value = i
        if _value < min_value:
            min_value = _value
            min_index = int(_index) + 1  # add the title line

    data['minvalue'] = min_value
    data['mintime'] = xlrd.xldate_as_tuple(sheet.cell_value(min_index, 0), 0)

    data['avgcoast'] = sum(coast_values_in_col) / (sheet.nrows - 1)  # minuse the title line

    return data


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

    cv = sheet.col_values(1, start_rowx=1, end_rowx=None)

    maxval = max(cv)
    minval = min(cv)

    maxpos = cv.index(maxval) + 1
    minpos = cv.index(minval) + 1

    maxtime = sheet.cell_value(maxpos, 0)
    realmaxtime = xlrd.xldate_as_tuple(maxtime, 0)
    mintime = sheet.cell_value(minpos, 0)
    realmintime = xlrd.xldate_as_tuple(mintime, 0)

    data = {
        'maxtime': realmaxtime,
        'maxvalue': maxval,
        'mintime': realmintime,
        'minvalue': minval,
        'avgcoast': sum(cv) / float(len(cv))
    }


def test():
    # open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()
