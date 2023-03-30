import json

class Bucatarie:
    def __init__(self):
        #with open("data/Inventar.json") as f:
        #self.inventar = json.load(f)
        self.inventar = {}
    def initializeaza_inventar(self):
        with open("data/Inventar.json") as f:
            self.inventar = json.load(f)
        return self.inventar
    def adauga_produs(self, nume_produs, cantitate):
        if nume_produs in self.inventar.keys():
            self.inventar[nume_produs] += cantitate
        else:
            self.inventar[nume_produs] = cantitate

    def salvare_inventar(self):
        with open("data/Inventar.json", "w") as f:
            json.dump(self.inventar, f)

    def scadere_produs(self, nume_produs, cantitate):
        if nume_produs in self.inventar:
            if self.inventar[nume_produs] >= cantitate:
                self.inventar[nume_produs] -= cantitate
            else:
                print("Nu exista suficient {} in inventar.".format(nume_produs))
        else:
            print("Ingredientul {} nu exista in inventar.".format(nume_produs))

