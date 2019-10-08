#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:19:58 2019

@author: shreevathsa
"""

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next week, " + magician.title() + ".\n")
    
print("Thank you, everyone. That was a great show!")