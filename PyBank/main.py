#Modules
import os
import csv



#import the data set
imput_path = os.path.join("resources", "budget_data.csv")

#initial the variable
months = 0
total = 0
average_pl_change = 0
date = []
pl = []
pl_change = []
max_increase = 0
max_decrease = 0

#open the path and read the file
with open(imput_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip the header
    header = next(csvreader)

    for row in csvreader:
        months += 1
        total +=int(row[1])
        date.append(row[0])
        pl.append(int(row[1]))

    for month in range(len(pl)-1):
        pl_change.append(pl[month+1]-pl[month])
    
average_pl_change = sum(pl_change)/(len(pl)-1)
max_increase = max(pl_change)
max_decrease = min(pl_change)

increase_index=pl_change.index(max_increase)
decrease_index=pl_change.index(max_decrease)
increase_month=date[increase_index+1]
decrease_month=date[decrease_index+1]
print(decrease_month)

print("Financial Analysis")
print("-------------------------------")
print(f"Total Months:{months}")
print(f"Total: ${total}")
print("Average Change: $"+"{:.2f}".format(average_pl_change))
print(f"Greatest Increase in Profits: {increase_month}, ${max_increase}")
print(f"Greatest Decrease in Profits: {decrease_month}, ${max_decrease}")


output_path = os.path.join("outputs", "budget_output.txt")
txtbudget = open(output_path, "w")

txtbudget.write(f"Total Months:{months}\n")
txtbudget.write(f"Total: ${total}\n")
txtbudget.write("Average Change: $"+"{:.2f}".format(average_pl_change)+"\n")
txtbudget.write(f"Greatest Increase in Profits: {increase_month}, ${max_increase})\n")
txtbudget.write(f"Greatest Decrease in Profits: {decrease_month}, ${max_decrease}")



