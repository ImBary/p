class Testowy():
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
    def show(self):
        print( self.imie + " " + self.nazwisko)

emp = Testowy('Karol', "Czomber")

emp.show()
    
