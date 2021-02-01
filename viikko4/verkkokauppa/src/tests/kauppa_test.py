import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self._pankki_mock = Mock()
        self._viitegeneraattori_mock = Mock()
        self._viitegeneraattori_mock.uusi.return_value = 42

        self._varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10
            if tuote_id == 3:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "ketsuppi", 2)
            if  tuote_id == 3:
                return Tuote(3, "jugurtti", 1)

        self._varasto_mock.saldo.side_effect = varasto_saldo
        self._varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self._kauppa = Kauppa(self._varasto_mock, self._pankki_mock, self._viitegeneraattori_mock)
        self._kauppa.aloita_asiointi()
        self._kauppa.lisaa_koriin(1)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        self._kauppa.tilimaksu("pekka", "12345")
        self._pankki_mock.tilisiirto.assert_called()
        
    def test_tilimaksu_kutsuu_metodia_oikeilla_muuttujilla(self):
        self._kauppa.tilimaksu("pekka", "12345")
        self._pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", "33333-44455", ANY)
        
    def test_ostetaan_kaksi_eri_tuotetta(self):
        self._kauppa.lisaa_koriin(2)
        self._kauppa.tilimaksu("pekka", "12345")
        self._pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", "33333-44455", 7)
        
    def test_ostetaan_kaksi_samaa_tuotetta(self):
        self._kauppa.lisaa_koriin(1)
        self._kauppa.tilimaksu("pekka", "12345")
        self._pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", "33333-44455", 10)
        
    def test_ostetaan_kaksi_eri_tuotetta_ja_toinen_on_loppu(self):
        self._kauppa.lisaa_koriin(3)
        self._kauppa.tilimaksu("pekka", "12345")
        self._pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", "33333-44455", 5)
        
    def test_aloita_asiointi_nollaa_edelliset_ostokset(self):
        self._kauppa.aloita_asiointi()
        self._kauppa.tilimaksu("pekka", "12345")
        self._pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", "33333-44455", 0)
        
    def test_kauppa_pyytaa_uuden_viitenumeron_jokaiselle_maksutapahtumalle(self):
        self._kauppa.tilimaksu("pekka", "12345")
        self._viitegeneraattori_mock.uusi.assert_called()
        
    def test_korista_poistaminen_palauttaa_varastoon(self):
        self._kauppa.poista_korista(1)
        self._varasto_mock.palauta_varastoon.assert_called()
        