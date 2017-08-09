#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name", help="Enter your name")
parser.add_argument("age", help="Enter your age")
args=parser.parse_args()
my_name = args.name
my_age = args.age
print my_name
print my_age

age = input("Please enter your age: ")
print age