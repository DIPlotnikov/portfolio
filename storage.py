#!/usr/bin/python3
# -*- coding: utf-8 -*-

# This program allows you to store information in the key/value format.
# Use the console. Request format: path...> python storage.py --key KEY --val VALUE
# To add a key and value, enter the key and value: path...> python storage.py --key KEY --val VALUE
# To get the value by key, enter only the key: path...> python storage.py --key KEY
# To clear the temporary storage, enter an empty query: path...> python storage.py

# D.Plotnikov 2021

import os
import tempfile
import argparse
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def get_data():
    if os.path.exists(storage_path):
        with open(storage_path, 'r') as data_base:
            raw_data = json.load(data_base)
            return raw_data
    else:
        return {}


def put(key, value):
    data = get_data()
    if key in data:
        data[key] = data[key], value
        with open(storage_path, 'w') as data_base:
            json.dump(data, data_base)
    else:
        with open(storage_path, 'w') as data_base:
            data[key] = value
            json.dump(data, data_base)


def read(key):
    data = get_data()
    if key in data:
        value = data[key]
        if type(value) == list:
            print(*data[key], sep=", ")
        else:
            print(data[key])
    else:
        print(None)


def clearn():
    os.remove(storage_path)


def storage():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', type=str, help='Key')
    parser.add_argument('--val', type=str, help='Value')
    args = parser.parse_args()

    if args.key and args.val:
        put(args.key, args.val)
    elif args.key:
        read(args.key)
    else:
        clearn()


if __name__ == "__main__":
    storage()
