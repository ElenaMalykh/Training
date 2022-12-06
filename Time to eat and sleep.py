woke_up = int(input('Enter wake time: '))
calories_sum = 0
awake_hours = 0
hour: int
for hour in range(woke_up, 23):
  print('Now:', hour, ':00')
  calories_per_our = int(input('Enter calories: '))
  calories_sum += calories_per_our
  if calories_sum < 2000:
      woke_up +=1
      continue
  break
print('Sum is: ', calories_sum, '. Its enough. You should go to sleep')