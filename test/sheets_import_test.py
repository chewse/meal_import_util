from unittest import TestCase
from sheets.sheets_import import SheetsImporter
import importlib
from google.oauth2.service_account import Credentials
from googleapiclient import discovery
from unittest.mock import MagicMock


class TestSheetsImporter(TestCase):

    def test_google_lib_import(self):
        """Check to be sure the google api client package is available"""
        google_lib = importlib.util.find_spec("googleapiclient")
        assert google_lib is not None

    def test_credentials_creation_attempt(self):
        """Check that attempt is made to create credentials on Importer initialisation"""
        discovery.build = MagicMock()
        Credentials.from_service_account_file = MagicMock()

        new_importer = SheetsImporter('test_file')

        Credentials.from_service_account_file.assert_called_once()
        self.assertIn('test_file',Credentials.from_service_account_file.call_args[0][0])

    def test_credentials_file_passed_in(self):
        """Check that the file path passed in is used in credential creation"""
        discovery.build = MagicMock()
        Credentials.from_service_account_file = MagicMock()

        new_importer = SheetsImporter('test_file')

        self.assertIn('test_file', Credentials.from_service_account_file.call_args[0][0])

    def test_get_google_services_creation_attempt(self):
        """Check that attempts are made to create the Google Drive and SHEETS services """
        discovery.build = MagicMock()
        Credentials.from_service_account_file = MagicMock()

        new_importer = SheetsImporter('test_file')

        self.assertEquals(discovery.build.call_count, 2)
        self.assertIn('sheets', discovery.build.call_args[0][0])


