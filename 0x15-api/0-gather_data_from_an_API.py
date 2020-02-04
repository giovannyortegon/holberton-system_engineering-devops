#!/usr/bin/python3
""" Imports """
from requests import get
from sys import argv


def main(value):
    """ Python script that, using this REST API,
        for a given employee ID, returns information
        about his/her TODO list progress.
    """
    data = {'userId': value[1]}

    url_1 = 'https://jsonplaceholder.typicode.com/todos'

    req_1 = get(url_1, params=data)
    resp_1 = req_1.json()

    url_2 = 'https://jsonplaceholder.typicode.com/users/{}'.format(value[1])
    req_2 = get(url_2)
    resp_2 = req_2.json().get('name')
    tasks = []

    for task in resp_1:
        if task.get('completed') is True:
            tasks.append(task.get('title'))
    if resp_2 is not None:
        print('Employee {} is done with tasks({}/{}):'.format(
               resp_2, len(tasks), len(resp_1)))
        for title in tasks:
            print('\t {}'.format(title))


if __name__ == '__main__':
    main(argv)
