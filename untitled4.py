# juft = int(input("juft son kiriting: ")); (print("rahmat") if juft % 2 ==0 else print("juft son kiriting"))

# s = int(input("son krt: "))

# for n in range(2, 11):
#     if not (s % n):
#         print(f"{s} soni {n} ga qoldqsz bolnad")
# 
# sonla = [1, 2, 3, 4 ,5, 6, 7, 8, 9, 10]

# for x in sonla:
#     print(x, end=(" "))

# for x in range(1, 11):
#     print(x, end=(" "))

# til = input("tlni tanlang uz/en/ru  ")
  
# if til == 'uz':
    # print("salom")
# elif til == 'ru':
    # print("privet")
# 
# elif til == 'en':
    # print("hello")
# else:
#     # print("uz/en/ru ladan brni tanlang")

# yow = '18'
# print(yow.isdigit())

# y = input("yowin nechda: ")
# if y.isdigit():
#     y = float(y)
# else: 
#     print("matnl raqam")

from random import randint
import math 
a = randint(1, 11)
b = randint(1, 11)

masala = ["kop", "bol", "ayr", "qow", "ara"]
s = 1
for m in masala:
    print(s, "-", m, end=("\n"))
    s+= 1

while True:
    amal = input("wuladan brni tanla: ")
    if "ayr" == amal:
        a = randint(1, 10)
        b = randint(1, 10)
        c = int(input("{} - {} = ".format(a, b)))
        print("togr")
    if "qow" == amal:
        a = randint(1, 10)
        b = randint(1, 10)
        c = int(input("{} + {} = ".format(a, b)))
        if c == (a + b):
            print("togr")
    
    if "kop" == amal:
        a = randint(1, 10)
        b = randint(1, 10)
        c = int(input("{} * {} = ".format(a, b)))
        print("togr")
    
    if "bol" == amal:
        a = randint(1, 10)
        b = randint(1, 10)
        c = float(input("{} / {} = ".format(a, b)))
        print("togr")
    
    # if "ild" == amal:
    #     a = randint(1, 10)
    #     b = randint(1, 10)
    #     c = int(input(math.sqrt(a)))
    #     print("togr")
    if "ara" == amal:
        a = randint(1, 10)
        b = randint(1, 10)
        c = float(input("{} / {} = ".format(a, b)))
        d = int(input("{} * {} = ".format(a, b)))
        c = int(input("{} - {} = ".format(a, b)))
        c = float(input("{} + {} = ".format(a, b)))
        # c = int(input(math.sqrt(a)))    
        print("togr")










































































































