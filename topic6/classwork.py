def topic8_2():
    while ((n := int(input())) != 0):
        print(n)

def topic8_3():
    while ((s := input()) != ""):
        print(s)

def topic8_4():
    sum = 0
    while (n := float(input())) >= 0:
        sum += n * 0.95 if n > 1000 else n
       #sum += n > 1000 ? n * 0.95 : n; C#
    print(sum)

def topic8_5():
    i = 0
    sum = 0
    while (n := float(input())) > -275.15:
        sum += n
        i += 1
    print(sum / i)

topic8_5()

