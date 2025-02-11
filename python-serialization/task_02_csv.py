#!/usr/bin/python3
"""Converting CSV Data to JSON Format"""


import csv
import json


def convert_csv_to_json(csv_file):

    data = []
    try:
        with open(csv_file, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)

        with open('data.json', 'w', encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True

    except (FileNotFoundError, Exception) as e:
        print("Error: {}".format(e))
        return False
