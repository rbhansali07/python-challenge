import csv
import os
file_path = os.path.join("Resources", "budget_data.csv")

with open(file_path, 'r') as file_handle:
    csv_handle = csv.reader(file_handle, delimiter=',')
    header = next(csv_handle)
    #getting first row values for initial calculation
    row_one = next(csv_handle)
    #count variable to get total number of months
    count = 1
    #initializing variables to calculate average profit/loss and month with greatest profit and loss
    avg_sum = 0
    total = int(row_one[1])
    start_profit = 0
    start_loss = 0
    start_num = row_one[1]
    
    #going over all rows one at a time
    for row in csv_handle:
        count = count + 1
        #getting profit/loss difference between previous and current month
        profit_loss = int(row[1]) - int(start_num)
        #adding profit/loss to get total amount of profit and loss difference
        avg_sum = avg_sum + profit_loss
        total = total + int(row[1])
        #comparing the profit/loss to find month with greatest profit and loss difference
        if profit_loss > start_profit:
            start_profit = profit_loss
            profit_mth = row[0] 
        if profit_loss < start_loss:
            start_loss = profit_loss
            loss_mth = row[0]
       #resetting the starting number for next row caluclation
        start_num = row[1]
    #Using count -1 for average change as number of change is one less than number of months
    avg_chg = round((avg_sum/(count-1)),2)
    #Creating desired output
    output = []
    output.append("Financial Analysis")
    output.append("----------------------------------")
    output.append(f'Total Months: {count}')
    output.append(f'Total: ${total}')
    output.append(f'Average Change: ${avg_chg}')    
    output.append(f'Greatest Increase in Profits: {profit_mth} (${start_profit})')
    output.append(f'Greatest Decrease in Profits: {loss_mth} (${start_loss})')
    output = '\n'.join(output)
    print(output)
with open('Output/PyBank_output.txt', 'w') as txtfile:
    txtfile.write(str(output))
 

            
        
        
