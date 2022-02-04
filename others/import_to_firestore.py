"""
MIT License

Copyright (c) 2019 Robin Cheptileh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Thanks to https://github.com/RobinCheptileh/simple-firestore-import for the awesome repository.
"""

# !/usr/bin/env python3

import os
import sys
import json

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def import_data(service_account_key_path, data_file, collection_name):
    try:
        cred = credentials.Certificate(service_account_key_path)
        firebase_admin.initialize_app(cred)

        db = firestore.client()

        data = get_data(data_file)
        check_data(data)

        doc_ref = db.collection(collection_name)
        for datum in data:
            doc_ref.add(datum)
            print(f"Added: {datum}")

    except Exception as error:
        print(f"\nERROR: {error}")
    else:
        print("\nImport complete")


def check_data(data):
    if isinstance(data, (list, tuple,)):
        for datum in data:
            if not isinstance(datum, (dict,)):
                raise ValueError(f"An object expected, got {datum}")
    else:
        raise ValueError(f"An array expected, got {data}")


def get_data(data_file):
    if os.path.splitext(data_file)[1].lower() == ".json":
        with open(data_file, "r") as read_file:
            return json.load(read_file)

    raise ValueError("Invalid file type. Allowed file type .json")


if __name__ == "__main__":
    try:
        if len(sys.argv) == 4:
            service_account_path = sys.argv[1]
            data_file_path = sys.argv[2]
            name_of_collection = sys.argv[3]
        else:
            service_account_path = input("Path to serviceAccountKey.json: ")
            data_file_path = input("Path to data file: ")
            name_of_collection = input("Name of collection: ")

        import_data(service_account_path, data_file_path, name_of_collection)
    except KeyboardInterrupt as keyboard_error:
        print("\nProcess interrupted")
    finally:
        print("\nGood Bye!")
