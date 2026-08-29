import openpyxl

def data_load(filename,sheet_name):
    #打开excel文件
    work_excel = openpyxl.load_workbook(filename)
    #选择表
    worksheet = work_excel[sheet_name]
    #读取表
    key = []
    datas = []
    for data in worksheet[2]:
        key.append(data.value)
    for row in worksheet.iter_rows(min_row=3,values_only=True):
        if row[17]:
            datas.append(dict(zip(key,row)))
    #关闭
    work_excel.close()
    return datas