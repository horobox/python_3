#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:11:14 2019

@author: shreevathsa
"""

tables = []
for value in range(1, 11):
    tables.append(value*3)
print(tables)

for value in range(1,11):
    print("3 X " + str(value) + " = " + str(tables[value-1]))

