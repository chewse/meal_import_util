# meal_import_util
This enables the import of meal items from Google Sheet files according to the template below :
https://docs.google.com/spreadsheets/d/1D_nOVbrqWEurZs3AMWYHOgMhQMgH4LpSDWjqgUV9YbY/edit#gid=0
<br />


# Table of Contents
- [Technology Stack](#technology-stack)
- [Usage as library](#usage-as-library)
- [Usage from Command line](#usage-from-command-line)
- [Testing](#testing)



## Technology Stack
- Python
- Google Python Client API


## Usage as library
Import the meal importer class, initialise an instance with a google credential file, and run the import function with a URL and a Sheet ID


from sheets.meal_items_import import MealItemImporter

meals_importer = MealItemImporter(cred_file)<br />
meal_items = meals_importer.get_meal_items_from_file(sheet_url, sheet_id)

## Usage from command line
Change directory into project folder and run the command line utility

$ cd project_folder

$ python import_meals.py "path/to/credential/file" "url/of/google/sheet" "sheetID"

## Testing
Change into project folder and run "pytest"

