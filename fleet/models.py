# fleet/models.py

from django.db import models


class Pojazd(models.Model):
    """
    Model reprezentujący pojazd w firmie.

    Atrybuty:
    - marka_pojazdu (str): Marka pojazdu.
    - model_pojazdu (str): Model pojazdu.
    - rodzaj_pojazdu (str): Rodzaj pojazdu (osobowy, ciężarowy, naczepa).
    - rok_produkcji (int): Rok produkcji pojazdu.
    - nr_rejestracyjny (str): Numer rejestracyjny pojazdu.
    - rok_pierwszej_rejestracji (int): Rok pierwszej rejestracji pojazdu.
    - nr_vin (str): Numer identyfikacyjny pojazdu.
    - moc (float): Moc pojazdu w koniach mechanicznych.
    - poj_silnika (float): Pojemność silnika w litrach.
    - paliwo (str): Rodzaj paliwa (benzyna, olej napędowy).
    - wlasciciel (str): Własnościca pojazdu (srodek własny, leasing).
    """
    marka_pojazdu = models.CharField(max_length=255)
    model_pojazdu = models.CharField(max_length=255)
    rodzaj_pojazdu = models.CharField(max_length=20, choices=[('osobowy', 'Osobowy'), ('ciężarowy', 'Ciężarowy'),
                                                              ('naczepa', 'Naczepa'), ('ciągnik siodłowy', 'ciągnik sidołowy')])
    rok_produkcji = models.IntegerField()
    nr_rejestracyjny = models.CharField(max_length=20)
    rok_pierwszej_rejestracji = models.IntegerField()
    nr_vin = models.CharField(max_length=17)
    moc = models.FloatField()
    poj_silnika = models.FloatField()
    PALIWO_CHOICES = [('benzyna', 'Pb95'), ('olej napędowy', 'ON')]
    paliwo = models.CharField(max_length=15, choices=PALIWO_CHOICES)
    WLASNOSC_CHOICES = [('srodek_wlasny', 'Własność Spółki'), ('leasing', 'LEASING')]
    wlasciciel = models.CharField(max_length=15, choices=WLASNOSC_CHOICES)

    def __str__(self):
        return f'{self.marka_pojazdu} {self.model_pojazdu}'


# noinspection NonAsciiCharacters
class KartaPaliwowa(models.Model):
    """
    Model reprezentujący kartę paliwową.

    Atrybuty:
    - nr_karty (str): Numer karty paliwowej.
    - nr_rejestracyjny (str): Numer rejestracyjny pojazdu przypisanego do karty.
    - data_ważności (Date): Data ważności karty.
    - kod_pin (str): Kod PIN karty.
    - typ_karty (str): Typ karty (Samochód ‘S’, Kierowca ‘K’).
    - status (bool): Status karty (aktywna lub nieaktywna).
    - limit (float): Limit wydatków na karcie.
    """
    nr_karty = models.CharField(max_length=255)
    nr_rejestracyjny = models.CharField(max_length=20)
    data_ważności = models.DateField()
    kod_pin = models.CharField(max_length=4)
    TYP_CHOICES = [('S', 'Samochód'), ('K', 'Kierowca')]
    typ_karty = models.CharField(max_length=1, choices=TYP_CHOICES)
    status = models.BooleanField(default=True)
    LIMIT_CHOICES = [
        ('C_3/60+120', 'C_3/60+120'),
        ('C_3/60+120+AutoGaz', 'C_3/60+120+AutoGaz'),
        ('C_1/75+120', 'C_1/75+120'),
        ('C_1/600+120', 'C_1/600+120'),
    ]
    limit = models.CharField(max_length=50, choices=LIMIT_CHOICES, null=True, blank=True)

    def __str__(self):
        return f'{self.nr_karty} - {self.typ_karty}'


class TowarzystwoUbezpieczeniowe(models.Model):
    """
    Model reprezentujący towarzystwo ubezpieczeniowe.

    Atrybuty:
    - nazwa (str): Nazwa towarzystwa ubezpieczeniowego.
    - ulica (str): Ulica siedziby towarzystwa.
    - miasto (str): Miasto siedziby towarzystwa.
    - kod_pocztowy (str): Kod pocztowy siedziby towarzystwa.
    """
    nazwa = models.CharField(max_length=255)
    ulica = models.CharField(max_length=255)
    miasto = models.CharField(max_length=255)
    kod_pocztowy = models.CharField(max_length=10)

    def __str__(self):
        return self.nazwa

