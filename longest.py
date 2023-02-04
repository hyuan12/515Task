#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 17:59:54 2023

@author: whale
"""

def longest_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        max_length = max(map(len, lines))
        return [line.strip() for line in lines if len(line) == max_length]
