from enum import Enum
from tkinter import ttk, constants, StringVar
from collections import deque

class Summa():
    def __init__(self, sovellus, syote):
        self._syote = syote
        self._sovellus = sovellus
        self._edellinen = []
        
        
    def toiminto(self):
        arvo = 0

        try:
            arvo = int(self._syote())
        except Exception:
            pass

        self._edellinen.append(self._sovellus.tulos)
        self._sovellus.plus(arvo)
        return True
        
    def kumoa(self):
        self._sovellus.aseta_arvo(self._edellinen.pop())
        
class Erotus():
    def __init__(self, sovellus, syote):
        self._syote = syote
        self._sovellus = sovellus
        self._edellinen = []
        
    def toiminto(self):
        arvo = 0

        try:
            arvo = int(self._syote())
        except Exception:
            pass
        
        self._edellinen.append(self._sovellus.tulos)
        self._sovellus.miinus(arvo)
        return True
        
    def kumoa(self):
        self._sovellus.aseta_arvo(self._edellinen.pop())
        
class Nollaus():
    def __init__(self, sovellus, syote):
        self._syote = syote
        self._sovellus = sovellus
        self._edellinen = []
        
    def toiminto(self):
        self._edellinen.append(self._sovellus.tulos)
        self._sovellus.nollaa()
        return True
        
    def kumoa(self):
        self._sovellus.aseta_arvo(self._edellinen.pop())
        
class Kumoa():
    def __init__(self, sovellus, syote):
        self._syote = syote
        self._sovellus = sovellus
        
    def toiminto(self):
        komento = self._syote.pop()
        komento.kumoa()
        return False
        
    def kumoa(self):
        self._sovellus.nollaa()
        
        
class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Kayttoliittyma:
    def __init__(self, sovellus, root):
        self._sovellus = sovellus
        self._root = root
        
        self._komento_lista = []
        self._komennot = { Komento.SUMMA: Summa(self._sovellus, self._lue_syote),
                           Komento.EROTUS: Erotus(self._sovellus, self._lue_syote),
                           Komento.NOLLAUS: Nollaus(self._sovellus, self._lue_syote),
                           Komento.KUMOA: Kumoa(self._sovellus, self._komento_lista)}
        

    def kaynnista(self):
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovellus.tulos)
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._tulos_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _nykyinen_arvo(self):
        return int(self._tulos_var.get())

    def _lue_syote(self):
        return self._syote_kentta.get()

    def _suorita_komento(self, komento):
        komento = self._komennot[komento]
        status = komento.toiminto()
        if status: 
            self._komento_lista.append(komento)

        self._kumoa_painike["state"] = constants.NORMAL if len(self._komento_lista) > 0 else constants.DISABLED
        self._nollaus_painike["state"] = constants.DISABLED if self._sovellus.tulos == 0 else constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(self._sovellus.tulos)
