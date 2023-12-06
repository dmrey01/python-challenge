from typing_extensions import Concatenate
import os
import csv


election_csv = "election_data.csv"
column_index = 0
column_index1 = 1
column_index2 = 2
  
Voter_ID = []
County = []
Candidate = []

file =  "analysis.txt"
with open(election_csv, 'r') as csvfile:
  csvreader = csv.reader(csvfile)
  header = next(csvreader)
  #print(header)
  for row in csvreader: 
    Voter_ID.append((row[column_index]))
    County.append(row[column_index1])
    Candidate.append(row[column_index2])  




#list to store data
candidate_vote_counts = []
candidate_name_list = []
can_counter0 = 0
can_counter1 =0
can_counter2 =0
i=0

print("Election Results")
print("----------------------")

#total number of votes cast
num_votes = len(Voter_ID)
print("Total Votes:" , (num_votes))

#compile a list of candiates 
candidate_name_list = list(set(Candidate))
print(candidate_name_list)


for i in range(len(Candidate)): 
  if Candidate[i] == candidate_name_list [0]:
    can_counter0 += 1
  elif Candidate[i] == candidate_name_list [1]:
    can_counter1 += 1
  elif Candidate[i] == candidate_name_list [2]:
    can_counter2 += 1

 
print(f"{candidate_name_list[0]}: {(can_counter0 / num_votes) *100:.2f}%" , can_counter0) 
print(f"{candidate_name_list[1]}: {(can_counter1 / num_votes) *100:.2f}%" , can_counter1)
print(f"{candidate_name_list[2]}: {(can_counter2 / num_votes) *100:.2f}%" , can_counter2)




print(f"winner" , (candidate_name_list[0]))
