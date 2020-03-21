# This Python is to perform the financial analysis on the bank budget data
# Importing the needed libraries
import os
import csv
import sys

# Assigning the path for the budget_data.csv file
budget_csv_path = os.path.join("..", "Resources", "budget_data.csv")

# Assigning the needs variables and dictionaries
No_Of_Months=0
Total_Change_Amount=0
Change_Dict={}

# Reading the CSV file and writing it to a dictionary
with open(budget_csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        Month=row[0]
        if Month!="":
            curr_Dict={No_Of_Months:[row[0],row[1]]}
            Change_Dict.update(curr_Dict)
            No_Of_Months=No_Of_Months+1

# Setting the length of the dictionary
Dictlen=len(Change_Dict)

# Defining the needed function to calculate the amount changes
def funamountchange(startvalue,nextvalue):
    return(float(nextvalue)-float(startvalue))

# Reading from the dictionary and appending the amount changes 
for i in range(len(Change_Dict)):
     if i< Dictlen-1:
         AmountChange=funamountchange(Change_Dict[i][1],Change_Dict[i+1][1])
         Change_Dict[i+1].append(AmountChange)
     if i==0:
         Change_Dict[i].append(0)

# Assining the needed variables to calculate the output values
SumAmount=0
SumChangedAmount=0
Greatest_Increase=0
Greatest_Decrease=0

# Reading from the dictionary to calculate the Average change, Greatest increase and decrease
for i in range(len(Change_Dict)):
     SumAmount=SumAmount+float(Change_Dict[i][1])
     SumChangedAmount=SumChangedAmount+float(Change_Dict[i][2])
     if Change_Dict[i][2] > Greatest_Increase:
         Greatest_Increase=Change_Dict[i][2]
         Greatest_Increase_Month=Change_Dict[i][0]
     if Change_Dict[i][2] < Greatest_Decrease:
         Greatest_Decrease=Change_Dict[i][2]
         Greatest_Decrease_Month=Change_Dict[i][0]

# Final output Calculations
Total_Months=len(Change_Dict)
Total=SumAmount
Average_Change=round(SumChangedAmount/(len(Change_Dict)-1),2)

# Printing the output to the terminal

print('Financial Analysis')
print('------------------')
print('Total Months:',Total_Months)
print('Total:',Total)
print('Average Change:', Average_Change)
print(f"Greatest Increase in Profits: {Greatest_Increase_Month} ({Greatest_Increase})")
print(f"Greatest Decrease in Profits: {Greatest_Decrease_Month} ({Greatest_Decrease})")

# Redirecting the output to a file

with open('PyBankFinancialnalysis.txt', 'w') as f:
     print('Financial Analysis', file=f)
     print('------------------', file=f)
     print('Total Months:',Total_Months, file=f)
     print('Total:',Total, file=f)
     print('Average Change:', Average_Change, file=f)
     print(f"Greatest Increase in Profits: {Greatest_Increase_Month} ({Greatest_Increase})",file=f)
     print(f"Greatest Decrease in Profits: {Greatest_Decrease_Month} ({Greatest_Decrease})",file=f)
