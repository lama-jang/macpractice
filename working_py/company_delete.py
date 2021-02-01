from openpyxl import load_workbook
import time

start = time.time()

wb = load_workbook("company_delete_raw.xlsx")
ws = wb.active

col_1 = ws['I']
companys = []
for i in range(0, 2656):
    companys.append(col_1[i].value)

# for cell in col_1:
    # i = 2
    # while i <= 2656:
        # if str(cell.value) == ws.cell(row=i, column=9).value:
            # target_counts += 1
            # ws.delete_rows(i)
        # else:
            # i += 1

target_counts = 0

i = 2
while i <= 8412:
    if ws.cell(row=i, column=8).value in companys:
        target_counts += 1
        ws.delete_rows(i)
    else:
        i += 1

print(target_counts)
wb.save("delete_file.xlsx")

print(time.time()-start)