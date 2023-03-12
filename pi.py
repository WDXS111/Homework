
num = 1
sign = 1
pi = num
n = int(input('请输入需要精确的位数'))
while  True:
    num += 2
    sign = -sign
    pi += 1/num * sign
    if 1/num < pow(10,-n):
        break
pi = 4 * pi
with open('E:\\杂\\随便写写\\text1.txt','w',encoding='utf-8')as f:
    f.write(str(pi))
    f.close()