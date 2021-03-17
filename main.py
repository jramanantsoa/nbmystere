import random

n = random.randint(1,10)
essais_restants = 3
while essais_restants > 0:
    a = input("Quel est le nombre mystère ? :")
    essais_restants -= 1
    print(n)
    print(f"il reste {essais_restants}")
    if int(a) < n:
        print("Inférieur")
    elif int(a) > n:
        print("supérieur")
    else :
        if essais_restants == 3:
            print("Bravo ! C'était bien "+str(n)+". Trouvé dès le premier coup !")
        else:
            print("Bravo ! C'était bien "+str(n)+". Trouvé au bout de "+str(3 - essais_restants)+" tentatives !")
        break
print(f"Dommage... Le nombre mystère était {n}" )