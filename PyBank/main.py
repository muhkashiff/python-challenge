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
    avgChange=0
    profits=[]
    change=[] 
    #count the number of months
    for row in csvreader:
        monthCount=monthCount+1
    #count net profit/loss
        netPl=int(row[1])
        profit_loss += netPl
        value= int(row[1])
    #find average change
        profits.append(value)
    #chat gpt search for finding differnece in consecutive row within column    
    
    for x in profits:
        
        for i in range(1, len(profits)):
            chng=profits[i]-profits[i-1]
            change.append(chng)
            
    #average change calculation reference from class room exercise
    length = len(change)
    totalc = 0.0
    for x in change:
        totalc += x
        avgChange= totalc / length
        roundavg=round(avgChange,2)
    
# Track greatest decrease or increase
                
    greatest_decrease=min(change)
    greatest_increase=max(change)
# getting values of all variable

Total_month=print(monthCount)
Net_profit_loss=print(profit_loss)
print(roundavg)
print(greatest_increase)
print(greatest_decrease)

# Financial Analysis   
name="Financial Analysis"
Title=name.title() 
print(Title)
print("---------------------------")
print(f"Total months:{monthCount}")
print(f"Total: {profit_loss}")
print(f'Average Change: {roundavg}')
print(f'Greatest Increase in Profits: {greatest_increase}')
print(f'Greatest Decrease in Profits: {greatest_decrease}')