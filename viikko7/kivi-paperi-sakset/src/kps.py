from tuomari import tuomari
from tekoaly import tekoaly
from tekoaly_parannettu import paranneltu_tekoaly

class KPS:
    def __init__(self):
        self._tuomari = tuomari 
        self._tekoaly = tekoaly
        self._parempi_tekoaly = paranneltu_tekoaly
        self._ekan_siirto = ''
        self._tokan_siirto = ''
    
    def pelaa(self):
        def onko_ok_siirto(siirto):
            return siirto == "k" or siirto == "p" or siirto == "s"
        self._ensimmaisen_siirto()
        self._toisen_siirto()
        
        while onko_ok_siirto(self._ekan_siirto) and onko_ok_siirto(self._tokan_siirto):
            self._tuomari.kirjaa_siirto(self._ekan_siirto, self._tokan_siirto)
            print(self._tuomari)
            
            self._ensimmaisen_siirto()
            self._toisen_siirto()
            
        print("Kiitos!")
        print(self._tuomari)
    
    def _ensimmaisen_siirto(self):
        self._ekan_siirto = input("Ensimmäisen siirto: ")
        
    def _toisen_siirto(self):
        self._tokan_siirto = input("Toisen siirto: ")