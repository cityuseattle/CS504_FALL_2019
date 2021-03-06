import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'Cars'
sheet['A1'] = 'Models'
sheet['B1'] = 'Prices'

wb.save('car_data.xlsx')

cars = [('BMW', 40000), ('Audi', 500000), ('Ford', 25000), ('Mclaren', 100000), ('Toyota', 30000)]

for car in cars:
    sheet.append(car)

wb.save('car_data.xlsx')