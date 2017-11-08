# -*- coding: utf-8 -*-
"""
Created on Wed Nov 08 13:43:24 2017

@author: LeeBaekHaeng
"""

import csv

#with open('components.csv', 'rb') as csvfile:
with open('csv_test.csv', 'rb') as csvfile:

    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    
    headers = spamreader.next()
    
    print('headers', headers)
    print('headers[0]', headers[0])
    
    for row in spamreader:
        
        print ', '.join(row)