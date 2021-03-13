from kps import KPS

class KPSTekoaly(KPS):
    def __init__(self):
        super().__init__()
    
    def _toisen_siirto(self):
        self._tokan_siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {self._tokan_siirto}")