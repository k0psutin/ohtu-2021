from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_tekoaly import KPSTekoaly

class Pelitehdas():
    @staticmethod
    def pvp():
        return KPSPelaajaVsPelaaja()
    
    @staticmethod
    def pv_ai():
        return KPSTekoaly()
    
    @staticmethod
    def pv_ai_impr():
        return KPSParempiTekoaly()