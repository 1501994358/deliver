
#!/usr/bin/python
# -*- coding: utf-8 -*-

from hashlib import md5, shake_256
from hashlib import sha256
import csv

def md5_str(_str):
    m = md5()
    m.update(str(_str).encode(encoding='utf-8'))
    return m.hexdigest()

def sha_256_str(_str):
    m = sha256()
    m.update(str(_str).encode(encoding='utf-8'))
    return m.hexdigest()
#
if __name__ == '__main__':
    print (md5_str('李阳'))
    print(sha_256_str("李阳"))


from hashlib import md5
# 待加密信息
# str = '李四'
# hl = md5()
# hl.update(str.encode(encoding='utf-8'))
# print('MD5加密前为 ：' + str)
# print('MD5加密后为 ：' + hl.hexdigest())


# import os, io
#
# f = open(r'C:\Users\Administrator\Desktop\f.xlsx', 'r+')
# for line in f.readlines():
#     print(line)
# print(f.read())
# f.close()

import xlrd,xlwt
from datetime import date,datetime


def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\f.xlsx')
    # 获取所有的sheet
    print (workbook.sheet_names())
    # sheet_name1 = workbook.sheet_names()[0]

    # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_index(0)
    # print(sheet1)
    sheet1 = workbook.sheet_by_name("Sheet1")
    # sheet的名称，行数，列数
    # print(sheet1.name, sheet1.nrows, sheet1.ncols)
    nrows = sheet1.nrows  # 获取表的行数
    # 读取表信息
    # l = list()
    for i in range(1,nrows):
        #sheet1.ncols.type
        data = sheet1.row_values(i)
        id_, cell, name = data[0], int(data[1]), data[2]
        print(id_, cell, name)
        print(md5_str(name))
        # l.append([id_, cell, name])
        # for lvalue in l:
        #     print(lvalue)
            # print(md5_str(lvalue))
        print(md5_str(id_).encode('utf-8'), md5_str(cell).encode('utf-8'), md5_str(name).encode('utf-8'))
    # 获取整行和整列的值（数组）
    # rows = sheet1.row_values(2)
    # cols = sheet1.row_values(1)
    # # if(sheet1.cell(1,1).ctype == 2):
    # #     date_value = xlrd.xldate_as_tuple(sheet1.cell_value(rows, 1), book.datemode)
    # #     date_tmp = string(date_value[:3])
    # print(rows)
    # print(cols)
    #
    # # 获取单元格内容
    # print(sheet1.cell(1,0).value.encode('utf-8'))
    # print(sheet1.cell_value(1,0).encode('utf-8'))
    # print(sheet1.row(1)[0].value.encode('utf-8'))
    #
    # # 获取单元格内容的数据类型
    # print(sheet1.cell(1,1).ctype)
def write_excle():
    # 创建工作簿
    f = xlwt.Workbook()
    sheet4 = f.add_sheet(u'Sheet5', cell_overwrite_ok=True)
    row0 = [u'md5_id', u'md5_cell', u'md5_name']
    # 生成第一行
    for i in range(0, len(row0)):
        sheet4.write(0, i ,row0[i])
    workbook = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\f.xlsx')
    # print(sheet1)
    sheet1 = workbook.sheet_by_name("Sheet1")
    nrows = sheet1.nrows  # 获取表的行数
    # 读取表信息
    l = list()
    for i in range(1, nrows):
        data = sheet1.row_values(i)
        id_, cell, name = data[0], int(data[1]), data[2]
        l.append([md5_str(id_), md5_str(cell), md5_str(name)])
        # print(md5_str(id_), md5_str(cell), md5_str(name))
    print(l)
    # for j in range(1, len(l)):
    #     sheet4.write(j ,l[j])
    # f.save('C:\\Users\\Administrator\\Desktop\\2.xlsx')

    with open('C:\\Users\\Administrator\\Desktop\\example.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in l:
            writer.writerow(row)

        # 还可以写入多行
        # writer.writerows(datas)


if __name__ == '__main__' :
    read_excel()
    write_excle()


