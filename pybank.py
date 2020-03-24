
#import libraries
import os
import csv
import pandas as pd

csvpath = os.path.join('..', 'python-challenge', 'budget_data.csv')

#find total months
with open(csvpath, "r") as f:
    reader = csv.reader(f, delimiter=",")
    data = list(reader)
    row_count = len(data) - 1

#find sum using pandas
data_file_df = pd.read_csv(csvpath)
total_sum = data_file_df["Profit/Losses"].sum()



#emppty place holders
total_profit = []
monthly_change = []
total_months = []

#open file
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    for row in csvreader:

        #append profits and months
        total_profit.append(int(row[1]))
        total_months.append(row[0])

    for i in range(len(total_profit)-1):

        #append the monthly changes
        monthly_change.append(total_profit[i+1]-total_profit[i])

#store the best and worst months
max_month = max(monthly_change)
min_month = min(monthly_change)

#fine the max and min of total profits
max_increase = total_profit.index(max(total_profit))
max_decrease = total_profit.index(min(total_profit))



#Print out the totals
print("Financial Analysis"
      "\n------------------------------")
print(f"Total Months: {str(row_count)}")
print(f"Total: ${total_sum}")
print(f"Average Change: ${round(sum(monthly_change)/(row_count - 1), 2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase]} (${str(max_month)})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease]} (${str(min_month)})")

# Specify the file to write to
output_path = os.path.join("..", "python-challenge", "financial_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile)

    # Write Financial Analysis into an output file
    csvwriter.writerow(["Financial Analysis"
      "\n------------------------------"])
    csvwriter.writerow([f"Total Months: {str(row_count)}"])
    csvwriter.writerow([f"Total: ${total_sum}"])
    csvwriter.writerow([f"Average Change: ${round(sum(monthly_change)/(row_count - 1), 2)}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {total_months[max_increase]} (${str(max_month)})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {total_months[max_decrease]} (${str(min_month)})"])

