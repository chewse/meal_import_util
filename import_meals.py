from sheets.meal_items_import import MealItemImporter
import sys
import pprint

def print_meal_item_info(meal_item):
    print("")

if __name__ == '__main__':
    if not len(sys.argv) >= 4:
        print("Missing Parameter. Call this script with following parameters")
        print("1. path to credentials file")
        print("2. URL to Google Sheet file")
        print("3. ID of the sheet which contains data to import")
        exit(1)

    cred_file = sys.argv[1]
    sheet_url = sys.argv[2]
    sheet_id = sys.argv[3]

    meals_importer = MealItemImporter(cred_file)
    meal_items = meals_importer.get_meal_items_from_file(sheet_url, sheet_id)

    print("Data Imported Successfully : ")
    print("********************************************************")
    print("Number of Meal Items imported - " + str(len(meal_items)))
    print("Meal Item Values : ")

    for item in meal_items:
        print(item.raw_data)
    print("********************************************************")





