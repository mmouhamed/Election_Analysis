import os
import csv
import collections


file_to_load = os.path.join("Resources", "election_results.csv")
total_vote = 0
candidate_name = []
total_candidate_name = []
candidate_votes = {}
winning_count = 0
winning_percentage = 0
winning_candidate = ""




with open(file_to_load) as file_data:
    file_reader = csv.reader(file_data)

    header = next(file_reader)

    for row in file_reader:
        total_vote += 1
        if row[2] not in candidate_name:
            candidate_name.append(row[2])
            candidate_votes[row[2]] = 0
        candidate_votes[row[2]] +=1

for candidate_name in candidate_votes:
    votes= candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_vote) * 100

    
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage


    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


# print(total_vote)
# print(candidate_name)
# print(candidate_votes)
print(f"Wining candidate is: {winning_candidate} Vote Count: {winning_count:,} Percentage: {winning_percentage:.1f}%")

