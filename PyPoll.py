# Add our dependencies
import csv
from distutils import text_file
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
    # Winning candidate and Winning Count Tracker
    winning_candidate = ''
    winning_count = 0
    winning_percentage = 0
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

# Save the results to our text file.
with open(file_to_save, 'w') as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
         f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end='')
    # After printing the final vote count to the terminal save the fianl vote count to the text file
    txt_file.write(election_results)
    #Calculate percentage of votes per candiate via looping through the counts.
    # 1 Iterate through the candiate list.
    for candidate_name in candidate_votes:
        # 2 Retrieve vote count of a candiate.
        votes = candidate_votes[candidate_name]
        # 3 Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count and candidate
        # 1 Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2 If true then set the winning_count = votes and winning_percentage = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 3 Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
    # Print the winning canidate's results to the terminal.    
    winning_candidate_summary = (
        f'-------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'-------------------------\n')
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    text_file.write(winning_candidate_summary)
