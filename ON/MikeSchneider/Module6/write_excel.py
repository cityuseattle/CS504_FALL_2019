import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'Cars'
sheet['A1'] = 'Models'
sheet['B1'] = 'Price'

wb.save('car_data.xlsx')
