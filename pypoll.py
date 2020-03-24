
#import libraries
import os
import csv
import pandas as pd


#import csv file

file = os.path.join('..', 'python-challenge', 'election_data.csv')

#read the csv file
df = pd.read_csv(file)

#Total votes
total_votes = df['Voter ID'].value_counts()
len_total_votes = len(total_votes)


#take a look at the index
df_index = df.set_index("Candidate")
#print(df_index.head())

#khan count
khan_count = df_index.loc["Khan", "Voter ID"]
khan_total_count = len(khan_count)
khan = round(khan_total_count/len_total_votes, 2) * 100

#Correy count
correy_count = df_index.loc["Correy", "Voter ID"]
correy_total_count = len(correy_count)
correy = round(correy_total_count/len_total_votes, 2) * 100

#Li count
li_count = df_index.loc["Li", "Voter ID"]
li_total_count = len(li_count)
li = round(li_total_count/len_total_votes, 2) * 100

#O'Tooly count
tooley_count = df_index.loc["O'Tooley", "Voter ID"]
tooley_total_count = len(tooley_count)
tooley = round(tooley_total_count/len_total_votes, 2) * 100

#find out the winner
if khan_total_count > li_total_count and khan_total_count > tooley_total_count and khan_total_count > \
        correy_total_count:
    winner = "Khan"
elif li_total_count > khan_total_count and li_total_count > tooley_total_count and li_total_count > correy_total_count:
    winner = "Li"
elif correy_total_count > li_total_count and correy_total_count > tooley_total_count and correy_total_count > \
        khan_total_count:
    winner = "Correy"
elif tooley_total_count > li_total_count and tooley_total_count > khan_total_count and tooley_total_count > \
        correy_total_count:
    winner = "O'Tooley"

#printing out stuff
print("Election Results"
      "\n-------------------")
print(f"Total Votes: {len_total_votes}")
print("---------------------")
print(f"Khan: {khan}% ({khan_total_count})")
print(f"Correy: {correy}% ({correy_total_count})")
print(f"Li: {round(li, 2)}% ({li_total_count})")
print(f"O'Tooley: {tooley}% ({tooley_total_count})")
print("---------------------")
print(f"Winner: {winner}")
print("---------------------")


# Specify the file to write to
output_path = os.path.join("..", "python-challenge", "election_results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile)

    # Write Financial Analysis into an output file
    csvwriter.writerow(["Election Results"
      "\n-------------------"])
    csvwriter.writerow([f"Total Votes: {len_total_votes}"])
    csvwriter.writerow(["---------------------"])
    csvwriter.writerow([f"Khan: {khan}% ({khan_total_count})"])
    csvwriter.writerow([f"Correy: {correy}% ({correy_total_count})"])
    csvwriter.writerow([f"Li: {round(li, 2)}% ({li_total_count})"])
    csvwriter.writerow([f"O'Tooley: {tooley}% ({tooley_total_count})"])
    csvwriter.writerow(["---------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["---------------------"])