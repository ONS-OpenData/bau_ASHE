 # -*- coding: utf-8 -*-
"""
Spyder Editor

Basic reusable functions to help post-process data with Pandas.

Author: Mike
"""

import pandas as pd


# Dismiss command for unwanted items. Will remove all 8 relevant columns.
def dismiss(myframe, headers):
    
    for each in headers:
        Column1 = myframe.columns.get_loc(each)
        for x in range(1, 9):
            myframe = myframe.drop(myframe.columns[Column1], axis=1)
    return myframe
    
