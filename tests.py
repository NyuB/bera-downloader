from meteo_france_api import MassifDay, MassifDayAvailabilty, BERAClient, DateYMD
import unittest

class BERAClientInternalTest(unittest.TestCase):
    def test_single_available_date_get_available_returns_single_date(self):
        input_date = "20220101"
        massif = MassifDayAvailabilty("Vanoise", [input_date])
        output_massif_day = massif.get_latest_available()
        self.assertEqual(output_massif_day.date, input_date)

    def test_two_ascend_sorted_dates_get_available_returns_latest_date(self):
        input_dates = ["20220101", "20220102"]
        massif = MassifDayAvailabilty("Vanoise", input_dates)
        output_massif_day = massif.get_latest_available()
        self.assertEqual(output_massif_day.date,  "20220102")

    def test_two_descend_sorted_dates_get_available_returns_latest_date(self):
        input_dates = ["20220102", "20220101"]
        massif = MassifDayAvailabilty("Vanoise", input_dates)
        output_massif_day = massif.get_latest_available()
        self.assertEqual(output_massif_day.date,  "20220102")
    
    def test_bera_client_massif_json_url_2022_3_4_returns_donneslibres_Pdf_BRA_bra20220304_json(self):
        client = BERAClient(meteo_france_base_url="http://testmeteo")
        day = DateYMD(2022, 3, 4)
        massif_json_url = client.build_bera_massifs_json_url(day)
        self.assertEqual(massif_json_url, "http://testmeteo/donnees_libres/Pdf/BRA/bra.20220304.json")

    def test_bera_client_bera_pdf_url_Vercors_20220304_returns_donneslibres_Pdf_BRA_BRA_VERCORS20220304_pdf(self):
        client = BERAClient(meteo_france_base_url="http://testmeteo")
        massif_json_url = client.build_bera_pdf_url("Vercors", "20220304")
        self.assertEqual(massif_json_url, "http://testmeteo/donnees_libres/Pdf/BRA/BRA.VERCORS.20220304.pdf")

class BERAClientIntegrationTest(unittest.TestCase):
    
    client = BERAClient()

    def assertPdfBytesEqualFileContent(self, actual_bytes: bytes, file_path: str):
        with open(file_path, 'rb') as test_file:
            self.assertTrue(test_file.readable())
            full_pdf_expected = test_file.read()
            self.assertEqual(actual_bytes, full_pdf_expected)

    def test_get_bera_for_massif_day_belledonne_20220101142303_returns_20220101142303_exact_pdf(self):
        full_pdf = self.client.get_bera_for_massif_day(MassifDay("belledonne", "20220101142303"))
        self.assertPdfBytesEqualFileContent(full_pdf, "resources/tests/BRA.BELLEDONNE.20220101142303.pdf")
    
    def test_get_latest_bera_for_massif_day_belledonne_2022_01_01_returns_20220101142303_exact_pdf(self):
        full_pdf = self.client.get_latest_bera_for_massif_day("Belledonne", DateYMD(2022, 1, 1))
        self.assertPdfBytesEqualFileContent(full_pdf, "resources/tests/BRA.BELLEDONNE.20220101142303.pdf")
