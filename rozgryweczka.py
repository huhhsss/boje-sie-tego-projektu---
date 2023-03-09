#===============importy================
from random import randint
from kartofel import Sklep
from kartofel import Zwykły_atak
from kartofel import Podwójny_atak
from kartofel import Leczenie
from kartofel import Leczenie_mala_potka
from kartofel import Leczenie_srednia_potka
from kartofel import Leczenie_duza_potka
from kartofel import Wybierzleczenie
from kartofel import Upgrade
from kartofel import Przeciwnik

#===============bohater================

bio = {
        "imie": None,
        "maxhp": 100,
        "hp": 100,
        "poziom": 1,
        "coin": 1000,
        "enemyhp": 30,
        "lvl_miecza":1, 
        "lvl_zbroji":1
        }


#==============przedmioty==============

shopitems = {
                "miecz" : "miecz",
                "zbroja" : "zbroja",
                "mala_potka" : "mala potka",
                "srednia_potka" : "srednia potka",
                "duza_potka" : "duza potka"
                }


myitems = []

#===========dane przeciwnika=============

dane_przeciwnik={
    "nazwa" : None,
    "enemyatack" : randint(1,3),
    "enemycoin": randint(0,25),
    "pokonane_bosy" : 0, 
    "pokonani_przeciwnicy": 0
}


#========================================

bio["imie"] = input("podaj imie swojego bohatera:\n")

input(f'\n{bio["imie"]} Zaczynasz swoją podróż')
print(f"twoje statystyki:\n\n {bio}")

while bio["hp"] > 0:
    bio["maxhp"]>= bio["hp"]
    print('-'*50)
    print(f'Twoje przedmioty:   {myitems}')
    print(f"twoje statystyki:\n\n {bio}")
    print('1 - walka')
    print('2 - sklep\n\n')
    inp = input('Co chcesz zrobić?   ')
    if inp == 'stop':
        break
    elif inp == '1':
        if bio["poziom"] % 5 == 0:
            print('!'*50)
            print('Nadszedł czas na walkę z Bossem!')
            dane_przeciwnik["nazwa"] = "boss"
            bio["enemyhp"] = 40
            while bio["enemyhp"] > 0 and bio["hp"] > 0 :
                Przeciwnik.enemy_atak(bio, dane_przeciwnik)
                w = int(input("co chcesz zrobic?\n\n 1 - atak\n2 - leczenie"))
                if w == 1:
                    odp = int(input("wybierz atak\n\n 1 - zwykły atak\n 2 - podwójny atak"))
                    if odp == 1:
                        Zwykły_atak(bio)
                    elif odp == 2:
                        Podwójny_atak(bio, myitems)
                elif w == 2:
                    d = int(input())
                    Wybierzleczenie.wybieranieleczenia(d, bio, myitems)
            else:
                if bio["enemyhp"] < 0 and bio["hp"] >0:
                    Przeciwnik.enemy_atak(bio, dane_przeciwnik)
                    Przeciwnik.enemy_coiny(bio, dane_przeciwnik)
                    bio["poziom"] = bio["poziom"] + 1
                    print(f"twoje statystyki:\n {bio}\n\n pokonane bossy:{dane_przeciwnik['pokonane_bosy']}, pokonani przeciwnicy:{dane_przeciwnik['pokonani_przeciwnicy']}")
                elif bio["enemyhp"] > 0 and bio["hp"] <= 0:
                    print('przegrałeś')
                    break

        if bio["poziom"] % 5 != 0:
            print('!'*50)
            print('Nadszedł czas na walkę z przeciwnikiem!')
            dane_przeciwnik["nazwa"] = "przeciwnik"
            bio["enemyhp"] = 20
            while bio["enemyhp"] > 0 and bio["hp"] > 0 :
                Przeciwnik.enemy_atak(bio, dane_przeciwnik)
                w = int(input("co chcesz zrobic?\n\n 1 - atak\n2 - leczenie"))
                if w == 1:
                    odp = int(input("wybierz atak\n\n 1 - zwykły atak\n 2 - podwójny atak"))
                    if odp == 1:
                        Zwykły_atak(bio)
                    elif odp == 2:
                        Podwójny_atak(bio, myitems)
                elif w == 2:
                    d = int(input())
                    Wybierzleczenie.wybieranieleczenia(d, bio, myitems)
            else:
                if bio["enemyhp"] < 0 and bio["hp"] >0:
                    Przeciwnik.enemy_atak(bio, dane_przeciwnik)
                    Przeciwnik.enemy_coiny(bio, dane_przeciwnik)
                    bio["poziom"] = bio["poziom"] + 1
                    print(f"twoje statystyki:\n {bio}\n\n pokonane bossy:{dane_przeciwnik['pokonane_bosy']}, pokonani przeciwnicy:{dane_przeciwnik['pokonani_przeciwnicy']}")
                elif bio["enemyhp"] > 0 and bio["hp"] <= 0:
                    print('przegrałeś')
                    break

    elif inp == "2":
        co = input("co chcesz zrobić?\n\n 1 - kupic\n2 - ulepszyc")
        if co == '1':
            Sklep.przedstawienie()
            odp = input("decyzja:")
            while odp != 'nic':   
                if odp == "1":
                    Sklep.kupmiecz(shopitems, bio, myitems)
                    print(odp)
                    odp = input("co jeszcze: ") 
                elif odp == '2':
                    Sklep.kupzbroje(shopitems, bio, myitems)
                    odp = input("co jeszcze:")
                elif odp == '3':
                    Sklep.kupmalapotka(shopitems, bio, myitems)
                    odp = input("co jeszcze: ") 
                elif odp =='4':
                    Sklep.kupsredniapotka(shopitems, bio, myitems)
                    odp = input("co jeszcze: ") 
                elif odp == '5':
                    Sklep.kupduzapotka(shopitems, bio, myitems)
                    odp = input("co jeszcze: ")  

            else:
                Sklep.zakonczenie(myitems)
                print(myitems)
        elif co == '2':
            Upgrade.wybierzulepszenie()
            odpp = input("decyzja:")
            while odpp != "nic":
                Upgrade.upgrady(odpp, bio, myitems)
                print(bio["lvl_miecza"])
                odpp = input("czy coś jeszcze? ")
            else:
                Upgrade.konieculepszaniachyba(bio)

else:
    print(bio)
    print(dane_przeciwnik["pokonane_bosy"])
    print[dane_przeciwnik["pokonani_przeciwnicy"]]


 
