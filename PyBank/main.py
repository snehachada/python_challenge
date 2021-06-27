import os
import csv
path = os.path.join('Resources', 'budget_data.csv')
with open(path) as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    data = []
    for row in csvreader:
        data.append(row)
    #Months in dataset
months = len(data)
print(months)
#Net profit/loss
pandl = []
for row in data:
    pandl.append(int(row[1]))
total_pandl = sum(pandl)
#Avg change in profit/loss
changes = []
for i in range(1, len(pandl)):
    value = pandl[i]
    prev_value = pandl[i - 1]
    change = value - prev_value
    changes.append(change)
avg_change = sum(changes)/len(changes)
print(avg_change)
#Max increase in profit/loss
max_change = max(changes)
print(max_change)
max_index = changes.index(max_change)
max_month = data[max_index + 1][0]
print(max_month)
#Greatest decrease in profit/loss
min_change = min(changes)
print(min_change)
min_index = changes.index(min_change)
min_month = data[min_index + 1][0]
print(min_month)
print("------------------")
print(f"Total months: {months}")
print(f"Total P&L: ${round(total_pandl, 2)}")
print(f"Average change: ${round(avg_change, 2)}")
print(f"Greatest Increase: {max_month} ({max_change})")
print(f"Greatest Loss: {min_month} ({min_change})")

# write the file in text file and w is used for replacing existing file
PyBank = open("Analysis/output_PyBank.txt", "w")
PyBank.write("---------------------")
PyBank.write("Financial Analysis") 
PyBank.write("---------------------")
PyBank.write('\n' +"Total Months: " + str(months)) 
PyBank.write('\n' +"Total P&L: " + str(round(total_pandl, 2)))
PyBank.write('\n' +"Average: " + str(round(avg_change, 2))) 
PyBank.write('\n' +"Greatest Increase: $" +str(max_change) +" in the month " +max_month) 
PyBank.write('\n' +"Greatest Loss: $" +str(min_change) +" in the month " +min_month)
PyBank.close
