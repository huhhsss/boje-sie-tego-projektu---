#==============importy=================
from random import randint

#===============bohater================

bio = {
        "imie": None,
        "maxhp": 100,
        "hp": 100,
        "xp": 0,
        "poziom": 1,
        "coin": 1000,
        "enemyhp": 100,
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

#===============sklep===================

class Sklep:

    def przedstawienie():
        print('Witaj w sklepie. Co chciałbyś kupić?    ')
        print(f'Masz {bio["coin"]} coinów\n')
        print('1 - Miecz: odblokowuje mocny atak  =  105 coinów')
        print('2 - Zbroja: +20 Max hp  =  200 coinów')
        print('3 - Mała potka: leczy 10 Hp  =  10 coinów')
        print('4 - Średnia potka: leczy 30 Hp  =  40 coinów')
        print('5 - Duża potka leczy: 100 Hp  =  100 coinów')
        print('-'*50)
        print(f'twoje przedmioty {myitems}')

    def kupmiecz(self, self2, myitems):
        if self["miecz"] in myitems:
            print("masz juz miecz") 
        elif self2["coin"] >= 105  and self["miecz"] not in myitems:
            myitems.append(self["miecz"])
            self2["coin"] = self2["coin"] - 105
            print(myitems)
        else:
            print("nie stac cie")

    def kupzbroje(self, self2, myitems):
        if self["zbroja"] in myitems:
            print("masz juz zbroje") 
        elif self2["coin"] >= 105 and self["zbroja"] not in myitems:
            myitems.append(self["zbroja"])
            self2["coin"] = self2["coin"] - 105
            print(myitems)
        else:
            print("nie stac cie")

    def kupmalapotka(self, self2, myitems):
        if self2["coin"] >= 10:
            myitems.append(self["mala_potka"])
            self2["coin"] = self2["coin"] - 10
            print(myitems)
        else:
            print("nie stac cie")

    def kupsredniapotka(self, self2, myitems):
        if self2["coin"] >= 40:
            myitems.append(self["srednia_potka"])
            self2["coin"] = self2["coin"] - 40
            print(myitems)
        else:
            print("nie stac cie")

    def kupduzapotka(self, self2, myitems):
        if self2["coin"] >= 100:
            myitems.append(self["duza_potka"])
            self2["coin"] = self2["coin"] - 100
            print(myitems)
        else:
            print("nie stac cie")

    def zakonczenie(myitems):
        print(myitems)

#================atak===================

class Zwykły_atak:
    def __init__(self, bio) -> None:
        if bio["hp"] > 0:
            bio["enemyhp"] = bio["enemyhp"] - randint(1,5)
            print(f"twój przeciwnik ma teraz")
            print(bio["enemyhp"])

class Podwójny_atak(Zwykły_atak):
    def __init__(self, bio, myitems):
        super().__init__(bio)
        if bio["hp"] > 0 and "miecz" in myitems and bio["lvl_miecza"] == 1:
            bio["enemyhp"] = bio["enemyhp"] - 5
            print(f"twój przeciwnik ma teraz hp")
            print(bio["enemyhp"])
        elif bio["hp"] > 0 and "miecz" in myitems and bio["lvl_miecza"] >= 2:
            bio["enemyhp"] = bio["enemyhp"] - 10
            print(f"twój przeciwnik ma teraz hp")
            print(bio["enemyhp"])
        else:
            print("nie możesz wykonać ataku, wykonany atak: zwykły atak")

#=================leczenie================

class Leczenie:
    def lek(listabio, wartoscpotki, myitems:list, potka):
        if listabio["hp"]<listabio["maxhp"] and listabio["hp"]+wartoscpotki <= listabio["maxhp"] and potka in myitems:
            listabio["hp"] = listabio["hp"] + wartoscpotki
            print("twoje hp")
            print(listabio["hp"])
            myitems.remove(potka)
        else:
            print("nie mozesz uzyc/nie masz tego itemu")

class Leczenie_mala_potka:
    def __init__(self, listabio, myitems:list) -> None:
        Leczenie.lek(listabio, 15, myitems, "mala potka")
class Leczenie_srednia_potka:
    def __init__(self, b, myitems:list) -> None:
        self.b = Leczenie.lek(b, 30, myitems, "srednia potka")
class Leczenie_duza_potka:
    def __init__(self, b, myitems:list) -> None:
        self.b = Leczenie.lek(b, 100, myitems, "duza potka")

class Wybierzleczenie:
    def wybieranieleczenia(a, bio, myitems):
        if a == 1:
            Leczenie_mala_potka(bio, myitems)
        elif a == 2:
            Leczenie_srednia_potka(bio, myitems)
        elif a == 3:
            Leczenie_duza_potka(bio, myitems)


#==============ulepszenia=================

class Upgrade:
    def wybierzulepszenie():
        print('Co chciałbyś ulepszyć?    ')
        print(f'Masz {bio["coin"]} coinów\n')
        print('1 - Miecz: + 2 Mocny atak  =  100 coinów')
        print('2 - Zbroja: + 15 Max Hp  =  175 coinów')

    def upgrady(odp, bio, myitems):
        if int(odp) == 1 and "miecz" in myitems and bio["coin"]>= 100 and bio["lvl_miecza"] == 1:
            bio["lvl_miecza"] = bio["lvl_miecza"] + 1
            bio["coin"] = bio["coin"] - 100
            print(bio["lvl_miecza"])
        elif int(odp) == 2 and "zbroja" in myitems and bio["coin"]>= 175 and bio["lvl_zbroji"] == 1:
            bio["lvl_zbroji"] = bio["lvl_zbroji"]+1
            bio["coin"] = bio["coin"] - 175
        else:
            print("nie mozesz dokonac ulepszenia")

    def konieculepszaniachyba(bio):
        print(bio["lvl_miecza"], bio["lvl_zbroji"])


#=================przeciwnicy===============


dane_przeciwnik={
    "nazwa" : "boss",
    "enemyatack" : randint(1,3),
    "enemycoin": randint(0,25),
    "enemyxp" : randint(1,30),
    "pokonane_bosy" : 0, 
    "pokonani_przeciwnicy": 0
}


class Przeciwnik():
    def enemy_atak(bio, dane):
        if bio["enemyhp"] > 0:
            bio["hp"] =bio["hp"] - dane["enemyatack"]
            print("przeciwnik zadał ci:")
            print(dane["enemyatack"])
            print("twoje hp:")
            print(bio["hp"])
        else:
            print("zabiłeś przeciwnika gratki")
            if dane["nazwa"] == "boss":
                dane["pokonane_bosy"] = dane["pokonane_bosy"] + 1
            else:
                dane["pokonani_przeciwnicy"] = dane["pokonani_przeciwnicy"] + 1
        
    def enemy_coiny(bio, dane):
        bio["coin"] = bio["coin"] + dane["enemycoin"]
        print("zdobyte coiny:")
        print(dane["enemycoin"])
        print("masz teraz:")
        print(bio["coin"])
    def enemy_xp(bio, dane):
        bio["xp"] = bio["xp"] + dane["enemyxp"]
        print("zdobyte xp:")
        print(dane["enemyxp"])
    