class Warsztat(models.Model):
    """
    Model reprezentujący warsztat samochodowy.

    Atrybuty:
    - nazwa (str): Nazwa warsztatu.
    - adres_ulica (str): Ulica, na której znajduje się warsztat.
    - adres_miasto (str): Miasto, w którym znajduje się warsztat.
    - adres_kod_pocztowy (str): Kod pocztowy warsztatu.
    - nip (str): Numer identyfikacyjny podatkowy warsztatu.
    - regon (str): Numer identyfikacyjny statystyczny warsztatu.
    - telefon (str): Numer telefonu do warsztatu.
    - email (str): Adres e-mail warsztatu.
    - osoba_kontaktowa (str): Imię i nazwisko osoby kontaktowej w warsztacie.
    """
    nazwa = models.CharField(max_length=255)
    adres_ulica = models.CharField(max_length=255)
    adres_miasto = models.CharField(max_length=255)
    adres_kod_pocztowy = models.CharField(max_length=10)
    nip = models.CharField(max_length=10)
    regon = models.CharField(max_length=14)
    telefon = models.CharField(max_length=15)
    email = models.EmailField()
    osoba_kontaktowa = models.CharField(max_length=255)

    def __str__(self):
        return self.nazwa

class Pracownik(models.Model):
    """
    Model reprezentujący pracownika.

    Atrybuty:
    - imie (str): Imię pracownika.
    - nazwisko (str): Nazwisko pracownika.
    - stanowisko (str): Stanowisko pracownika.
    - dział (str): Dział, w którym pracuje pracownik.
    - nr_rej_samochodu (str): Numer rejestracyjny samochodu przypisanego pracownikowi.
    - koszty_dzialu (int): Koszty działu, do którego należy pracownik.
    """
    imie = models.CharField(max_length=255)
    nazwisko = models.CharField(max_length=255)
    stanowisko = models.CharField(max_length=255)
    dzial = models.CharField(max_length=255)
    nr_rej_samochodu = models.CharField(max_length=20)
    Stanowisko_kosztow_CHOICES = [
        (2000, '2000- KOSZTY POŚREDNIE PRODUKCJI'),
        (2100, '2100- KOSZTY UTRZYMANIA RUCHU'),
        (2200, '2200-KOSZTY NADZORU PRODUKCYJNEGO'),
        (2210, '2210-KOSZTY GŁÓWNEGO SPAWALNIKA'),
        (2230, '2230-KOSZTY WŁASNYCH SZKOLEŃ I PRAKTYK'),
        (3300, '3300-KOSZTY NARZĘDZIOWNI'),
        (4000, '4000-KOSZTY DZIAŁU KONTROLI WEWNĘTRZNEJ'),
        (5100, '5100-DYREKTOR DS.HANDLOWYCH'),
        (5110, '5110-KOSZTY DZIAŁU OFERTOWEGO'),
        (5120, '5120-KOSZTY DZIAŁU HANDLOWEGO'),
        (5200, '5200-KOSZTY DZIAŁU ZAKUPOW'),
        (5300, '5300-KOSZTY DZIALU MARKETINGU'),
        (5400, '5400-KOSZTY GOSPOD.MATER., LOGISTYKI I SPEDYCJI'),
        (6100, '6100-DYREKTOR DS. PRODUKCJI, DS. PRZYGOT.I REALIZ.PRODU'),
        (6110, '6110-KOSZTY DZIAŁU PRODUKCJI'),
        (6120, '6120-KOSZTY DZIAŁU PRZYGOTOWANIA'),
        (6130, '6130-KOSZTY DZIAŁU REALIZACJI'),
        (6200, '6200-KOSZTY DZIAŁU PLANOWANIA I CYFRYZACJI'),
        (6300, '6300-KOSZTY DZIAŁU TECHNICZNEGO'),
        (6410, '6410-KOSZTY DZIALU MONTAZOWEGO'),
        (6500, '6500-KOSZTY LABORATORIUM'),
        (6510, '6510-KOSZTY DZIAŁU KONTROLI JAKOŚCI'),
        (6520, '6520-KOSZTY DZIALU ZAPEWN.JAKOŚCI, BHP I OCHRONY ś'),
        (6600, '6600-KOSZTY DZIAŁU INWESTYCJI'),
        (6700, '6700-KOSZTY Z-CY DYREKTORA DS. TECHNOLOGII'),
        (7000, '7000-KOSZTY RADY NADZORCZEJ'),
        (7100, '7100-KOSZTY ZARZĄDU'),
        (7110, '7110-KOSZTY BIURA ZARZĄDU'),
        (7120, '7120-KOSZTY DORADCÓW ZARZADU'),
        (7300, '7300-KOSZTY OBSŁUGI PRAWNEJ'),
        (7310, '7310-KOSZTY DZIAŁU UMÓW'),
        (7400, '7400-KOSZTY DZIAŁU FINANSOWO - KSIĘGOWEGO'),
        (7510, '7510-KOSZTY DZIAŁU KONTROLINGU'),
        (7600, '7600-KOSZTY WYDZIAłU ADMINISTRACYJNEGO'),
        (7700, '7700-KOSZTY DZIAŁU INFORMATYKI'),
        (7800, '7800-KOSZTY DZIAŁU PŁAC I ZZL'),
    ]
    koszty_działu = models.IntegerField(choices=Stanowisko_kosztow_CHOICES)

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'

    class Polisa(models.Model):
        """
        Model reprezentujący polisę ubezpieczeniową.

        Atrybuty:
        - nr_polisy (str): Numer polisy.
        - towarzystwo_ubezpieczeniowe (ForeignKey): Towarzystwo ubezpieczeniowe przypisane do polisy.
        - nr_rej_pojazdu (ForeignKey): Numer rejestracyjny pojazdu przypisanego do polisy.
        - zakres (str): Zakres ubezpieczenia (złoty, platynowy, złoty+).
        - data_rozpoczecia (Date): Data rozpoczęcia obowiązywania polisy.
        - data_zakonczenia (Date): Data zakończenia obowiązywania polisy.
        """
        nr_polisy = models.CharField(max_length=255)
        towarzystwo_ubezpieczeniowe = models.ForeignKey(TowarzystwoUbezpieczeniowe, on_delete=models.CASCADE)
        nr_rej_pojazdu = models.ForeignKey(Pojazd, on_delete=models.CASCADE)
        ZAKRES_CHOICES = [('złoty', 'Złoty'), ('platynowy', 'Platynowy'), ('złoty+', 'Złoty+')]
        zakres = models.CharField(max_length=15, choices=ZAKRES_CHOICES)
        data_rozpoczecia = models.DateField()
        data_zakonczenia = models.DateField()

        def __str__(self):
            return self.nr_polisy

    class BadanieTechniczne(models.Model):
        """
        Model reprezentujący badanie techniczne.

        Atrybuty:
        - nr_przegladu (str): Numer przeglądu serwisowego.
        - data_przegladu (Date): Data wykonania przeglądu.
        - notatki (str): Dodatkowe notatki z przeglądu.
        - pojazd (ForeignKey): Pojazd, którego dotyczy przegląd serwisowy.
        """
        nr_przegladu = models.CharField(max_length=255)
        data_przegladu = models.DateField()
        notatki = models.TextField()
        pojazd = models.ForeignKey(Pojazd, on_delete=models.CASCADE)

        def __str__(self):
            return self.nr_przegladu

    class Naprawa(models.Model):
        """
        Model reprezentujący naprawe pojazdu.

        Atrybuty:
        - nr_naprawy (str): Numer naprawy.
        - data_naprawy (Date): Data wykonania naprawy.
        - notatki (str): Dodatkowe notatki z naprawy.
        - pojazd (ForeignKey): Pojazd, którego dotyczy naprawa.
        """
        nr_naprawy = models.CharField(max_length=255)
        data_naprawy = models.DateField()
        notatki = models.TextField()
        pojazd = models.ForeignKey(Pojazd, on_delete=models.CASCADE)

        def __str__(self):
            return self.nr_naprawy

