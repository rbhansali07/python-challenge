import csv
import os
file_path = os.path.join("Resources", "election_data.csv")

with open(file_path, 'r') as file_handle:
    csv_handle = csv.reader(file_handle, delimiter=',')
    header = next(csv_handle)
    election_dict = {}
    count = 0
    #creating election dictionary by going over each row
    for row in csv_handle:
        count += 1
        if row[2] in election_dict:
            election_dict[row[2]] +=1
        else:
            election_dict[row[2]] = 1
    #setting Output
    output = []
    output.append("Election Results")
    output.append("----------------------------------")
    output.append(f'Total Votes: {count}')
    output.append("----------------------------------")
    #Looping over dictionary keys to get win percentage
    for name in election_dict.keys():
        percentage = round(election_dict[name]*100/count)
        output.append(f'{name}: {"%.3f"%percentage}% ({election_dict[name]})')
    #finding the winner using key lookup for max value
    winner = max(election_dict, key=election_dict.get)
    output.append("----------------------------------")
    output.append(f'Winner: {winner}')
    output.append("----------------------------------")
    output = '\n'.join(output)
    print(output)
with open('Output/PyPoll_output.txt', 'w') as txtfile:
   txtfile.write(str(output))
 

            
        
        
