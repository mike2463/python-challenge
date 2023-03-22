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
#open csv file and create variables that will store data as the average P/L is being calculated
with open(budget_data,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    firstrow = next(csvreader)
    prevnet = int(firstrow[1])
    monthcount = monthcount + 1
    total  += prevnet
#convert csvreader to a stored list
    budgetlist = list(csvreader)
   
#Loop through budgetlist to find the total months, net total amount, changes in P/L and average of P/L, the greatest increase/decrease
    for row in budgetlist:
        monthcount = monthcount + 1
        total += int(row[1])
        monthly_change = int(row[1]) - prevnet
        prevnet = int(row[1])
        monthly_change_list += [monthly_change]
    maxchange = max(monthly_change_list)
    minchange = min(monthly_change_list)
    maax = monthly_change_list.index(maxchange)
    miin = monthly_change_list.index(minchange)
    net_monthly_avg = sum(monthly_change_list)/len(monthly_change_list)
#print all of the calculations   
    print('Total Months:', monthcount)
    print('Total Profits/Losses:', total)
    print('Changes in P/L:', sum(monthly_change_list))
    print('Average P/L:', net_monthly_avg )
    print('Greatest increase:',budgetlist[maax-1][0], maxchange)
    print('Greatest Decrease:', budgetlist[miin-1][0], minchange)
    

#write the report to a text file. 
results.write(f'Financial Analysis\n---------------\n')
results.write(f'Profit: ${total}\n')
results.write(f'Total Months: {monthcount}\n')
results.write(f'Average P/L: ${net_monthly_avg}\n')
results.write(f'Greatest Increase in Profits: ${budgetlist[maax-1][0]} {maxchange}\n')
results.write(f'Greatest Decrease in profits: ${budgetlist[miin-1][0]} {minchange}')
        

    
    
    
        

    
    
    

 


    
    
    