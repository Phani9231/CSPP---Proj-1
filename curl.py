"""The python code helps to read the command line input for curl method."""

"""We are importing sys module"""

import sys

"""we are importing only the required files i.e curl from a different file in same directory i.e lib.helper in our case."""

from lib.helper import curl

"""Initialising URL variable with null value"""

URL = None

"""Initializing a variable ARG_CNT with a length function which calculates the length of the argument given in command line and reduces it by 1"""

ARG_CNT = len(sys.argv) - 1

""" condition : if the value of ARG_CNT is not equal to 1 then the print statement is executed"""

if ARG_CNT != 1:
    print('Usage: curl [URL]...')

""" condition : if the value of ARG_CNT is equal to 1 then the user specified url is saved in the variable URL and enters the second if condition"""
""" condition : if the variable URL does not contain http then http:// is added to the contents of URL variable at the start """
"""the print statement here calls the curl function which further takes the variable URL as an argument"""
if ARG_CNT == 1:
    URL = sys.argv[1]
    if 'http' not in URL[:5]:
        URL = "http://"+URL
    print(curl(URL))
