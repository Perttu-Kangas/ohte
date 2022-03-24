import unittest
from maksukortti import Maksukortti


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_aluksi_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_saldon_kasvatus_toimii(self):
        self.maksukortti.lataa_rahaa(5)
        self.assertEqual(self.maksukortti.saldo, 15)

    def test_saldon_vahennys(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(self.maksukortti.saldo, 5)

    def test_saldon_liiallinen_vahennys(self):
        self.maksukortti.ota_rahaa(11)
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_ota_rahaa_tosi(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5), True)

    def test_ota_rahaa_epatosi(self):
        self.assertEqual(self.maksukortti.ota_rahaa(11), False)

    def test_str(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")