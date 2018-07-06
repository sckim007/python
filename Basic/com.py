class CpStockCode:
    def __init__(self):
        self.stocks = {'유한양행':'A000100'}

    def GetCount(self):
        return len(self.stocks)

    def NameToCode(self, name):
        return self.stocks[name]

instCpStockCode = CpStockCode()
print(instCpStockCode.GetCount())
print(instCpStockCode.NameToCode('유한양행'))

# this is a part of pywin32
import win32com.client

'''
Call InternetExplore Application

###############################################################################
explore = win32com.client.Dispatch("InternetExplorer.Application")
explore.Visible = True
###############################################################################
'''

'''
Call Word Application
###############################################################################
word = win32com.client.Dispatch("Word.Application")
word.Visible = True
###############################################################################
'''

'''
Call Excel Application
###############################################################################
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True

wb = excel.Workbooks.Add()
ws = excel.Worksheets("Sheet1")
ws.Cells(1,1).Value = "hello world"
wb.SaveAs('c:\\Users\\sckim007\\Desktop\\test.xlsx')
excel.Quit()
###############################################################################
'''

'''
Read data from Excel file

###############################################################################
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True

wb = excel.Workbooks.Open('c:\\Users\\sckim007\\Desktop\\test.xlsx')
ws = excel.ActiveSheet
print(ws.Cells(1, 1).Value)
excel.Quit()
###############################################################################
'''

'''
Set color to Cell
'''
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True

wb = excel.Workbooks.Open('c:\\Users\\sckim007\\Desktop\\test.xlsx')
ws = excel.ActiveSheet

ws.Cells(1, 2).Value = "is"
ws.Range("C1").Value = "good"
ws.Range("C1").Interior.ColorIndex = 10

excel.Quit()
