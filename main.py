import csv
import os


os.path.join("...", "python-challenge","election_data.csv")

candidates = []
total_votes = 0

# opens up the csv and counts the total number of votes and appends all of the voters' candidate choices to a new list
#
with open('election_data.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader, None)
    for row in csv_reader:
        total_votes += 1
        candidates.append(row[2])


# takes the unique number of candidates and stores them as an alphabetically ordered list
#
unique_candidates = list(sorted(set(candidates)))

# vote_count is the vote for each unique candidate and these values will be stored in a list
#
vote_count = 0
unique_candidate_votes = []

# for every unique candidate, this block of code goes down the list of candidates and tallys up the
# votes for each unique candidate and appends them to a list. 
# 
for i in range(len(unique_candidates)):
    for candidate in candidates:
        if candidate == unique_candidates[i]:
            vote_count += 1
    unique_candidate_votes.append(vote_count)           
    vote_count = 0

# calculates the percent of votes each unique candidate got and adds it to a list
#
percent_votes = [round((x/total_votes)*100, 2) for x in unique_candidate_votes]

# zips up the data for each unique candidate and stores it in a list that is in descending order from most votes to least votes
#
results = sorted(list(zip(unique_candidates, unique_candidate_votes, percent_votes)),  key=lambda vote: vote[1], reverse = True)

# since results list in descending order by name, the first name in the list will be the winner
#
for a, b, c in results:
    winner = a
    break

print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')
for a, b, c in results:
    print (f'{a}: {c}%, ({b})')
print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')



with open('output.txt', 'w', newline='') as textfile:
    textfile.write('Election Results\n')
    textfile.write('-------------------------\n')
    textfile.write(f'Total Votes: {total_votes}\n')
    for a, b, c in results:
        textfile.write(f'{a}: {c}%, ({b})\n')
    textfile.write('-------------------------\n')
    textfile.write(f'Winner: {winner}\n')
    textfile.write('-------------------------\n')




##########################################################################
# 
# Disregard.... this was the hard-coded solution
#
# since the unique_candidates list was sorted, we know that the nth element in unique_candidate_votes corresponds
# to the nth element in unique_candidates.
# this allows us to create a dictionary out of these pairs
# 
# voting_dict = dict(zip(unique_candidates,unique_candidate_votes))
        
# correy_votes = 0
# khan_votes = 0
# tooley_votes = 0
# li_votes = 0


# for candidate in candidates:
#     if candidate == 'Correy':
#         correy_votes += 1
#     elif candidate == 'Khan':
#         khan_votes += 1
#     elif candidate == 'Li':
#         li_votes += 1
#     elif candidate == "O'Tooley":
#         tooley_votes += 1
    



# votes = [correy_votes, khan_votes, li_votes, tooley_votes]

# d = dict(zip(unique_candidates,votes))

#make a list of unique candidates and use that instead of hard-coding in my for loop

    