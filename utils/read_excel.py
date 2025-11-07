import openpyxl

def read_excel():
    # 加载Excel工作簿
    workbook = openpyxl.load_workbook('../data/test_data.xlsx')
    # 选择第一个工作表Sheet1
    worksheet = workbook['Sheet1']

    # 创建空列表用于存储数据
    data = []
    # 获取第一行作为键名列表
    keys = [cell.value for cell in worksheet[2]]

    # 从第3行开始遍历每一行数据
    for row in worksheet.iter_rows(min_row=3, values_only=True):
        # 将键名和行数据打包(zip)组合成字典
        dict_data = dict(zip(keys, row))
        # 判断is_true列是否为真，如果是则添加到数据列表中
        if dict_data['is_true']:
            data.append(dict_data)

    # 关闭工作簿
    workbook.close()
    # 返回筛选后的数据列表
    return data

