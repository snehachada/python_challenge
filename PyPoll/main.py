import os
import csv
path = "Resources/election_data.csv"
with open(path) as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    data = [row for row in csvreader]
candidates = {}
# Total
total_votes = len(data)
print(total_votes)
# List of candidates
candidate_votes = []
for row in data:
    candidate_votes.append(row[2])
unique_candidates = set(candidate_votes)
for candidate in unique_candidates:
    candidates[candidate] = 0
# Total votes per candidate
for vote in candidate_votes:
    candidates[vote] += 1
print(candidates)
# Vote percentage for each candidate
percentage_votes = {}
for candidate in unique_candidates:
    vote_count = candidates[candidate]
    percentage_votes[candidate] = int(round(vote_count/total_votes * 100, 0))
print(percentage_votes)
# Winner (most votes)
winner_name = ""
winner_votes = 0
winner_pct = 0
for key, value in candidates.items():
    if value > winner_votes:
        winner_votes = value
        winner_name = key
        winner_pct = percentage_votes[key]
print("Election Results")
print("---------------------")
print(f"Total Votes: {total_votes}")
print("---------------------")
for w in sorted(candidates, key=candidates.get, reverse=True):
    print(f"{w}: {percentage_votes[w]}% ({candidates[w]})")
print("---------------------")
print(f"{winner_name} IS THE WINNER!")

PyPoll = open("Analysis/output_PyPoll.txt", "w")
print("Election Results", file=PyPoll)
print("---------------------", file=PyPoll)
print(f"Total Votes: {total_votes}", file=PyPoll)
print("---------------------", file=PyPoll)
for w in sorted(candidates, key=candidates.get, reverse=True):
    print(f"{w}: {percentage_votes[w]}% ({candidates[w]})", file=PyPoll)
print("---------------------", file=PyPoll)
print(f"{winner_name} IS THE WINNER!", file=PyPoll)
PyPoll.close