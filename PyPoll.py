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
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Opening File

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    
    
    
    
    # with open(file_to_save, 'a') as save_file:
    #     for row in file_reader: 
    #         save_file.write(row[1])
        







