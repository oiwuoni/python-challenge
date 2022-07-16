import os
import csv

total_votes = 0
winning_count = 0
candidates_list = []
candidate_votes = {}


election_data_csv = os.path.join('Resources', 'election_data.csv')
with open (election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    header_row = next(csvfile)

    for row in csvreader:
        candidate_name = row[2]
        total_votes = total_votes + 1
        if candidate_name not in candidates_list:
            candidates_list.append(candidate_name)
            candidate_votes[candidate_name] = 0
    
        candidate_votes[candidate_name] += 1


print(total_votes)
for candidate_name, votes in candidate_votes.items():
    print(f"{candidate_name} \n {votes}")
    vote_percentage = votes / total_votes
    vote_percentage_formatted = "{:.3%}".format(vote_percentage)
    print(vote_percentage_formatted)
    winning_count = max(candidate_votes)
print(winning_count)

    

    