import random
def son_odam(x=10):
    t_son = random.randint(1, x)
    print("kelin son top oynini oynaymz! ")
    print(f"1 dan {x} gacha son oyladm. Topa olaszmi?")
    i =0 
    while True:
        i+= 1
        taxmin = int(input(">>> "))
        if taxmin < t_son:
            print(f"xoto, men oylagan son {taxmin} dan kattaroq")
        elif taxmin > t_son:
            print(f"xato, men oylagan son {taxmin} dan kichina")
        else:
            break
        
    print(f"topdingz! {t_son} son ")





























































