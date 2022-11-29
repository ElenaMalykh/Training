exit_code = "0550"  # int числа не могут начинаться с 0, поэтому надо использовать str
while True:
    print("Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!")
    user_code = input("Введите код: ")  # И тут соответственно не нужно приводить число к int типу
    if user_code == exit_code:
        print("Код верный, завершаю работу...")
        break

# while user_code := input('Enter password: ') != '0550':
#   print('Computer has been blocked. First give back my skate, Than I will tell you the password')
#
# print('Right')