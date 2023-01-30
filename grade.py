#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 12:52:12 2023

@author: whale
"""

def calculate(number_grade):
    if 90 <= number_grade <= 100:
        return 'A'
    elif 80 <= number_grade < 90:
        return 'B'
    elif 70 <= number_grade < 80:
        return 'C'
    elif 60 <= number_grade < 70:
        return 'D'
    elif 0 <= number_grade < 60:
        return 'F'
    else:
        return 'N/A'