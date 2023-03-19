import os
import csv

#Create empty variables
totalvotes = 0

candidate_list = []

#import csv file 
election_data = os.path.join('Resources', 'election_data.csv')

#Open a text document
results = open('results.txt', 'w')

#open csv file and create variables that will store data as the average P/L is being calculated
with open(election_data,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
   
#convert csvreader to a stored list
    candidates = list(csvreader)
    
#Loop through candidates list to total the number of votes and then to create a list of candidates
    for row in candidates:
        totalvotes = totalvotes + 1
        candidate_list += [row[2]]
      
#Filter through the candidates list and create a list of each candidate
    charles_list = list(filter(lambda i: 'Charles Casper Stockham' in i, candidate_list))
    diana_list = list(filter(lambda i: 'Diana DeGette' in i, candidate_list))
    raymon_list = list(filter(lambda i: 'Raymon Anthony Doane' in i, candidate_list))

#Find the total number of votes for each candidate based on the length of the list for each candidate
    charles = len(charles_list)
    diana = len(diana_list)
    raymon = len(raymon_list)

#Calculate the the percentage for each candidate
    percent_charles = round((charles/totalvotes)*100, 3)
    percent_diana = round((diana/totalvotes)*100, 3)
    percent_raymon = round((raymon/totalvotes)*100, 3)

#Create dictionary with the results of candidate
    election_results = {'Charles': percent_charles, 'Diana': percent_diana, 'Raymon': percent_raymon}

#Create a new variable that stores the winner of the election by using the election_results dictionary and the max function 
    winner = max(election_results, key=election_results.get)
        
#print all of the results   
    print(totalvotes)
    print(percent_charles, charles)
    print(percent_diana, diana)
    print(percent_raymon, raymon)
    print(winner)

#write the report to a text file. 
    results.write(f'Election Results\n-------------\n')
    results.write(f'Total Votes: {totalvotes}\n--------------\n')
    results.write(f'Charles Casper Stockham: {percent_charles}% ({charles})\n')
    results.write(f'Diana DeGette: {percent_diana}% ({diana})\n')
    results.write(f'Raymon Anthony Doane: {percent_raymon}% ({raymon})\n--------------\n')
    results.write(f'Winner: {winner}\n-----------------\n') 

    
    
    
        

    
    
    

 


    
    
    