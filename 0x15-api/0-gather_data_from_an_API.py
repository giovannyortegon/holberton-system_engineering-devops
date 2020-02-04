#!/usr/bin/python3
""" Imports """
from requests import get
from sys import argv


def main(value):
    """ Python script that, using this REST API,
        for a given employee ID, returns information
        about his/her TODO list progress.
    """
    data_1 = {'userId': value[1]}
    url_1 = 'https://jsonplaceholder.typicode.com/todos'

    req_1 = get(url_1, params=data_1)
    resp_1 = req_1.json()

    data_2 = {'id': value[1]}
    url_2 = 'https://jsonplaceholder.typicode.com/users'
    req_2 = get(url_2, params=data_2)
    resp_2 = req_2.json()
    tasks = []

    for task in resp_1:
        if task.get('completed') is True:
            tasks.append(task)

    print('Employee {} is done with tasks({}/{}):'.format(
          resp_2[0].get('name'), len(tasks), len(resp_1)))
    if len(tasks) > 0:
        for title in tasks:
            print('\t {}'.format(title.get('title')))


if __name__ == '__main__':
    main(argv)
