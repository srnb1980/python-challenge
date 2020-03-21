# This Python script is to perform the election analysis
# Importing the needed libraries
import os
import csv
import sys

# Assigning the path for the budget_data.csv file
election_csv_path = os.path.join("..", "Resources", "election_data.csv")

# Assigning the needs variables and dictionaries
voterid=0
No_Of_votes=0
election_Dict={}
summary_Dict={}
unique_contestant=[]

# Reading the CSV file and writing it to a dictionary and also finding unique contestants
with open(election_csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        voterid=row[0]
        if  voterid!="":           
            curr_Dict={No_Of_votes:[row[0],row[1],row[2]]}
            election_Dict.update(curr_Dict)
            No_Of_votes=No_Of_votes+1
        contestant=row[2]
        if contestant not in unique_contestant:
            unique_contestant.append(contestant)
# Setting the length of the dictionary
Dictlen=len(election_Dict)

# Defining the needed function to calculate the election percent
def funelectionpercent(individial_count,Total_Count):
    return(round(individial_count/Total_Count*100,0))

# Putting unique contestants in a dictionary
for i in unique_contestant:
    curr_Dict={i:[0]}
    summary_Dict.update(curr_Dict)

#Reading from the unique contestant dictionary and election dictionary to find number of votes and create summary dictionary
for i in range(len(unique_contestant)):
     for j in range(len(election_Dict)):
         if unique_contestant[i] == election_Dict[j][2]:
             count=int(summary_Dict[unique_contestant[i]][0])+1
             summary_Dict[unique_contestant[i]][0]=count

# Calculating the election percentages and appending to the summary dictionary

for i in summary_Dict:
     election_percent=funelectionpercent(summary_Dict[i][0],len(election_Dict))
     summary_Dict[i].append(election_percent)

Winning_Count=0

# finding the winner from the summary dictionary

for i in summary_Dict:
    if summary_Dict[i][0]>Winning_Count:
        Winner=i
        Winning_Count=summary_Dict[i][0]

# Printing the output to the terminal

print('Election Results')
print('-----------------------')
print('Total Votes:',Dictlen)
print('-----------------------')
for i in summary_Dict:
    print(f"{i}: {summary_Dict[i][1]}% ({summary_Dict[i][0]})")
print('-----------------------')
print(f"Winner: {Winner}")
print('-----------------------')

# Redirecting the output to a file

with open('PyPollElectionnalysis.txt', 'w') as f:
     print('Election Results',file=f)
     print('-----------------------',file=f)
     print(f"Total Votes: {Dictlen}",file=f)
     print('-----------------------',file=f)
     for i in summary_Dict:
         print(f"{i}: {summary_Dict[i][1]}% ({summary_Dict[i][0]})",file=f)
     print('-----------------------',file=f)
     print(f"Winner: {Winner}",file=f)
     print('-----------------------',file=f)