# -*- coding: utf-8 -*-
"""
Reads the most recent maintenace events from a csv into a dictionary.  Then
writes that dictionary to a text file in json format.
"""

import csv
import json

# Initialize variables
my_dict = {}
last_asset = ''

# Reads data from csv into a dictionary
with open('mx_raw (1).csv', newline='') as csvfile:
    myreader = csv.reader(csvfile, delimiter=',')
    next(myreader, None) # skips header row
    for row in myreader:
        if row[0] != last_asset:
            last_asset = row[0]
            my_dict[row[0]] = {'description': row[1],'Priority Number': row[10],
                                   'event':[{'work_id': row[2],
                                             'status': row[3],
                                             'event_id': row[4],
                                             'event_name': row[5],
                                             'duration': row[6],
                                             'date': row[7],
                                             'mx_type': row[8],
                                             'mx_kind': row[9]
                                             }]
                                  }
        else:
            my_dict[last_asset]['event'].append({'work_id': row[2],
                                                 'status': row[3],
                                                 'event_id': row[4],
                                                 'event_name': row[5],
                                                 'duration': row[6],
                                                 'date': row[7],
                                                 'mx_type': row[8],
                                                 'mx_kind': row[9]
                                                 })
#my_dict.pop('Closed') # deletes empty rows

# Writes dictionary to text file in json format
with open('mx_json.txt', 'w') as outfile:
    json.dump(my_dict, outfile)