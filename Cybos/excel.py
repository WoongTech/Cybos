import openpyxl

# ---------------------------------------------------------
# EXCEL
# ---------------------------------------------------------

def makeExcel(excelName):
    wb = openpyxl.Workbook()
    wb.save(excelName)


def editExcel(wbName, data1, data2):
    wb = openpyxl.load_workbook(wbName)
    sheet = wb['Sheet']

    sheet.append([data1,data2])

    wb.save(wbName)


makeExcel("Hi.xlsx")
editExcel("Hi.xlsx",1,2)