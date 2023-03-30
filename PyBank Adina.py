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