#!/usr/bin/python3

import requests
from sys import argv

def main(value):
    
    data = {'userId': value}
    
    url = 'https://jsonplaceholder.typicode.com/todos' 

    req = request(url, params=data)
    resp = req.json()

    print(resp)


if __name__ == '__main__':
    main(argv[1])
