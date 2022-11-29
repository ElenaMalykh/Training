counter_plus = 0
counter_minus = 0
while (number := int(input('Enter the number : '))) != 0:
    if number < 0:
        counter_minus += 1
    else:
        counter_plus += 1
print ('number of positive numbers: ', counter_plus)
print ('number of negative numbers: ', counter_minus)

