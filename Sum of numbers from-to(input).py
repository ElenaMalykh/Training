first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))
numbers_sum = 0
for numbers in range(first_number, second_number +1):
  numbers_sum += numbers
print('Sum is: ', numbers_sum)