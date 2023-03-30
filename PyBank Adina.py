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
profit_change = 0
profit_change_list = []

# Open and read the "budget_data" CSV file
with open(budget_csv, newline="") as csvfile:
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

        # check if the profit change is the greatest or decrease
        if profit_change > greatest_increase:
            greatest_increase = profit_change
            greatest_increase_month = row [0]       
        elif profit_change < greatest_decrease:
            greatest_decrease = profit_change
            greatest_decrease_month = row[0]  

        # add the profit change to a list
        profit_change_list.append(profit_change)

        # reset profit_change for next loop
        profit_change = 0
                      


# calculate the average profit change
average_profit_change = sum(profit_change_list[1:]) / len(profit_change_list[1:])

# print the analysis to the console
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${round(average_profit_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# define the file path for the analysis text file
output_file = os.path.join("budget_analysis_results.txt")

# open the text analysis file in write mode
with open(output_file, "w") as file:

    # write the analysis to the output text file
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit}\n")
    file.write(f"Average Change: ${round(average_profit_change, 2)}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")

# confirm the file export in the console
print(f"The analysis has been exported to {output_file}.")