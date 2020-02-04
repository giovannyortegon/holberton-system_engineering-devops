#!/usr/bin/python3
""" Imports """
from requests import get
from sys import argv
from json import dump


def main(value):
    """ Python script to export data in the JSON format.
    """
    # Todos
    url_1 = 'https://jsonplaceholder.typicode.com/todos'
    data_1 = {'userId': value[1]}
    req_1 = get(url_1, params=data_1)
    # Users
    url_2 = 'https://jsonplaceholder.typicode.com/users'
    data_2 = {'id': value[1]}
    req_2 = get(url_2, params=data_2)

    resp_1 = req_1.json()
    resp_2 = req_2.json()

    tasks = []

    for task in resp_1:
        all_task = {}
        all_task.update({'task': task.get('title')})
        all_task.update({'completed': task.get('completed')})
        all_task.update({'username': resp_2[0].get('username')})
        tasks.append(all_task)

    objs = {}
    objs.update({value[1]: tasks})

    file_name = "{}.json".format(value[1])

    with open(file_name, 'w') as json_file:
        dump(objs, json_file)


if __name__ == '__main__':
    main(argv)
