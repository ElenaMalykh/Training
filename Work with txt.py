with open("text.txt", "a") as a:
    for i in range(10):
        if i %2 == 0:
            a.write(str (i))