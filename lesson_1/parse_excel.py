import xlrd
import sys

datafile = "c:\\Users\\zieft\\Dropbox\\PyCharmProjects_WIN\\MongoDB\\lesson_1\\native_Load_2016.xlsx"


def parse_file(datafile, r=2, c=3, start_rowx=1, end_rowx=3):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    data = [[sheet.cell_value(r, col)
             for col in range(sheet.ncols)]
            for r in range(sheet.nrows)]

    print "\nList Comprehension"
    print "data[{}][{}]:".format(r, c),
    print data[r][c]

    print "\nCells in a nested loop:"
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            if row == 50:
                print sheet.cell_value(row, col),

    ### other useful methods:
    print "\nROWS, COLUMNS, and CELLS:"
    print "Number of rows in the sheet:",
    print sheet.nrows
    print "Type of data in cell (row {}, col {}):".format(r, c),
    print sheet.cell_type(r, c)
    print "Value in cell (row {}, col {}):".format(r, c),
    print sheet.cell_value(r, c)
    print "Get a slice of values in column {}, from rows {}-{}:".format(c, start_rowx, end_rowx)
    print sheet.col_values(c, start_rowx, end_rowx)

    print "\nDATES:"
    print "Type of data in cell (row 1, col 0):",
    print sheet.cell_type(1, 0)
    exceltime = sheet.cell_value(1, 0)
    print "Time in Excel format:",
    print exceltime
    print "Convert time to a Python datetime tuple, from the Excel float:",
    print xlrd.xldate_as_tuple(exceltime, 0)

    return data


data = parse_file(datafile)
