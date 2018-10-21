#!/usr/bin/python
# -*- coding: utf-8 -*-

import hashlib
def md5(str):
    m = hashlib.md5()
    m.update(str.encode(encoding = 'utf-8'))
    return m.hexdigest()

file = open(r'C:\Users\Administrator\Desktop\file.csv','r')
dmfile = open(r'C:\Users\Administrator\Desktop\file.csv',encoding='utf-8')
dm = dmfile.readlines()
md5file = open(r'C:\Users\Administrator\Desktop\md5file', 'a+')
print(dm)
for d in dm:
    print(md5(d))
    md5file.write(md5(d))
    md5file.write('\n')
file.close()
dmfile.close()
md5file.close()