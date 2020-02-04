#!/usr/bin/python3
""" Imports """
from requests import get
from sys import argv
from csv import writer, QUOTE_ALL


def main(value):
    """ Script to export data in the CSV format.
    """
    url_1 = 'https://jsonplaceholder.typicode.com/todos'
    data = {'userId': value[1]}
    req_1 = get(url_1, params=data)

    url_2 = 'https://jsonplaceholder.typicode.com/users'
    data = {'id': value[1]}
    req_2 = get(url_2, params=data)

    resp_1 = req_1.json()
    resp_2 = req_2.json()

    file_name = "{}.csv".format(value[1])

    with open(file_name, 'w', newline='') as csv_file:
        csv_write = writer(csv_file, quoting=QUOTE_ALL)
        for task in resp_1:
            csv_write.writerow([int(value[1]), resp_2[0].get('username'),
                                task.get('completed'), task.get('title')])


if __name__ == '__main__':
    main(argv)
