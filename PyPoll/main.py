import csv
import os

#Locate CSV file
election_data = os.path.join('PyPoll','Resources','election_data.csv')

#Read CSV file
with open(election_data, 'r') as election_file:
    csvreader = csv.reader(election_file, delimiter=',')
    header = next(csvreader)
    all_data = [row for row in csvreader]
    
#Create a list for each column of all_data
ballot_data = [row[0] for row in all_data]
county_data = [row[1] for row in all_data]
candidate_data = [row[2] for row in all_data]
    
# The total number of votes cast
votes_cast = len(ballot_data)

# A complete list of candidates who received votes
candidates = sorted(set(candidate_data))

# The total number of votes each candidate won
c = 0
d = 0
r = 0
for candidate in candidate_data:
    if candidate == candidates[0]:
        c = c + 1
    elif candidate == candidates[1]:
        d = d + 1
    elif candidate == candidates[2]:
        r = r + 1
  
# The percentage of votes each candidate won
percentage_c = c / votes_cast * 100
percentage_d = d / votes_cast * 100
percentage_r = r / votes_cast * 100

# Idenifying the winner's name of the election based on popular vote
winner = ''
if c > d and c > r:
    winner = candidates[0]
if d > c and d > r:
    winner = candidates[1]
if r > c and r > d:
    winner = candidates[2]


#Results of calculations above
results = f"""\
Election Results
-------------------------
Total Votes: {votes_cast}
-------------------------
{candidates[0]}: {percentage_c:.3f}% ({c})
{candidates[1]}: {percentage_d:.3f}% ({d})
{candidates[2]}: {percentage_r:.3f}% ({r})
-------------------------
Winner: {winner}
-------------------------
"""
print(results)

#Create a new file path for text file of results
analysis_results = os.path.join('PyPoll','analysis','analysis_results.txt')

# Write the results
with open(analysis_results, 'w') as analysis_file:
    analysis_file.write(results)
