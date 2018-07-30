"""
Meal item import related classes & functions
"""
from sheets.sheets_import import SheetsImporter
from sheets.import_models import MealItem
from sheets import utils

class MealItemImporter(SheetsImporter):
    """Class for acccesing meal item export functionality"""

    def __init__(self, cred_file):
        super(MealItemImporter, self).__init__(cred_file)

    def get_meal_items_from_file(self, file_url, sheet_id):
        """
        Provided with a Google sheet file, get and return a list of meal items
        :param file_url: The URL to the Google sheet file
        :param sheet_id: The ID of the sheet to import data from
        :return:
        """
        sheet = {}
        sheet['id'] = utils.get_sheet_id_from_url(file_url)
        values = self.get_sheet_range_output(sheet, sheet_id)
        meal_items = self.get_meal_items_from_values(values)
        return meal_items

    def get_meal_items_from_values(self, values):
        import_values = values[15:]
        meal_items = [MealItem(x) for x in import_values if len(x) >= 12]
        return meal_items


