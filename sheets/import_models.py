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
        self.visible = values[0]
        self.meal_buckets = values[1]
        self.meal_components = values[2]
        self.vendor_facing_name = values[3]
        self.client_facing_name = values[4]
        self.parent_item = values[5]
        self.description = values[6]
        self.portion_quantity = values[7]
        self.portion_unit = values[8]
        self.unit_cost = values[9]
        self.msrp = values[10]
        self.food_label = values[11]
        self.ingredients = values[12]
        self.serving_utencil1 = values[13]
        self.serving_utencil2 = values[14]
        self.serving_utencil3 = values[15]

    def __str__(self):
        return self.vendor_facing_name

