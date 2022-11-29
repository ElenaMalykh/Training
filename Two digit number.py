# import random
#
# number = int(input('Enter nimber: '))
# if 0 < number//10 < 9 or -9 < number//10 < 0:
#   print('two-digit number')
# else:
#   print('not a two digit number')
#
#
#
# number_one = int(input('Enter number 1: '))
# number_two = int(input('Enter number 2: '))
# number_three = int(input('Enter number 3: '))
# if number_one == number_two == number_three:
#   print('3')
# elif number_one == number_two != number_three or number_one != number_two == number_three or  number_one == number_three != number_three:
#   print('2')
# else:
#   print('1')
#
#
# apartment_price = int(input('Enter apartment price(mn): '))
# apartment_size = int(input('Enter apartment size(sq. m): '))
# if apartment_price < 10 and apartment_size > 100 or apartment_price < 7 and apartment_size > 80:
#   print('This apartment suits us')
#
# else:
#   print('This apartment suck')



# from random import randint
# lst = [randint(0, 9) for _ in range(100)]
# print(type(lst))
# print(lst)
# print(set(lst))
#
# number_of_duplicates = dict.fromkeys(set(lst), 0)
#
# for i in lst:
#   number_of_duplicates[i] += 1
#
# print(number_of_duplicates)



summ = 0
while (number := int(input('Enter the number: '))) != 0:
  summ += number
  print(summ)





# true_pass = 235

# password  = int(input('Enter pass: '))
# while password != true_pass:
#   print('Wrong pass. Try again')
#   password  = int(input('Enter pass: '))
#
# print('Correct pass')

# car_price = 500000
# my_money = 0
#
# while my_money < car_price:
#   my_money += int(input('How much money to put aside?: '))
# print('Enough for car')


# weather = int(input('Enter the air temperature: '))
# distance = 0
# while weather > 15:
#   distance += 20
#   weather -= 2
#   if weather <= 15:
#     break
#   distance += 10
# print('Distance: ', distance)
