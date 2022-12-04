count = 0
for ticket in 345, 19, 87, 1020, 421:
    if 99 < ticket < 1000 and ticket % 5 == 0:
        print(ticket, " - Выигрышный билет!")
        count += 1

print("Количество победителей -", count)