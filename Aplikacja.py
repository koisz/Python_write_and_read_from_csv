import csv

class Pacjent:
    """
    Klasa Pacjent pozwalająca tworzyć obiekty jako pacjentów.

    Atrybuty:
        __imie (str):
        __nazwisko(str): Nazwisko pacjenta
        __pesel (tuple): Pesel pacjenta
        __adres (str): Adres zamieszkania
        __dataUrodzenia (str): Data urodzenia pacjenta
        __lzabieg (int): Liczba zabiegów
        __zabieg (list): Lista zabiegów
    """

    def __init__(self, imie, nazwisko, pesel, adres, dataUrodzenia):
        """
        Inicjalizuje obiekt Pacjent

        :param imie: Imię pacjenta
        :param nazwisko: Nazwisko pacjenta
        :param pesel: Pesel pacjenta
        :param adres: Adres zamieszkania
        :param dataUrodzenia: Data urodzenia pacjenta
        """
        self.__imie=imie
        self.__nazwisko=nazwisko
        self.__pesel=tuple(pesel)
        self.__adres=adres
        self.__dataUrodzenia=dataUrodzenia
        self.__lzabieg = 0
        self.__zabieg = []

    def __str__(self):
        """
        Przekształca dane pacjenta na tekst odpowiedni do zapisania w pliku

        :return: Dane pacjenta jako tekst
        """
        return f"{self.__imie},{self.__nazwisko},{self.peselNaString()},{self.__adres},{self.__dataUrodzenia},{self.__lzabieg},{self.wypiszZabiegi()}"

    def getImie(self):
        """
        Zwraca imię pacjenta
        :return: imię pacjenta
        """
        return self.__imie

    def getNazwisko(self):
        """
        Zwraca nazwisko pacjenta
        :return: nazwisko pacjenta
        """
        return self.__nazwisko

    def setLiczbaZabiegow(self,l):
        """
        Ustawia liczbę zabiegów pacjenta
        :param l: liczba zabiegów
        """
        self.__lzabieg=l
    def getLiczbaZabiegow(self):
        """
        Zwraca liczbę zabiegów pacjenta
        :return: liczba zabiegów
        """
        return self.__lzabieg

    def dodajZabieg(self, zabieg):
            """
            Dodaje zabieg do listy zabiegów pacjenta

            :param zabieg:
            """
            self.__zabieg.append(zabieg)


    def peselNaString(self):
        """
        Zmienia pesel pacjenta z krotki na string

        :return: Pesel pacjenta jako string
        """
        pesel=""
        for i in self.__pesel:
            pesel=pesel+i
        return pesel

    def wypiszDane(self):
        """
        Wypisuje dane pacjenta
        """
        if self.__lzabieg==0:
            print(f"{self.__imie} {self.__nazwisko}\n"
                  f"PESEL: {self.peselNaString()}\n"
                  f"Data urodzenia: {self.__dataUrodzenia}\n"
                  f"Adres zamieszkania: {self.__adres}\n"
                  f"Brak zabiegów")
        else:
            print(f"{self.__imie} {self.__nazwisko}\n"
                f"PESEL: {self.peselNaString()}\n"
                f"Data urodzenia: {self.__dataUrodzenia}\n"
                f"Adres zamieszkania: {self.__adres}\n"
                f"Zabiegi:{self.wypiszZabiegi()}")

    def wypiszZabiegi(self):
        """
        Wypisuje zabiegi z listy
        :return: Wszystkie zabiegi po przecinku w formie jednego stringa
        """
        p=""
        if self.__lzabieg != 0:
            for n in self.__zabieg:
                if n==self.__zabieg[-1]:
                    p = p + n
                    return (f"{p}")
                p = p + n + ','
            return (f"{p}")
        return ("")

