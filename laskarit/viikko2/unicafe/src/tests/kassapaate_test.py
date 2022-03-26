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
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_maksu_riittava_vaihtoraha_edullisesti_kateisella(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(vaihtoraha, 260)

    def test_maksu_riittava_maukkaasti_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_maksu_riittava_vaihtoraha_maukkaasti_kateisella(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)

    def test_maksu_kasvattaa_maukkaita_kateinen(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maksu_kasvattaa_edullisia_kateinen(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maksu_ei_riita_edullisesti_kateisella_kassa(self):
        self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maksu_ei_riita_edullisesti_kateisella_vaihtoraha(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(vaihtoraha, 230)

    def test_maksu_ei_riita_edullisesti_kateisella_edulliset_maara(self):
        self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maksu_ei_riita_maukkaasti_kateisella_kassa(self):
        self.kassapaate.syo_maukkaasti_kateisella(50)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maksu_ei_riita_maukkaasti_kateisella_vaihtoraha(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(50)
        self.assertEqual(vaihtoraha, 50)

    def test_maksu_ei_riita_maukkaasti_kateisella_maukkaat_maara(self):
        self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maksu_riittava_edullisesti_kortilla(self):
        kortti = Maksukortti(500)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), True)

    def test_maksu_riittava_edullisesti_kortilla_kortin_saldo(self):
        kortti = Maksukortti(500)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 260)

    def test_maksu_riittava_maukkaasti_kortilla(self):
        kortti = Maksukortti(500)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), True)

    def test_maksu_riittava_maukkaasti_kortilla_kortin_saldo(self):
        kortti = Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 100)

    def test_maksu_riittava_edulliset_kasvaa_kortilla(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maksu_riittava_maukkaat_kasvaa_kortilla(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maksu_ei_riittava_edulliset_ei_kasva_kortilla(self):
        kortti = Maksukortti(5)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maksu_ei_riittava_maukkaat_ei_kasvaa_kortilla(self):
        kortti = Maksukortti(5)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortti_ei_vaikuta_kassaan(self):
        self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(500))
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_lataus_saldo(self):
        kortti = Maksukortti(50)
        self.kassapaate.lataa_rahaa_kortille(kortti, 500)
        self.assertEqual(kortti.saldo, 550)

    def test_kortille_lataus_kassa(self):
        kortti = Maksukortti(50)
        self.kassapaate.lataa_rahaa_kortille(kortti, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_kortille_lataus_negatiivinen_saldo(self):
        kortti = Maksukortti(50)
        self.kassapaate.lataa_rahaa_kortille(kortti, -50)
        self.assertEqual(kortti.saldo, 50)

    def test_kortille_lataus_negatiivinen_kassa(self):
        kortti = Maksukortti(50)
        self.kassapaate.lataa_rahaa_kortille(kortti, -50)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
