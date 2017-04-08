import math
import csv

def skip_lines(input_file, lines):
    pass

def is_number(v):
    pass

def ensure_float(v):
    if is_number(v):
        return float(v)


def audit_population_density(input_file):
    for row in input_file:
        population = ensure_float(row['populationTotal'])
        area = ensure_float(row['areaLand'])
        population_density = ensure_float(row['populationDensity'])
        if population and area and population_density:
            calculated_density = population / area
            if math.fabs(calculated_density - population_density) > 10:
                print "Passibly bad population density for", row['name']


if __name__ == '__main__':
    input_file = csv.DictReader(open('cities.csv'))
    skip_lines(input_file, 3)
    audit_population_density(input_file)
