#!/bin/python3
import sys

def host_gather(file_name):
    with open(file_name) as inv:
        for line in inv.read().splitlines():
            if '.<something_common>.' in line:
                print(line)

def inv_file_getter():
    for arg in sys.argv[1:]:
        file_name = arg
        host_gather(file_name)

inv_file_getter()
