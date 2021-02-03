class IntJoukko:
    def __init__(self, lukujono=None):
            self.lukujono = [] if lukujono is None else lukujono

    def kuuluu(self, luku):
        return luku in self.lukujono

    def lisaa(self, luku):
        if not self.kuuluu(luku):
            self.lukujono.append(luku)

    def poista(self, luku):
        if not self.kuuluu(luku):
            return False
        self.lukujono = list(filter(lambda arvo: arvo != luku, self.lukujono))
        return True

    def mahtavuus(self):
        return len(self.lukujono)

    def to_int_list(self):
        return self.lukujono[:]

    @staticmethod
    def yhdiste(a_joukko, b_joukko):
        return IntJoukko(lukujono=[*a_joukko.lukujono,*b_joukko.lukujono])

    @staticmethod
    def leikkaus(a_joukko, b_joukko):
        return IntJoukko(lukujono=[luku for luku in a_joukko.lukujono if luku in b_joukko.lukujono])

    @staticmethod
    def erotus(a_joukko, b_joukko):
        return IntJoukko(lukujono=[luku for luku in a_joukko.lukujono if luku not in b_joukko.lukujono])

    def __str__(self):
        return str(set(self.lukujono)) if self.mahtavuus() > 0 else "{}"
