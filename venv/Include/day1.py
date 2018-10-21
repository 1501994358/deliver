
'''
i = input('请输入您的年龄:')
i = int(i)
if 5<i<10:
    print('小孩子')
elif(10<i<18):
    print("年轻人")
else :
    print("成年人")
'''
'''
a, b, c = 1, 2 ,4
print(a,b,c)
del a, b
print(c)
'''
'''
s = "456485554"
print(s[2:])
print(s * 2)
for i in s:
    print(i)
'''
'''
for s in range(0, 1000):
    print(s)
print(type(range(0, 1000)))
'''
#str(字符串)      支持切片，截取等操作
D = '123456789'
#List（集合）     列表用 [ ] 标识，是 python 最通用的复合数据类型
A = ["liyang","nengwu","jianxin","guoyu","wangqiang"]
#tuple（元组）    元组用"()"标识,内部元素用逗号隔开,元组不能二次赋值，相当于只读列表
B = ('liyang','nengwu','jianxin','guoyu','wangqiang')
#dictionary       字典用"{ }"标识。字典由索引(key)和它对应的值value组成
C = {'name':'liyang','sex':'男','age':'23','addr':'陕西','hight':'174'}

a = 10; b = 20
print(a+b,a-b,a*b,a/b,a%b,a**b,a//b)
print(a==b,a!=b,a>b,a<b,a>=b,a<=b)
c = 10
# c+=a  20  c=c+a   家数
# c-=a  0   c=c-a   减数
# c*=a  100 c=c*a   乘数
# c/=a  1   c=c/a   除数
# c%=a  0   c=c%a   余数
# c**=a 100 c=c**a  幂次方
# c//=a 1   c=c//a  取整数
c**=a
print(c)

# print(A.append("guanjun"))
# print(A)
# for C1 in C:
#     for A1 in A:
#         print(A1)
#     print(C1)

