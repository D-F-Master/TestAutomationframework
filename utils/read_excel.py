import openpyxl

def read_excel():
    workbook = openpyxl.load_workbook('../data/test_data.xlsx')
    print(workbook['Sheet1'])

if __name__ == '__main__':
    read_excel()