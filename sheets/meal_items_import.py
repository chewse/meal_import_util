"""
Meal item import related classes & functions
"""
from sheets.sheets_import import SheetsImporter

class MealItemExporter(SheetsImporter):
    """Class for acccesing meal item export functionality"""

    def __init__(self, cred_file):
        super(MealItemExporter, self).__init__(cred_file)

    def get_meal_items_from_file(self, file_url):
        """
        Provided with a Google sheet file, get and return a list of meal items
        :param file_url:
        :return:
        """