from unittest import TestCase
from sheets import utils

class UtilsTest(TestCase):
    def test_get_sheet_id_from_url(self):
        """
        Check that the utils function returns IDs accurately from the supplied Google sheets API
        :return:
        """
        url_1 = "https://docs.google.com/spreadsheets/d/1D_nOVbrqWEurZs3AMWYHOgMhQMgH4LpSDWjqgUV9YbY/edit#gid=0"
        sheet_id = utils.get_sheet_id_from_url(url_1)
        self.assertEquals(sheet_id, "1D_nOVbrqWEurZs3AMWYHOgMhQMgH4LpSDWjqgUV9YbY")