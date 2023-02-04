#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 11:47:25 2023

@author: whale
"""

strs = input().split()
numbers = list(map(int, strs))
sum_of_positives = sum(x for x in numbers if x > 0)
print(sum_of_positives)

