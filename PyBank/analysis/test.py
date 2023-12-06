import os
import csv

budget_csv = os.path.join('..','Resources', 'budget_data.csv')

def get_column_data(file_path, column_index):
    PL_List = []
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        for row in csvreader:
            PL_List.append(row[column_index])
    return PL_List
file_path = os.path.join('..', 'Resources', 'budget_data.csv')
column_index = 1
profit_losses_data = get_column_data(file_path, column_index)
# Print the result
print(profit_losses_data)