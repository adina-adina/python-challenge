# modules
import os
import csv

# define file path
budget_csv = os.path.join("budget_data.csv")

# define variables
total_months = 0
total_profit = 0
greatest_increase = 0
greatest_decrease = 0
prev_profit = 0
profit_change_list = []

# Open and read the "budget_data" CSV file
with open(census_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip header row
    next(csvreader)

    # Loop through each row in "budget_data" and analyze data
    for row in csvreader:

        # count the total months
        total_months += 1

        # calculate the total profit
        total_profit += int(row[1])

        # calculate the total profit
        profit_change += int(row[1]) - prev_profit
        prev_profit = int(row[1])
                        
