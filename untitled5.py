from random import randint
import math 
savol = "dastur tugawi uchun 'exit' deb yozin: "
# savol += ' dastur tugawi uchun"exit" deb yozin ' 
iwora = True
while iwora:
    
    a = randint(1, 11)
    b = randint(1, 11)
    c = int(input("{} * {} = ".format(a, b)))
    if a*b == c:
        print("togr")
    else:
        print("notogri")
    qiymat = input(savol)
    if qiymat == "exit":
        break
