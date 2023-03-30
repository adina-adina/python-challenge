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

        # calculate the change in profit compared to the previous month
        profit_change += int(row[1]) - prev_profit
        prev_profit = int(row[1])

        # add the profit change to a list
        profit_change_list.append(profit_change)

        # check if the profit change is the greatest or decrease
        if profit_change > greatest_increase
            greatest_increase = profit_change
            greatest_increase_month = row [0]       
        elif profit_change < greatest_decrease:
            greatest_decrease = profit_change
            greatest_decrease_month = row[0]                        
