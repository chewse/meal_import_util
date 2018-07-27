from google.oauth2 import service_account
from googleapiclient import discovery
import sys


class SheetsImporter:

    def __init__(self, cred_file):
        """
        Initialise class with a path to credential file to set up
        Google DRIVE and SHEETS API services
        """

        scopes = [
            'https://www.googleapis.com/auth/drive.readonly.metadata',
            'https://www.googleapis.com/auth/spreadsheets'
        ]
        service_account_key_file = cred_file

        credentials = service_account.Credentials.from_service_account_file(
            service_account_key_file, scopes=scopes)

        drive_service = discovery.build('drive', 'v3', credentials=credentials)
        sheets_service = discovery.build('sheets', 'v4', credentials=credentials)

        self.services = {
            'sheets_service': sheets_service,
            'drive_service': drive_service
        }

    def get_google_sheet_files(self, drive_file = None):
        """
        List all files in DRIVE belonging to the service account which are
        Google Sheet files
        :param drive_file the DRIVE folder to check for google sheets files
        TODO : implement checking in the provided google drive folder for sheets files
        """
        drive_service = self.services['drive_service']
        files = drive_service.files().list().execute().get('files', [])
        sheet_files = []
        for f in files:
            # pick sheet files by checking mime types
            if f['mimeType'] == 'application/vnd.google-apps.spreadsheet':
                sheet_files.append(f)
        return sheet_files

    def get_google_all_sheets_and_contents(self, sheet_file):
        """
        Get all sheets in this file and print out their values
        :param sheet_file: the file whose content is to be picked
        """
        sheets_service = self.services['sheets_service']
        workbook = sheets_service.spreadsheets().get(spreadsheetId=sheet_file['id']).execute()
        all_sheets = workbook.get('sheets', '')
        print("\nFile : " + sheet_file['name'])
        for sheet in all_sheets:
            title = sheet.get("properties", {}).get("title", "Sheet1")
            values = self.get_sheet_range_output(sheet_file, title)
            print("\n\tSheet : " + title)
            for row in values:
                print(row)
            print("\n")


    def get_sheet_range_output(self, sheet_file, range):
        """
        Get the values in the range of the provided sheets file
        :param sheet_file: the file whose content is to be picked
        :param range: the range of columns and rows whose values are to be returned
        :return: a list of list of values in the range specified
        """
        sheets_service = self.services['sheets_service']
        result = sheets_service.spreadsheets().values().get(spreadsheetId=sheet_file['id'], range=range).execute()
        values = result.get('values', [])
        return values

    def list_sheet_contents(self, sheet_files):
        """
        List contents of files with the range provided
        :param sheet_files: list of google sheets files
        :return:
        """
        for file in sheet_files:
            self.get_google_all_sheets_and_contents(file)


if __name__ == '__main__':
    if sys.argv[1]:
        g_cred_file = sys.argv[1]
        # '/Users/solomon/CHEWSE/sheets_import/credential_key.json'

        sheets_importer = SheetsImporter(g_cred_file)
        g_sheet_files = sheets_importer.get_google_sheet_files()
        sheets_importer.list_sheet_contents(g_sheet_files)

    else:
        print("Provide a credentials file ")







