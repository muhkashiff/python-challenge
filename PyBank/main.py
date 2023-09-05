#import modules
import os
import csv
#import files path
csvpath = os.path.join('Resources','budget_data.csv')
#read csv file with open command
with open(csvpath,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    #skip the header
    header= next(csvreader)
    #list of variable 
    monthCount=0
    profit_loss=0
    column_index=1
    profits=[]
    losses=[]
    greatest_decrease= ''
    greatest_increase= ''
    
    
    for row in csvreader:
        monthCount=monthCount+1
    #count net profit/loss
        netPl=int(row[1])
        profit_loss += netPl
   
        split_pl=row[1].split(',')
        value= int(row[1])
    #average change #chatgpt code search...split profit loss within column
        if value >= 0:
            profits.append(value)
        else:losses.append(value)
    for x in profits:
    #     print(x)
        for y in losses:
    #     print(y)
# Track greatest decrease or increase
                
            greatest_decrease=min(losses)
            greatest_increase=max(profits)
# Total number of Months
    

Total_month=print(monthCount)
Net_profit_loss=print(profit_loss)

print(greatest_decrease)
print(greatest_increase)
