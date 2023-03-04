#Written by Shiven Desai
#This program calculates average rainfall over years
years = int(input("Enter the number of years: "))  # prompt the user for the number of years
months = years * 12  # calculate the total number of months

total_rainfall = 0  # initialize a variable to keep track of the total rainfall
for year in range(1, years+1):  # iterate once for each year
    for month in range(1, 13):  # iterate once for each month
        inches = float(input(f"Enter the inches of rainfall for year {year}, month {month}: "))
        total_rainfall += inches  # add the inches to the total

average_rainfall = total_rainfall / months  # calculate the average rainfall
print(f"Number of months: {months}")
print(f"Total inches of rainfall: {total_rainfall}")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")
