# This is a sample Python script.
from operation.transpose import Excel
import sys


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def test_excel_transpose(file_name, source_sheet_name, destination_sheet_name):
    excel = Excel(file_name)
    excel.read(source_sheet_name)
    excel.write(destination_sheet_name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_name = sys.argv[1]
    source_sheet_name = sys.argv[2]
    destination_sheet_name = sys.argv[3]
    test_excel_transpose(file_name, source_sheet_name, destination_sheet_name)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