class Ogumienie(models.Model):
    """
    Model reprezentujący ogumienie pojazdu.

    Atrybuty:
    - nr_rejestracyjny (str): Numer rejestracyjny pojazdu przypisanego do ogumienia.
    - rodzaj (str): Rodzaj ogumienia (letnie, zimowe, całoroczne).
    - rozmiar (str): Rozmiar opony.
    - stan_lewy_przod (str): Stan opony lewy przód.
    - stan_lewy_tyl (str): Stan opony lewy tył.
    - stan_prawy_przod (str): Stan opony prawy przód.
    - stan_prawy_tyl (str): Stan opony prawy tył.
    - uwagi (str): Dodatkowe uwagi dotyczące ogumienia.
    """
    nr_rejestracyjny = models.CharField(max_length=20)
    RODZAJ_CHOICES = [('letnie', 'Letnie'), ('zimowe', 'Zimowe'), ('całoroczne', 'Całoroczne')]
    rodzaj = models.CharField(max_length=15, choices=RODZAJ_CHOICES)
    rozmiar = models.CharField(max_length=20)
    STAN_CHOICES = [('dobry', 'Dobry'), ('do wymiany', 'Do wymiany'), ('uszkodzony', 'Uszkodzony')]
    stan_lewy_przod = models.CharField(max_length=15, choices=STAN_CHOICES)
    stan_lewy_tyl = models.CharField(max_length=15, choices=STAN_CHOICES)
    stan_prawy_przod = models.CharField(max_length=15, choices=STAN_CHOICES)
    stan_prawy_tyl = models.CharField(max_length=15, choices=STAN_CHOICES)
    uwagi = models.TextField()

    def __str__(self):
        return f'Ogumienie - {self.nr_rejestracyjny} - {self.rodzaj}'

class Koszt(models.Model):
    """
    Model reprezentujący koszt związany z pojazdem.

    Atrybuty:
    - data (Date): Data wystąpienia kosztu.
    - kwota (Decimal): Kwota kosztu.
    - opis (str): Opis kosztu.
    - czesci (Decimal): Kwota kosztu związanego z zakupem części.
    - robocizna (Decimal): Kwota kosztu związanego z kosztami robocizny.
    - suma (Decimal): Suma kosztów części i robocizny.
    - pojazd (ForeignKey): Pojazd, z którym powiązany jest koszt.
    """
    data = models.DateField()
    kwota = models.DecimalField(max_digits=10, decimal_places=2)
    opis = models.TextField()
    czesci = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    robocizna = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    suma = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    pojazd = models.ForeignKey('Pojazd', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.suma = self.czesci + self.robocizna
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.opis} - {self.kwota} PLN ({self.data})'