import pytest
import openpyxl

book = openpyxl.load_workbook("C:/Users/nikos/OneDrive/Υπολογιστής/BootCamps/GitDemo/ProjectA/Sheets/UserSheet.xlsx")
sheet = book.active

def ListOfUsers():
    sheet_list = []
    for i in range(2, sheet.max_row + 1):
        user_list = []
        for j in range(2, sheet.max_column + 1):
            user_list.append(sheet.cell(row=i, column=j).value)
            if len(user_list) == sheet.max_column - 1:
                sheet_list.append(user_list)
    return sheet_list

@pytest.fixture(params=ListOfUsers())
def user(request):
    return request.param

@pytest.fixture(params=["a lot", "a little"])
def quantity(request):
    return request.param

