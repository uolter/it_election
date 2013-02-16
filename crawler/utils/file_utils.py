__author__ = 'uolter'

import csv

def read_csv(file_name, normalize = False):

    data_set = []

    with open( file_name, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            # normalize numeric value
            new_row= []
            for v in row:
                if v.isdigit() and normalize:
                    new_row.append(float(v))
                else:
                    new_row.append(v)

            data_set.append(new_row)

    return data_set


def save_csv(file_name, data):

    writer = csv.writer(open(file_name, 'w'), delimiter=';')

    for row in data:
        writer.writerow(row)
