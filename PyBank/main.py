import os
import csv
import numpy as np

# Converts the Date and Profits/Losses columns into lists. 
total_months = []
profits_list = []
budget_data_csv = os.path.join('Resources', 'budget_data.csv')
# Opens the budget data file. 
with open (budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    # Skips the header row. 
    header_row = next(csvfile)
    
    for row in csvreader:
        months = row[0]
        # Adds the months to the 'Total Months' list. 
        if months not in total_months:
            total_months.append(months)


        profits = int(row[1])
        # Adds the profit/loss amounts to the 'Profits' list. 
        profits_list.append(profits)
        # Calculates the net amount of profits/losses. 
        total_profits = sum(profits_list)

        # Calculates the changes in profits/losses over the entire CSV. 
        change_in_profits = np.diff(profits_list)
        # Calculates the average of the changes in profits/losses. 
        average_change_in_profits = change_in_profits.mean()
        # Formats the value for average profits/losses to include two decimal places. 
        average_change_formatted = "{:.2f}".format(average_change_in_profits)
       
    # Calculates the largest increase in profits. 
    max_increase_in_profits = max(change_in_profits)
    # Calculates the largest decrease in profits. 
    max_decrease_in_profits = min(change_in_profits)
    for i in range(len(change_in_profits)):
        if change_in_profits[i] == max_increase_in_profits:
            # Matches the greatest increase in profits with its corresponding month. 
            max_increase_statement = str(f"{total_months[i + 1]} (${max_increase_in_profits})")

        if change_in_profits[i] == max_decrease_in_profits:
            # Matches the greatest decrease in profits with its corresponding month. 
            max_decrease_statement = str(f"{total_months[i + 1]} (${max_decrease_in_profits})")
        
    
    # Finds the number of months in total. 
    total_months_count = len(total_months)
    
    
    
    # Summarizes the results. 
    financial_results = (
        f"Financial Analysis\n"
        f"-------------------\n"
        f"Total Months: {total_months_count}\n"
        f"Total: ${total_profits}\n"
        f"Average Change: ${average_change_formatted}\n"
        f"Greatest Increase in Profits: {max_increase_statement}\n"
        f"Greatest Decrease in Profits: {max_decrease_statement}")
    print(financial_results)
    
output_path = os.path.join('analysis', 'main.txt')
with open (output_path, 'w') as textfile:
    textfile.write(financial_results)
