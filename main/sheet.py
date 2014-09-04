from google_spreadsheet.api import SpreadsheetAPI
from config import GOOGLE_SPREADSHEET


def list_sheets(key=False):
    """If no key passed, lists spreadsheet keys for the user defined in
    config file. If key passed as argument, lists ids of individual sheets"""

    api = SpreadsheetAPI(GOOGLE_SPREADSHEET['USER'],
        GOOGLE_SPREADSHEET['PASSWORD'],
        GOOGLE_SPREADSHEET['SOURCE'])
    spreadsheets = api.list_spreadsheets()
    if key:
        worksheets = api.list_worksheets(key)
        print worksheets
    else:
        for sheet in spreadsheets:
            print sheet


def get_google_sheet(sheet_key=False, sheet_id='od6'):
    """Uses python_google_spreadsheet API to interact with sheet
    https://github.com/yoavaviram/python-google-spreadsheet
    Returns a list of dicts with each row its own list with the first row key"""

    api = SpreadsheetAPI(GOOGLE_SPREADSHEET['USER'],
        GOOGLE_SPREADSHEET['PASSWORD'],
        GOOGLE_SPREADSHEET['SOURCE'])
    sheet = api.get_worksheet(sheet_key, sheet_id)
    sheet_object = sheet.get_rows()
    return sheet_object
