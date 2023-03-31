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

        # If the candidate is not in the dictionary, add them with one vote
        if row[2] not in candidates:
            candidates[row[2]] = 1
        # If the candidate is already in the dictionary, add one to their vote count
        else:
            candidates[row[2]] += 1

# print Total Votes
print("")
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# loop through each candidate in the dictionary
for candidate in candidates:

    # calculate vote percentage for each candidate
    vote_percentage = round((candidates[candidate] / total_votes) * 100, 3)

    # print candidate's name, vote percentage, and total number of votes
    print(f"{candidate}: {vote_percentage}% ({candidates[candidate]})")

    # find the winner
    if candidates[candidate] > max_votes:
        max_votes = candidates[candidate]
        winner = candidate

# print winner
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# define the file path for the results text file
output_file = os.path.join("election_results.txt")

# open the text analysis file in write mode
with open(output_file, "w") as file: