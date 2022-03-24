import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kassa_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_saldo_aluksi_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edulliset_aluksi_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_aluksi_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maksu_riittava_edullisesti_kateisella(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(vaihtoraha, 260)

    def test_maksu_riittava_maukkaasti_kateisella(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(vaihtoraha, 100)

    def test_maksu_riittava_lounaat_kasvaa_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maksu_ei_riita_edullisesti_kateisella(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(vaihtoraha, 230)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maksu_ei_riita_maukkaasti_kateisella(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(50)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(vaihtoraha, 50)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maksu_riittava_edullisesti_kortilla(self):
        kortti = Maksukortti(500)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), True)
        self.assertEqual(kortti.saldo, 260)

    def test_maksu_riittava_maukkaasti_kortilla(self):
        kortti = Maksukortti(500)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), True)
        self.assertEqual(kortti.saldo, 100)

    def test_maksu_riittava_lounaat_kasvaa_kortilla(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maksu_ei_riita_lounaat_ei_kasvaa_kortilla(self):
        kortti = Maksukortti(5)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortti_ei_vaikuta_kassaan(self):
        self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(500))
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_lataus(self):
        kortti = Maksukortti(50)
        self.kassapaate.lataa_rahaa_kortille(kortti, 500)
        self.assertEqual(kortti.saldo, 550)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_kortille_lataus_nolla(self):
        kortti = Maksukortti(50)
        self.kassapaate.lataa_rahaa_kortille(kortti, -50)
        self.assertEqual(kortti.saldo, 50)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)



