from kps import KPS

class KPSParempiTekoaly(KPS):
    def __init__(self):
        super().__init__()
        
    def _toisen_siirto(self):
        self._tokan_siirto = self._parempi_tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {self._tokan_siirto}")
        self._parempi_tekoaly.aseta_siirto(self._ekan_siirto)