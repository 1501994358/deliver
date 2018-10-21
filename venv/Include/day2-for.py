
# count = 9
# while count < 100:
#     count = count + 1
#     if count % 2 == 0:
#         continue
#     print(count)


# numbers = [1,5,89,12,45]
# even = []; odd = []
# while len(numbers) > 0:
#     number = numbers.pop()
#     if(number % 2 == 00):
#         even.append(number)
#         print("even:", even)
#     else:
#         odd.append(number)
#         print("odd:",odd)
# print(even, odd)
'''
i = 1
while i<10:
    i+=1
    if i%2==0:
        continue
    print(i)
while 1:
    print(i)
    i+=1
    if i>10:
        break
'''

'''
#100以内的素数
i = 0
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if not(i%j):break
        j = j+i
    if(j>i/j):print(i,"是素数")
    i=i+1
'''

'''
for i in "123456":
    if i == "5":
        pass
    print(hex(int(i)))

i = 48646255
print(hex(i), oct(i))
'''

'''
import math, random
print(abs(-8))  #绝对值
print(math.fabs(-8))  #绝对值的小数位
print(math.ceil(8.6)) #上入函数
print(math.floor(8.6)) #下舍函数
print(math.log(math.e)) #1.0 以10为基数的N次方
print(math.log10(1000)) #3.0
print(max([1,5,9]))   #返回序列的最大值
print(min([1,5,9]))   #返回序列的最小值
print(math.modf(1.9))  #返回整数和小数分开的两个值
print(math.pow(10,2))  #x**y的值
print(math.sqrt(100))  #x的平方根
print(round(2.36459,3)) #返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
print(random.choice("123456"))  #返回序列中的任意一个数
print(random.randrange(2,10,2))
'''

n = 100; sum = 0; i = 1
while i<=n:
    sum = sum + i
    i += 1
print(sum)