import csv
import os

# define file path
poll_csv = os.path.join("election_data.csv")

# define variables
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# open and read "election_data.csv"
with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip header row
    next(csvreader)

    # loop through each row and analyze data
     for row in csvreader:

        # count total votes
        total_votes += 1
