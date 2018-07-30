import re

def get_sheet_id_from_url(sheet_url):
    """
    Given the URL of a Google sheet file, return the ID
    :param url: the google sheet's URL
    :return: the ID of the sheet's URL
    """
    try:
        pattern_to_match = '/spreadsheets/d/([a-zA-Z0-9-_]+)'
        sheet_id_match = re.search(pattern_to_match, sheet_url).group(0)
        sheet_id = sheet_id_match.replace('/spreadsheets/d/', '')
        return sheet_id
    except AttributeError:
        raise ValueError('Input value does not contain a valid Google Sheet ID')



