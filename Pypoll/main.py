#Modules
import os
import csv

#import the data set
imput_path = os.path.join("resources", "election_data.csv")

#initial the variable
candidates = []
total_votes = 0
vote_count = 0
number_of_candidates = 0
candidate_index = []
candidate_vote_count = []
total_vote_count = 0
winner_vote_count = 0
candidate_index = []
winner_vote_count = 0
winner = ""

#open the path and read the file
with open(imput_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip the header
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            number_of_candidates +=1
            candidate_vote_count.append(1)
        else: 

            for candidate in range(number_of_candidates):
                if row[2] == candidates[candidate]:
                    candidate_vote_count[candidate] +=1

winner_vote_count = max(candidate_vote_count)

for candidate in range(number_of_candidates):
    if winner_vote_count == candidate_vote_count[candidate]:
        winner = candidates[candidate]
#print(winner)

# Add all the votes together
    for candidate in range(number_of_candidates):
        total_vote_count += candidate_vote_count[candidate]

# Calculate the percentages for each candidate
    for candidate in range(number_of_candidates):
        print (str(candidates[candidate])+": "+"{:.2f}".format(candidate_vote_count[candidate]/total_vote_count*100) +"% ("+str(candidate_vote_count[candidate])+")")



# Print table for election results
    print ("Election Results")
    print ("----------------------------")
    print (f"Total Votes: {total_vote_count}")
    print ("----------------------------")
    print ("----------------------------")
    print (f"Winner: {winner}")
    print ("----------------------------")

# Send output file as txt
output_path = os.path.join("Outputs", "election_output.txt")

# Initialize writer
txtwriter = open(output_path, 'w')

# Write the row of total votes
txtwriter.write(f"Total Votes: {total_vote_count}\n")

# Write info for each candidate
for candidate in range(number_of_candidates):
    txtwriter.write(str(candidates[candidate])+": "+"{:.2f}".format(candidate_vote_count[candidate]/total_vote_count*100) +"% ("+str(candidate_vote_count[candidate])+")\n")

# Write the information about the winner
txtwriter.write(f"Winner: {winner}\n")
    

