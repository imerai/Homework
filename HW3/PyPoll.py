# Dependencies
import csv
# Using a function that retuns a callable value (found this in google search for sorting)
from operator import itemgetter
# Files to Load
#file_to_load = "/Users/VINESH/Desktop/election_data.csv"
file_to_load = "/Users/VINESH/Desktop/GitLab/nu-class-homework/HW3/election_data.csv"
file_to_output = "/Users/VINESH/Desktop/GitLab/nu-class-homework/HW3/PyPoll.txt"

#Variables
# Used to skip first row
fRow = True
# Count of total votes per candidate
tVotes = 0
# Total candidate count
tCandidates= 0
# Total votes
gVotes = ["", 0]
# Define a list to hold Candidate names
cOptions = []
# Define a truple to hold count of votes for each candidate 
cVotes = {}
# Define a list to hold calculate values
cList = []

with open(file_to_load, newline="") as election_data:
    csvreader = csv.reader(election_data, delimiter=',')

    for row in csvreader:
        # skip first row
        if fRow:
            fRow = False
            continue
        # Total votes basically total rows in file
        tVotes = tVotes + 1
        # Third col of csv holds the candidates name
        tCandidates = row[2]
        # First time round add the name to list and votes count = 1
        if row[2] not in cOptions:
            cOptions.append(row[2])
            cVotes[row[2]] = 1
        else:
            # Name already in list so increment vote count
            cVotes[row[2]] = cVotes[row[2]] + 1
    # the result of the first 10 row of  the if stmt is:
    # {'Khan': 1}
    # {'Khan': 1, 'Correy': 1}
    # {'Khan': 2, 'Correy': 1}
    # {'Khan': 3, 'Correy': 1}
    # {'Khan': 4, 'Correy': 1}
    # {'Khan': 4, 'Correy': 1, 'Li': 1}
    # {'Khan': 4, 'Correy': 2, 'Li': 1}
    # {'Khan': 5, 'Correy': 2, 'Li': 1}
    # {'Khan': 6, 'Correy': 2, 'Li': 1}
    # {'Khan': 6, 'Correy': 3, 'Li': 1}
    for candidate in cVotes:
        #print("cVotes: " + str(cVotes))
        # {'Khan': 323, 'Correy': 113, 'Li': 55, "O'Tooley": 9}
       
        # To a new list add Name, percentage of all votes and total votes of the candidate
        cList.append(candidate)
        cList.append((cVotes[candidate]/tVotes)*100)
        cList.append(cVotes[candidate])
        #['Khan', 64.60000000000001, 323, 'Correy', 22.6, 113, 'Li', 11.0, 55, "O'Tooley", 1.7999999999999998, 9]
print()
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(tVotes))
print("-------------------------")
# This is not a great or proper way to do this but in the short time I have, this works
print(cList[0] + ":" + "     " + str(round(cList[1])) + "%" + " (" + str(cList[2]) + ")") 
print(cList[3] + ":" + "   " + str(round(cList[4])) + "%" + " (" + str(cList[5]) + ")") 
print(cList[6] + ":" + "       " + str(round(cList[7])) + "%" + " (" + str(cList[8]) + ")") 
print(cList[9] + ":" + "  " + str(round(cList[10])) + "%" + " (" + str(cList[11]) + ")") 
#  itemgetter is a callable that grabs the first item from a list-like object, also reverse the order
winner = sorted(cVotes.items(), key=itemgetter(1), reverse=True)
print("-------------------------")
print("Winner: " + str(winner[0]))
print("-------------------------")
#Winner: ('Khan', 323)

# Write to file
try:
    with open(file_to_output, "w") as txt_file:
        txt_file.write("Election Results")
        txt_file.write("\n")
        txt_file.write("-------------------------")
        txt_file.write("\n")
        txt_file.write("Total Votes: " + str(tVotes))
        txt_file.write("\n")
        txt_file.write("-------------------------")
        txt_file.write("\n")
        txt_file.write(cList[0] + ":" + "     " + str(round(cList[1])) + "%" + " (" + str(cList[2]) + ")")
        txt_file.write("\n")
        txt_file.write(cList[3] + ":" + "   " + str(round(cList[4])) + "%" + " (" + str(cList[5]) + ")")
        txt_file.write("\n")
        txt_file.write(cList[6] + ":" + "       " + str(round(cList[7])) + "%" + " (" + str(cList[8]) + ")")
        txt_file.write("\n")
        txt_file.write(cList[9] + ":" + "  " + str(round(cList[10])) + "%" + " (" + str(cList[11]) + ")")
        txt_file.write("\n")
        txt_file.write("-------------------------")
        txt_file.write("\n")
        txt_file.write("Winner: " + str(winner[0]))
        txt_file.write("\n")
        print()
        print()
        print("File written")
except IOError as x:
    print("Error writing to file")