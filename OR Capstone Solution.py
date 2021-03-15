# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 20:23:18 2021

@author: C21Elisha.Palm
"""

import pandas as pd
import datetime as dt
import numpy as np
import calendar

#df = pd.read_csv('data/mx_raw.csv')
df = pd.read_csv('mx_raw.csv')
pd.set_option('display.max_rows', df.shape[0]+1)
df.head()

# convert date column to datetime type
df.date = pd.to_datetime(df.date)


# Round avg duration to 2 decimal
df['Avg Duration'] = round(df['Avg Duration'], 2)

# Adding A column with Avg Duration in Mins
df['Avg Duration Mins'] = df['Avg Duration'] * 60

# find unique mx times
df['mx time'].unique()

# create the new date column by add the date and mx time columns
# convert mx time to hours
# create a list of our conditions
conditions = [
    (df['mx time'] == '2yr'),
    (df['mx time'] == 'Annual'),
    (df['mx time'] == 'Semi-Annual'),
    (df['mx time'] == 'Quarterly'),
    (df['mx time'] == 'Monthly'),
    (df['mx time'] == '2 Week'),
    (df['mx time'] == 'Weekly'),
    (df['mx time'] == 'Bi-Weekly'),
    (df['mx time'] == 'Daily')
    ]

# create a list of the values we want to assign for each condition
values = [17520,
          8760,
          4380,
          2190,
          730,
          336,
          168,
          84,
          24
         ]
#if mx
# create new date column
df['mx_due_date'] = df.date + pd.to_timedelta(np.select(conditions, values), unit='h')

# find today 
today = dt.date.today()

# slice all mx due next month or past due
next_month_mx = df.loc[(df.mx_due_date.dt.month == today.month + 1) | (df.mx_due_date < pd.to_datetime(today))]



# find sum of avg duration
tot_mx_hrs = sum(next_month_mx['Avg Duration'])

# Slice Daily Events
#df_daily = df.loc[df['mx time'] <= 8.97222, 'Priority Value'] = 1

# pd.to_datetime(today).weekday()
next_month = today.month + 1
year = today.year

weekdays = 0
weekends = 0
cal = calendar.Calendar()
hours_in_week = []
# iterate through weeks in month
# 12 days for pr1
# 9 days for pr2
# 3 days for pr3
# 3 days for pr 4
for week in cal.monthdayscalendar(year, next_month):
    for i, day in enumerate(week):
        # check if in month and weekend
        if day != 0 and i >= 5:
            weekends += 1
            hours_in_week.append(32)
        # check if in month and weekday
        elif day!= 0 and i < 5:  
            weekdays += 1
            hours_in_week.append(18)
tot_man_hrs = weekdays * 32 + weekends * 18
tot_man_hrs_4_guys = weekdays * 64 + weekends * 36
tot_man_hrs_5_guys = weekdays * 80 + weekends * 45


df1 = df.loc[df['Priority Number'] == 1]
df2 = df.loc[df['Priority Number'] == 2]
df3 = df.loc[df['Priority Number'] == 3]
df4 = df.loc[df['Priority Number'] == 4]
#dataframe = next_month_mx.loc[next_month_mx['Priority Number']==1,['Asset ID','Work ID', 'Asset Description', 'Event Name', 'mx time', 'mx_due_date', 'Avg Duration', 'Priority Number']].sort_values('Priority Number')
dataframe = df1[['Asset ID','Work ID', 'Asset Description', 'Event Name', 'mx time', 'mx_due_date', 'Avg Duration', 'Priority Number', 'KPR']]


# Python3 code for Dynamic Programming 
# based solution for 0-1 Knapsack problem 
  
# Prints the items which are put in a  
# knapsack of capacity W

def printknapSack(W, wt, val, n, day_jobs): 
    W = int(W)
    n = int(n)
    K = [[(0,'') for x in range(W + 1)] for x in range(n + 1)]
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = (0,'')
            elif wt[i-1][0] <= w:
                
                if val[i-1] + K[i-1][w-wt[i-1][0]][0] > K[i-1][w][0]:
                    K[i][w] = (val[i-1] + K[i-1][w-wt[i-1][0]][0],wt[i-1][1])
                    
                else:
                    K[i][w] = K[i-1][w]
                    
            else:
                K[i][w] = K[i-1][w]
    # stores the result of Knapsack 
    res = K[n][W][0]
    #print(res) 
      
    w = W 
    for i in range(n, 0, -1): 
        if res <= 0: 
            break
        # either the result comes from the 
        # top (K[i-1][w]) or from (val[i-1] 
        # + K[i-1] [w-wt[i-1]]) as in Knapsack 
        # table. If it comes from the latter 
        # one/ it means the item is included. 
        if res == K[i - 1][w][0]:
            continue
        else: 
  
            # This item is included. 
            #print(wt[i - 1])
            day_jobs.append(wt[i - 1])
            # Since this weight is included 
            # its value is deducted 
            res = res - val[i - 1] 
            w = w - wt[i - 1][0]
            

i =0 
last_len = 0
W = hours_in_week[i] * 1000
while len(hours_in_week) > i: # len(dataframe) > 0 and len(dataframe) != last_len or 
    last_len = len(dataframe)
    i +=1
    day_jobs = []
    val = []
    wt = []
    
    for index, row in dataframe.iterrows():
        clean = int(row['Avg Duration'] * 1000) 
        wt.append((clean,row['Work ID']))
        val.append(row['KPR'])
        
    
    W = hours_in_week[i] * 1000
    n = int(len(val))
    
    printknapSack(W,wt,val,n,day_jobs)
    
    value = 0
    
    for job in day_jobs:
        name = job[1]
        dataframe.drop(dataframe[dataframe['Work ID']==name].index, inplace = True)
    
    print(len(dataframe))
    print("finished day: " + str(i))

print(dataframe)