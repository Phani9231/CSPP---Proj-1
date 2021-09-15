"""Implementing the wc shell command in python."""

"""We are importing sys module"""

import sys

"""we are importing only the required files i.e wc and readfile from a different file in same directory i.e lib.helper in our case."""

from lib.helper import wc, readfile

"""Initialising the TEXT variable with null value"""

TEXT = None

"""Initializing a variable ARG_CNT with a length function which calculates the length of the argument given in command line and reduces it by 1"""

ARG_CNT = len(sys.argv) - 1

"""condition : if value of ARG_CNT == 0 a TEXT variable is initialised with a input function using sys library and reads the file"""

if ARG_CNT == 0:
    TEXT = sys.stdin.read()

"""condition : if value of ARG_CNT == 1 a variable named filename is initialised and the filename is stored in it, then a new variable named TEXT is used to store a function call operation to return value"""  

if ARG_CNT == 1:
    filename = sys.argv[1]
    TEXT = readfile(filename)

""" wc function is called using TEXT variable as its argument and stored in the response variable """

response = wc(TEXT)

"""All the responses are concatenated using spaces and print together using print function"""

print(" " + str(response[0]) + "  " + str(response[1]) + " " + str(response[2]))