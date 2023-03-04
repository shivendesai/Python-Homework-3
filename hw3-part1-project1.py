#Written by Shiven Desai
#This program calculates distance and time
# Prompt the user for the speed of the vehicle (in mph) and the number of hours it has traveled
speed = int(input("What is the speed of the vehicle in mph? "))
hours = int(input("How many hours has it traveled? "))

# Print a header for the table of hour and distance traveled
print("Hour Distance Traveled")

# Initialize a counter variable to keep track of the current hour
current_hour = 1

# Use a while loop to calculate the distance traveled for each hour in the time period
while current_hour <= hours:
    distance = speed * current_hour  # calculate the distance traveled
    print(current_hour, distance)    # print the hour and distance traveled
    current_hour += 1                # increment the counter variable

