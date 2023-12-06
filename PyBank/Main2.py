from typing_extensions import Concatenate
import os
import csv


budget_csv = "budget_data.csv"
column_index = 1
column_index2 = 0
  
PL_List = []
Date_List = []

file =  "analysis.txt"
with open(budget_csv, 'r') as csvfile:
  csvreader = csv.reader(csvfile)
  header = next(csvreader)
  #print(header)
  for row in csvreader: 
    PL_List.append(int(row[column_index]))
    Date_List.append(row[column_index2])  


  
print("Financial Analysis")

#List to store data
column_data =[]
num_mths = 0 
sum_list = 0
total_net_amt = 0
total_avg = 0




num_mths = len(Date_List)
print("Total Months:" , (num_mths))


# the net Total of profit/ losses: over the entier period
#for i in PL_List:
  #total_net_amt += int(i)
total_net_amt =sum(PL_List)
print("Total:", (total_net_amt))

# the greatest increase the profit (date and amount) over the entire period
#difference = 0
#difference_list = []
#count = 0 
#i = 0
#j = 1

#for i in range(len(PL_List)):
  #for j in range(i + 1, len(PL_List)):
    #difference = int(PL_List [j]) - int (PL_List[i])
    #difference_list.append([i])
    #i = i + 1

#print(difference_list)


diff = [PL_List[i + 1] - PL_List[i] for i in range(len(PL_List) - 1)]
average_change = sum(diff) / len(diff)
print("Averge Change:" , average_change)



#the greatest increase in profit (date and amount over the entire period)
greatest_increase = max(diff)
greatest_increase_index = diff.index(greatest_increase)
greatest_increase_date =Date_List[greatest_increase_index + (1)]
print("Greatest Increase in Profits:" , greatest_increase_date, greatest_increase)




# the greatest decrease in profit (date and amount over the entire period)
greatest_decrease =min(diff)
greatest_decrease_index = diff.index(greatest_decrease)
greatest_decrease_date = Date_List[greatest_decrease_index + (1)]
print("Greatest Decrease in Profits:" , greatest_decrease_date, greatest_decrease)
