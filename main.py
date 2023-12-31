# This is a sample Python script.
from operation.excel.transpose import Excel
import sys


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



def test_excel_transpose(file_name, source_sheet_name, destination_sheet_name):
    excel = Excel(file_name)
    excel.read_and_assemble_data(source_sheet_name)
    excel.write_to_destination_sheet(destination_sheet_name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_name = sys.argv[1]
    source_sheet_name = sys.argv[2]
    destination_sheet_name = sys.argv[3]
    test_excel_transpose(file_name, source_sheet_name, destination_sheet_name)

