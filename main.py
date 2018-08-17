# Module for reading CSV files

import os
import csv
import statistics

filepath = os.path.join('budget_data.csv')

row_count = 0
net_revenue = 0
max_difference = 0
min_difference = 0
sum_difference = 0
num_items_difference = 0

dates = []
revenue = []

# reads through csv and counts all of the months as row_count, adds up total revenue, and appends both the dates and revenue values
# to separate lists
#
with open(filepath, newline = '') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')    
    csv_header = next(csv_reader)
    for row in csv_reader:
        row_count +=1
        net_revenue += int(row[1])
        dates.append(row[0])
        revenue.append(int(row[1]))

# creates a list of each profit/loss for every month except the first one
#
difference = [revenue[i+1]-revenue[i] for i in range(len(revenue)-1)]

# iterates through the profit/loss for each month and stores values to calculate the average profit/loss
#
for items in difference:
    sum_difference += items
    num_items_difference +=1

# calculates the average profit/loss and rounds to 2 decimal places
#
avg_difference = round(sum_difference/num_items_difference,2)

#avg_difference = round(statistics.mean(difference),2) <----------------This was using the stats module, which is not allowed

# deletes the first element in the dates list to be able to have a list that will correspond to the 
# list that stores the profit/loss for every month. first profit/loss will be after the first month has passed
# so we don't count it
#
del dates[0]

# zips up the dates and the profit/loss lists and iterates to find the largest gain and biggest loss
#
for i, j in zip(dates, difference):
    if j > max_difference:
        max_difference = j
        max_date = i
    elif j < min_difference:
        min_difference = j
        min_date = i


print('Financial Analysis')
print('------------------------------------')
print(f'Total Months: {row_count}')
print(f'Total: ${net_revenue}')
print(f'Average Change: ${avg_difference}')
print(f'Greatest Increase in Profits: ${max_difference} on {max_date}')
print(f'Greatest Decrease in Profits: ${min_difference} on {min_date}')


with open('output.txt', 'w', newline='') as textfile:
    textfile.write('Financial Analysis\n')
    textfile.write('------------------------------------\n')
    textfile.write(f'Total Months: {row_count}\n')
    textfile.write(f'Total: ${net_revenue}\n')
    textfile.write(f'Average Change: ${avg_difference}\n')
    textfile.write(f'Greatest Increase in Profits: ${max_difference} on {max_date}\n')
    textfile.write(f'Greatest Decrease in Profits: ${min_difference} on {min_date}\n')
