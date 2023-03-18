import os
import csv

#Create empty variables
monthcount = 0
total = 0
totalsum =0
monthly_change_list = []

#import csv file 
budget_data = os.path.join('Resources', 'budget_data.csv')

results = open('results.txt', 'w')
#open csv file
with open(budget_data,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    firstrow = next(csvreader)
    prevnet = int(firstrow[1])
    monthcount = monthcount + 1
    total  += prevnet
#convert csvreader to a stored list
    budgetlist = list(csvreader)
   
#Loop through
    for row in budgetlist:
        monthcount = monthcount + 1
        total += int(row[1])
        monthly_change = prevnet - int(row[1])
        prevnet = int(row[1])
        monthly_change_list += [monthly_change]
        maxchange = max(budgetlist)
        minchange = min(budgetlist)
    net_monthly_avg = sum(monthly_change_list)/len(monthly_change_list)
    
    print('Total Months:', monthcount)
    print('Total Profits/Losses:', total)
    print('Changes in P/L:', sum(monthly_change_list))
    print('Average P/L:', net_monthly_avg )
    print('Greatest increase:', maxchange)
    print('Greatest Decrease:', minchange)

results.write(f'Financial Analysis\n---------------\n')
results.write(f'Profit: ${total}\n')
results.write(f'Total Months: {monthcount}\n')
results.write(f'Average P/L: ${net_monthly_avg}\n')
results.write(f'Greatest Increase in Profits: ${maxchange}\n')
results.write(f'Greatest Decrease in profits: ${minchange}')
        

    
    
    
        

    
    
    

 


    
    
    