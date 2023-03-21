import csv
import os

# Get to location of budget_data
budget_data = os.path.join('PyBank', 'Resources', 'budget_data.csv')
  
# Reading of CSV file and skip the header                    
with open(budget_data,'r') as budget_file:
    csvreader = csv.reader(budget_file, delimiter=',')
    header = next (csvreader)

# Read each row of data after the header  
    data = [row for row in csvreader]

# Calculate the total number of months included in the dataset
count = len(data)

#The net total amount of "Profit/Losses" over the entire period
net_total = 0
for row in data:
    net_total = net_total + int(row[1])

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
sum_change = 0
for i in range(1,len(data)):
    sum_change = (sum_change + int(data[i][1]) - int(data[i-1][1]))
avg = sum_change / (count - 1)

#The greatest increase in profits (date and amount) over the entire period
differences = [int(data[i][1]) - int(data[i-1][1]) for i in range(1,len(data))]
greatest_increase = max(differences)
index_greatest_increase = differences.index(greatest_increase) + 1
date_greatest_increase = data[index_greatest_increase][0]

#The greatest decrease in profits (date and amount) over the entire period
greatest_decrease = min(differences)
index_greatest_decrease = differences.index(greatest_decrease) + 1
date_greatest_decrease = data[index_greatest_decrease][0]

# Results of calculations above
results = f"""\
Financial Analysis
----------------------------
Total Months: {count}
Total: ${net_total}
Average Change: ${avg:.2f}
Greatest Increase in Profits: {date_greatest_increase} (${greatest_increase})
Greatest Decrease in Profits: {date_greatest_decrease} (${greatest_decrease})
"""
print(results)

# Create a new path to analysis text file
analysis_results = os.path.join('PyBank','analysis','analysis_results.txt')

# Write in csv analysis_results                   
with open(analysis_results,'w') as analysis_file:
    analysis_file.write(results)