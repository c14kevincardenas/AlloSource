# -*- coding: utf-8 -*-
''' This reads a text file called mx_json.txt, formatted as json, into a Python
    dictionary. '''
    
import json
import datetime as dt
with open('mx_json.txt') as json_file:
    my_data = json.load(json_file)

i = 0
for key in my_data:
    i += 1
    print(my_data[key]['event'])
    if i == 5:
        break
mxtype =['Monthly', 'Quarterly', 'Semi-Annual', 'Annual', '2yr', 'Weekly', 'Daily'
         , '2 Week', 'Bi-Weekly']

# changing date string to datetime obj
o = 0
for asset, event_list in my_data.items():
    for eventdict in event_list:
        o += 1
        print(eventdict[0])
        if o ==5:
            break
#        print(dt.datetime.strptime(my_data[Asset][eventdescription])
    #my_var = dt.datetime.strptime(my_data[Asset][eventdescription][0]['date'], "%m/%d/%Y")
#my_var + dt.timedelta(days=90)

'''
for asset in my_data:
    if my_data[asset]['mx_kind'] == kind:
        if my_data[asset]['date']:
'''       
     
'''
for key in my_data:
    if my_data[key]['Priority Number'] == 1: # Schedule off of 40%
        for pri1 in my_data[key]['Event Priority']: # Implement Event Priority
            if pri1 == 1:
                #Schedule First
            elif pri1 == 2:
                #Schedule Second
            elif pri1 == 3:
                #Schedule third
            elif pri1 == 4:
                #Schedule Fourth
    elif my_data[key]['Priority Number'] == 2: # Schedule off of 30%
        for pri2 in my_data[key]['Event Priority']: # Implement Event Priority
            if pri2 == 1:
                #Schedule First
            elif pri2 == 2:
                #Schedule Second
            elif pri2 == 3:
                #Schedule third
            elif pri2 == 4:
                #Schedule Fourth
    elif my_data[key]['Priority Number'] == 3: # Schedule off 10%
        for pri3 in my_data[key]['Event Priority']: # Implement Event Priority
            if pri3 == 1:
                #Schedule First
            elif pri3 == 2:
                #Schedule Second
            elif pri3 == 3:
                #Schedule third
            elif pri3 == 4:
                #Schedule Fourth
    elif my_data[key]['Priority Number'] == 4: # Schedule off 10%
        for pri4 in my_data[key]['Event Priority']: # Implement Event Priority
            if pri4 == 1:
                #Schedule First
            elif pri4 == 2:
                #Schedule Second
            elif pri4 == 3:
                #Schedule third
            elif pri4 == 4:
                #Schedule Fourth
    else: # Schudule Random Events off 10%
'''