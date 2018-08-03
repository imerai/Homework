# Dependencies
import csv

# Files to Load
file_to_load = "/Users/VINESH/Desktop/GitLab/nu-class-homework/HW3/budget_data.csv"
file_to_output = "/Users/VINESH/Desktop/GitLab/nu-class-homework/HW3/PyBank.txt"

#Tracking variable
# Total month, basically total rows
tMonth = 0
# Total revenue
tRevenue = 0
# First row to skip
fRow = True
# Revenue change
rChange = 0
# Price change
pChange = 0
# List of greatest increase in price and the month
gIncrease = ["", 0]
# List of greatest decrease in price and the month
gDecrease = ["", 0]
# Revenue average
rAvg = 0
# List of revenue changes
rChanges = []

# Read Files
with open(file_to_load, newline="") as revenue_data:
    csvreader = csv.reader(revenue_data, delimiter=',')

    # Loop through all the rows of data we collect
    for row in csvreader:
        # skip first row
        if fRow:
            fRow = False
            continue
        tMonth = tMonth + 1
        # Total Revenue, as we loop thru each row accoumulate the revenue col
        tRevenue = tRevenue + int(row[1])
         # Keep track of changes between the current row and previous row
        rChange = int(row[1]) - pChange
         # Reset the value of pChange to the current row 
        pChange = int(row[1])
        ####print (int(rChange), int(gIncrease[1]))
        # Revenue change is greater than revneue value in prev row,
        #  set prev row revenue date and value to list
        if (rChange > gIncrease[1]):
            gIncrease[0] = row[0]
            gIncrease[1] = rChange
        # Revenue change is less than revneue value in prev row,
        #  set prev row revenue date and value to list    
        if (rChange < gDecrease[1]):
            gDecrease[0] = row[0]
            gDecrease[1] = rChange
        
         # Add to the revenue_changes list to derive average
        rChanges.append(int(row[1]))

    # Set the Revenue average
    rAvg = sum(rChanges) / len(rChanges)

    # Display results
    print()
    print("Financial Analysis")
    print("------------------")
    print("Total Months: " + str(tMonth))
    print("Total: " + "$" + str(tRevenue))
    print("Average Change: " + "$" + str(round(sum(rChanges) / len(rChanges),2)))
    print("Greatest Increase in Profit: " + str(gIncrease[0]) + " ($" +  str(gIncrease[1]) + ")") 
    print("Greatest Decrease in Profit: " + str(gDecrease[0]) + " ($" +  str(gDecrease[1]) + ")")

    # Export to test file and check if successfully written to file
try:
    with open(file_to_output, "w") as txt_file:
        txt_file.write("Financial Analysis")
        txt_file.write("\n")
        txt_file.write("------------------")
        txt_file.write("\n")
        txt_file.write("Total Months: " + str(tMonth))
        txt_file.write("\n")
        txt_file.write("Total Revenue: " + "$" + str(tRevenue))
        txt_file.write("\n")
        txt_file.write("Average Change: " + "$" + str(round(sum(rChanges) / len(rChanges),2)))
        txt_file.write("\n")
        txt_file.write("Greatest Increase: " + str(gIncrease[0]) + " ($" + str(gIncrease[1]) + ")") 
        txt_file.write("\n")
        txt_file.write("Greatest Decrease: " + str(gDecrease[0]) + " ($" + str(gDecrease[1]) + ")")
        print()
        print()
        print("File written")
except IOError as x:
    print("Error writing to file")