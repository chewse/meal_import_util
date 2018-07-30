from unittest import TestCase
from sheets.meal_items_import import MealItemImporter
from google.oauth2.service_account import Credentials
from googleapiclient import discovery
from unittest.mock import MagicMock

class MealItemImportTest(TestCase):
    def setUp(self):

        """
        Setup for the meal items import functionality
        :return:
        """
        discovery.build = MagicMock()
        Credentials.from_service_account_file = MagicMock()

        self.values = []
        self.values.append(['Vendor Info'])
        self.values.append(['Vendor ID', '448'])
        self.values.append(['Vendor Name', 'Mission Picnic'])
        self.values.append([])
        self.values.append(['Guidelines'])
        self.values.append(['Meal Componet Key:', 'Meal Bucket Key:', 'Food Label Key', '', 'Protein Definitions', '', '',
                        '*Put toppings and sauces first so included items are added first, then below add Mains' +
                        ' and Sides, when an included item  '])
        self.values.append(['Main', 'Breakfast =B', '1= Vegetarian', '5= Contains Dairy ', 'S= Simple'])
        self.values.append(['Side', 'Lunch =L', '2= Vegan', '6= Contains Soy ', 'V= Variety'])
        self.values.append(['Base', 'Dinner =D', '3= Contains Gluten', '7= Contains Egg ', 'P= Premium'])
        self.values.append(['Topping', 'Happy Hour =H', '4= Contains Nuts', '8= Contains Shellfish'])
        self.values.append(['Sauce', 'Treat =T'])
        self.values.append(['A La Carte'])
        self.values.append([])
        self.values.append(['Item Details'])
        self.values.append(['Visible', 'Meal Bucket', 'Meal Component', 'Vendor Facing Item Name', 'Client Facing Item Name',
                        'Parent Item', 'Description', 'Portion Quantity', 'Portion Unit ', 'Unit Cost', 'MSRP',
                        'Food Label', 'Ingredients', 'Serving Utensil #1', 'Serving Utensil #2', 'Serving Utensil #3'])
        self.values.append(['yes', 'L,D', 'Base', 'Side Salad Mixed Greens', ' Mixed Greens', '', '', '0.75', 'oz. (weight)',
                        '1', '', '1,2'])
        self.values.append(['yes', 'L,D', 'Base', 'Side Salad Arugula', ' Arugula', '', '', '0.75', 'oz. (weight)', '1', '',
                        '1,2'])
        self.values.append(['no', 'L,D', 'Base', 'Side Salad Spinach', ' Spinach', '', '', '0.75', 'oz. (weight)', '1', '',
                        '1,2'])
        self.values.append(['yes', 'L,D', 'Base', 'Full Salad  Mixed Greens', ' Mixed Greens', '', '', '0.25', 'oz. (weight)',
                      '0.33', '', '1,2'])
        self.values.append(['yes', 'L,D', 'Base', 'Full Salad Arugula', ' Arugula', '', '', '0.25', 'oz. (weight)', '0.33',
                        '', '1,2'])
        self.values.append(['bad', 'data', '1'])
        self.values.append([])

        self.import_result = MealItemImporter('test_file').get_meal_items_from_values(self.values)

    def test_first_16_rows_ignored(self):
        """
        Test that the first 16 rows in the input values are ignored
        """
        first_meal_item = self.import_result[0]
        self.assertEquals(first_meal_item.vendor_facing_name, 'Side Salad Mixed Greens')
        self.assertEquals(first_meal_item.client_facing_name, 'Mixed Greens' )

    def test_correct_number_of_meals_imported(self):
        """
        Test that the right number of records were imported from the input values
        """
        self.assertEquals(len(self.import_result), 5)

    def test_empty_rows_and_inadequate_data_ignored(self):
        """
        Test that empty rows and rows with data less than 12 items are ignored
        """
        last_meal_item = self.import_result[4]
        self.assertEquals(last_meal_item.vendor_facing_name, 'Full Salad Arugula')
        self.assertEquals(last_meal_item.client_facing_name, 'Arugula')




