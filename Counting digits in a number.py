number = int(input('Enter the number : '))
counter = 0
if number == 0:
  print (1)
else:
    while number > 0:
        number = number // 10
        counter +=1
    print (counter)