#!/usr/bin/python3
"""This function appends to a json file"""
import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
s = load_from_json_file('add_item.json')
s += sys.argv
save_to_json_file(s, 'add_item.json')
