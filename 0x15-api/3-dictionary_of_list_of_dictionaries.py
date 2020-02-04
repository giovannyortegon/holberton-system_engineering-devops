#!/usr/bin/python3
""" Imports """
from requests import get
from json import dump


def main():
    """ Python script to export data in the JSON format.
    """
    # Todos
    url_1 = 'https://jsonplaceholder.typicode.com/todos'
    req_1 = get(url_1)
    # Users
    url_2 = 'https://jsonplaceholder.typicode.com/users'
    req_2 = get(url_2)

    resp_1 = req_1.json()
    resp_2 = req_2.json()

    users = {}

    for user in resp_2:
        uname = user.get('username')
        all_users = []

        for task in resp_1:
            if task.get('userId') == user.get('id'):
                all_task = {}
                all_task.update({'username': uname})
                all_task.update({'task': task.get('title')})
                all_task.update({'completed': task.get('completed')})
                all_users.append(all_task)
        users.update({user.get('id'): all_users})

    with open('todo_all_employees.json', 'w') as json_file:
        dump(users, json_file)


if __name__ == '__main__':
    main()
