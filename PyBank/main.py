import os
import csv

#import csv file 
monthcount = 0
total = 0
ltotal = 0
ptotal = 0
budget_data = os.path.join('Resources', 'budget_data.csv')

with open(budget_data,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    budgetlist = list(csvreader)
    #print(budgetlist)
    for row in budgetlist:
        monthcount = monthcount + 1
        total += int(row[1])
        avg = total/monthcount
        if int(row[1]) < 0:
            ltotal += int(row[1])
        if int(row[1]) > 0:
            ptotal += int(row[1])
        pchange = ((ptotal-total)/total)*100
        lchange = ((ltotal - total)/total)*100
        ttchange = ((pchange - lchange)/lchange)*100
    print('Total Months:', monthcount)
    print('Total Profits/Losses:', total)
    print('Average of P/L:', avg)
    print('Losses Total:', ltotal)
    print('Profit Total:', ptotal)
    print('Profit Change:', pchange)
    print('Losses Change:', lchange)
    print('Total Change:', ttchange)
    
    
 


    
    
    