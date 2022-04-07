# Add our dependencies
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join('Resources','election_results.csv')
# Assign a variable to save the file to a path.
file_to_save = os.path.join('analysis', 'election_analysis.txt')
# Assign a total vote counter to 0.
total_votes = 0
# Declare new candidate options.
candidate_options = []
# Declare empty candidate vote count dictionary.
candidate_votes = {}
# Open the election results.
with open(file_to_load) as election_data: 
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
         # Increase total votes   
        total_votes += 1
        # Print the candidate name for each row
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add next vote to that candidate's count.
        candidate_votes[candidate_name] += 1
# Print the candidate vote dictionary.
print(candidate_votes)

#Calculate percentage of votes per candiate via looping through the counts.
# 1 Iterate through the candiate list.
for candidate_name in candidate_votes:
    # 2 Retrieve vote count of a candiate.
    votes = candidate_votes[candidate_name]
    # 3 Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4 Print the candidate name and percentage of votes.
    print(f'{candidate_name}: recieved {vote_percentage}% of the vote.')

        # RETURN TO 3.5.5 TO CONTINUE

# The data we need to retrieve
# Find the total Votes cast
# Find and list all Candidates
# Find percentage of Votes cast per Candidate
# Find the total Votes cast per Candidate
# Find the winner based on Popular Vote