class App:
    """
    Klasa App tworząca aplikację do zarządzania informacją medyczną, gromadząca dane osobowe

    Atrybuty:
        plik (str): Nazwa pliku csv z którego pobierane są dane pacjentów.
        pacjenci (list): Lista obiektów klasy Pacjent zawierająca dane pacjentów.
    """
    def __init__(self, nazwaPliku):
        """
        Inicjalizuje obiekt App, wczytuje pacjentów wraz z danymi z pliku csv oraz wypisuje listę pacjentów

        :param nazwaPliku: Nazwa pliku csv zawierającego dane
        """
        self.plik=nazwaPliku
        try:
            self.pacjenci = self.wczytajPacjentów(self.plik)
            self.wypiszPacjentów(self.pacjenci)
        except OSError as er:
            print(er)

    def menu(self,lista):
        """
        Metoda tworząca menu aplikacji
        :param lista: wczytana lista pacjentów
        """
        print("\n1 - Wybierz pacjenta, ktorego dane chcesz zobaczyć i dodać zabieg\n2 - Dodaj pacjenta\n0 - Wyjdź z aplikacji ")
        while(1):
            try:
                j=int(input())
                if j==0:
                    exit(0)
                elif j==1:
                    while(1):
                        print("Wpisz imię pacjenta: ")
                        p = input()
                        print("Wpisz naziwsko pacjenta: ")
                        po = input()
                        for j in lista:
                            if j.getNazwisko() == po:
                                if j.getImie() == p:
                                    self.pokazDanePacjenta(j)
                    print("Prosze podać poprawne imię i nazwisko pacjenta z listy!\n")
                elif j==2:
                    self.dodajPacjenta()
                else:
                    raise ValueError
            except ValueError as err:
                print("Wprowadź poprawny numer!")
                continue

    def zapiszDoPliku(self):
        """
        Metoda zapisuje listę pacjentów do pliku
        """
        try:
            with open(self.plik, "wt", newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter="\n")
                writer.writerow(self.pacjenci)
        except FileNotFoundError as er:
            print("Nie znaleziono pliku o takiej nazwie")

    def dodajPacjenta(self):
        """
        Metoda dodająca pacjenta do pliku
        """
        print("Imię pacjenta:")
        a=input()
        print("Naziwsko pacjenta:")
        b=input()
        while 1:
            print("Pesel:")
            c=input()
            if len(c)==11 and c.isdigit():
                break
            print("Wprowadzono błędnie pesel")
        print("Adres zamieszkania:")
        f=input()
        d="ul."+f
        print("Data urodzenia:")
        while 1:
            try:
                print("Dzień:")
                h=int(input())
                if h<32 and h>0:
                    h=str(h)
                    break
                raise ValueError
            except ValueError as e:
                print("Wprowadź poprawnie dzień!")
        while 1:
            try:
                print("Miesiąc:")
                m=int(input())
                if m>0 and m<13:
                    m=str(m)
                    break
                raise ValueError
            except ValueError as err:
                print("Wprowadź poprawnie miesiąc!")
        while 1:
            try:
                print("Rok:")
                v=int(input())
                if v<2023 and v>1900:
                    v=str(v)
                    break
                raise ValueError
            except ValueError as err:
                print("Wprowadź poprawnie dzień!")
        e= h+'.'+m+'.'+v
        self.pacjenci.append(Pacjent(a,b,c,d,e))
        self.zapiszDoPliku()
        self.wypiszPacjentów(self.pacjenci)

    def wczytajPacjentów(self, nazwaPilku):
        """
        Metoda wczytująca wszytskich pacjentów z pliku

        :param nazwaPilku: Nazwa pliku, w którym znajdują się informacje o pacjentach
        :return: Lista pacjentów
        """
        pacjenci = []
        try:
            with open(nazwaPilku,"r",encoding='utf-8')as file:
                reader = csv.reader(file, delimiter=",")
                for r in reader:
                    a=Pacjent(r[0],r[1],r[2],r[3],r[4])
                    d=int(r[5])
                    a.setLiczbaZabiegow(d)
                    if d !=0:
                        for n in range(6,d+6):
                            a.dodajZabieg(r[n])
                    pacjenci.append(a)
        except FileNotFoundError as er:
            print("Nie znaleziono pliku o takiej nazwie")
        return pacjenci

    def wypiszPacjentów(self, lista):
        """
        Metoda wypisująca liste pacjentów, umożliwiająca wybranie pacjenta

        :param lista: Lista pacjentów
        """
        while 1:
            print("Lista pacjentów:")
            a=1
            for i in lista:
                print(f"{a}." + i.getImie(), i.getNazwisko())
                a = a + 1
            self.menu(lista)

    def pokazDanePacjenta(self,Pacjent):
        """
        Metoda pokazująca dane wybranego pacjenta, umożliwiająca dodanie nowego zabiegu.

        :param Pacjent: Obiekt pacjent, którego dane są wypisywane
        """
        Pacjent.wypiszDane()
        while 1:
            print("\nCzy chcesz dodać nowy zabieg [Tak/Nie]?")
            v = input()
            if v == "Tak":
                self.dodajZabieg(Pacjent)
            elif v == "Nie":
                print("\n")
                self.wypiszPacjentów(self.pacjenci)

    def dodajZabieg(self, Pacjent):
        """
        Metoda pozwalająca na dodanie zabiegu do listy dla wybranego wcześniej pacjenta oraz zapisanie go w pliku csv
        :param Pacjent: Referencja na wybrany wcześniej obiekt Pacjent
        """
        print("Podaj nazwę zabiegu:")
        zabieg=input()
        if zabieg == "close":
            exit(0)
        Pacjent.dodajZabieg(zabieg)
        Pacjent.setLiczbaZabiegow(1 + Pacjent.getLiczbaZabiegow())
        self.zapiszDoPliku()
        print("\nDane pacjenta po dodaniu zabiegu:\n")
        Pacjent.wypiszDane()
        print("\n")
        self.wypiszPacjentów(self.pacjenci)

if __name__ == '__main__':
    App("Pacjenci")