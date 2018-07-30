"""
This module will contain models that will serve as the output items of an import run on the Google sheets
"""


class MealItem:
    """Data model for a meal item record"""

    def __init__(self, values):
        """
        Pass in a list of values that this instance of MealItem will be built from
        :param values:
        """
        self.raw_data = values
        self.visible = values[0].strip()
        self.meal_buckets = values[1].strip()
        self.meal_components = values[2].strip()
        self.vendor_facing_name = values[3].strip()
        self.client_facing_name = values[4].strip()
        self.parent_item = values[5].strip()
        self.description = values[6].strip()
        self.portion_quantity = values[7].strip()
        self.portion_unit = values[8].strip()
        self.unit_cost = values[9].strip()
        self.msrp = values[10].strip()
        self.food_label = values[11].strip()
        #self.ingredients = values[12].strip()
        #self.serving_utencil1 = values[13].strip()
        #self.serving_utencil2 = values[14].strip()
        #self.serving_utencil3 = values[15].strip()
        #TODO : Discuss the padding of empty cells with empty strings to prevent index issues with import

    def __str__(self):
        return self.vendor_facing_name


