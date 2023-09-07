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
    dollarsign='$'
    dates=[] 
    changeMonth=[]
    date_to_find=[]
    #count the number of months
    for row in csvreader:
        monthCount=monthCount+1
    #count net profit/loss
        netPl=int(row[1])
        profit_loss += netPl
        value= int(row[1])
        date=str(row[0])
    #find average change
        profits.append(value)
        dates.append(date)
    #chat gpt search for finding differnece in consecutive row within column    
    
    for x in profits:
            for i in range(1, len(profits)):
                chng=profits[i]-profits[i-1]
                change.append(chng)
                
    for i in dates:
                
    #average change calculation reference from class room exercise
        length = len(change)
        totalc = 0.0
        for x in change:
            totalc += x
            avgChange= totalc / length
            roundavg=round(avgChange,2)
        


# Track greatest decrease or increase
    greatest_increase=max(change)            
    greatest_decrease=min(change)
    # Reference chat gpt search for finding index
    date_index_increase=change.index(greatest_increase)
    date_index_decrease=change.index(greatest_decrease)
    # Reference chatgpt search tracking value based on index within column
    if 0<= int(date_index_increase+1)<len(dates):
         date_to_find_I=dates[int(date_index_increase+1)]
    if 0<= int(date_index_decrease+1)<len(dates):
         date_to_find_D=dates[int(date_index_decrease+1)]

# Financial Analysis   

name="Financial Analysis"
Title=name.title() 
print(Title)
print("---------------------------")
print(f"Total months:{monthCount}")
print(f"Total: {profit_loss}")
print(f'Average Change: {roundavg}')
print(f'Greatest Increase in Profits:{date_to_find_I} {dollarsign}{greatest_increase}')
print(f'Greatest Decrease in Profits:{date_to_find_D} {dollarsign}{greatest_decrease}')
# write output files
path=os.path.join("analysis","financial_analysis.txt")
with open(path, "w", newline='') as datafile:
    datafile.write("Financial Analysis\n")
    datafile.write("------------------\n")
    datafile.write(f"Total months:{monthCount}\n")
    datafile.write(f"Total: {profit_loss}\n")
    datafile.write(f"Average Change: {roundavg}\n")
    datafile.write(f"Greatest Increase in Profits:{date_to_find_I} {dollarsign}{greatest_increase}\n")
    datafile.write(f"Greatest Decrease in Profits:{date_to_find_D} {dollarsign}{greatest_decrease}\n")