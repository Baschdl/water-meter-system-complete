import unittest
from lib.ZaehlerstandClass import Zaehlerstand

class TestZaehlerstand(unittest.TestCase):
    def test_checkConsistency(self):
        zaehlerstand = Zaehlerstand()
        zaehlerstand.LastVorkomma = '?'
        zaehlerstand.akt_vorkomma = '?'
        zaehlerstand.ConsistencyEnabled = True
        error, errortxt = zaehlerstand.checkConsistency()
        self.assertEqual(error, '?')
        self.assertEqual(errortxt, '?')
        self.fail()

    def test_AnalogReadoutToValue(self):
        zaehlerstand = Zaehlerstand()
        result = zaehlerstand.AnalogReadoutToValue(res_analog='?')
        self.assertEqual(result, 5)
        self.fail()

    def test_DigitalReadoutToValue(self):
        zaehlerstand = Zaehlerstand()
        zaehlerstand.LastVorkomma = '?'
        zaehlerstand.LastNachkomma = '?'
        result = zaehlerstand.DigitalReadoutToValue(res_digital='', UsePreValue=True, lastnachkomma='', aktnachkomma='')
        self.assertEqual(result, 6)
        self.fail()


if __name__ == '__main__':
    unittest.main()