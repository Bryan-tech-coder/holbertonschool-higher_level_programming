#!/usr/bin/env python3
"""Module that converts CSV data to JSON format."""

import csv
import json


def convert_csv_to_json(filename):
    """
    Reads a CSV file and writes its contents as JSON to data.json.
    Returns True on success, False on failure.
    """
    try:
        data = []
        with open(filename, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)

        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True
    except Exception:
        return False
