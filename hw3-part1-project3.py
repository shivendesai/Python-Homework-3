#Written by Shiven Desai
#This program displays the sum of positive numbers
total = 0
number = 0
while number >= 0:
    number = int(input('Enter a series of positive numbers or enter a negative number to end: '))
    if number >= 0:
        total += number
print(f'The sum of the positive numbers entered is: {total}')