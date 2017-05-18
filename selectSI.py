#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 14:01:49 2017

@author: stjohn

Takes a json file with census tracts for NYC and produces a new file with 
only Staten Island.
"""

import json

jsonData = open("CENSUS.json")
wholeCity = json.load(jsonData)

siFeatures = []

for item in wholeCity['features']:
    if item['properties']['BoroName'] == 'Staten Island':
        siFeatures.append(item)

wholeCity['features'] = siFeatures

with open('ctSI.json', 'w') as outfile:
    json.dump(wholeCity, outfile)