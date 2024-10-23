# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won - total #vote per candidate/ total votes of all Candidates
# 4. The total number votes each cadidate won
# 5. The winner of the election based on popular vote.


# Import the datetime class from the datetime module.
import csv
import os


# Initiation File to read and file to Save
file_to_load = os.path.join("Resources","election_results.csv") 
file_to_save = os.path.join("analysis", "election_analysis_test.txt")

total_vote= 0

candidate_options = []
candidate_votes = {}

winning_count= 0
wiining_percentage = 0
winning_candidate = ""

# Opening File

with open(file_to_load) as file_data:
    # File store data as a list of lists
    file_reader = csv.reader(file_data)
    #Skip to header of the data
    header = next(file_reader)
    # print(header)
    
    #Iterate over the list and tally total votes
    for row in file_reader:
        total_vote+=1
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] +=1
    
    with open(file_to_save, "w") as txt_file:
        election_result = (
            f"Election Results\n"
            f"----------------------------------\n" 
            f"Total Votes: {total_vote:,}\n"
            f"----------------------------------\n" 

        )
        txt_file.write(election_result)

        for candidate_name in candidate_votes:
            votes = candidate_votes[candidate_name]
            votes_percentage = float(votes)/float(total_vote)*100
            
            canditate_result = (f"{candidate_name}: {votes_percentage:.1f} ({votes:,})\n")
            txt_file.write(canditate_result)
            if votes > winning_count:
                winning_count = votes
                winning_candidate = candidate_name
                wiining_percentage = votes_percentage

        winning_candidate_result = (
            f"----------------------------------\n" 
            f"Winner: {winning_candidate} \n"
            f"Winning Vote Count: {winning_count:,} \n"
            f"Winning Percentage: {wiining_percentage:.1f}% \n"
            f"----------------------------------\n" 

        ) 

        txt_file.write(winning_candidate_result)





