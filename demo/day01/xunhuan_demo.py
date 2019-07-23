for i in range(5):
    print("重要的事情说第",i+1,"遍")
for a in range(100):
    if (a % 2 == 1):
        print(a)
print(10,'\t',end='')
print(10,'\t')
# 九九乘法表
# '\t' 代表空格 相当于Tab
# print() 代表换行
# end = ‘’代表 放到同一行
for a in range(1,10):
    for b in range(1,(a+1)):
        print(a,"X",b,"=", a*b,'\t',end = '')
    print()
for h in range(1,10):
    for j in range(1,(h+1)):
        print(j,"X",h,"=", h*j,'\t',end = '')
    print()
# 100以内的质数
for d in range(2,101):
    n = 2
    for m in range(2,d):
        if(d%n == 0):
            break
        n = n+1
    if(n==d ):
        print(d)
# 成绩0-59不及格，60-70及格 70-80 良好 80以上是优秀    [90,100,81,84]判断下改组成绩是否全部都是优秀
# z = 0 # 0代表全部优秀 1 代表不是全部优秀
# for g in [90,100,81,84]:
#     o =  80
#     if(g-o<0):
#       z = 1
#       break
# if(z==0):
#     print("全部优秀")
# else:
#     print("不是全部优秀")
# "01010010001110001001001010101010010101" 计算下几个0 几个1
# s = "01010010001110001001001010101010010101"
# x = 0 # x表示0
# q = 0 # q表示1
# for e in s:
#     if(e=="0"):
#         x = x+1
#     else:
#         q = q+1
# print("有",x,"个0，",q,"个1")
# 求1+2+3+4+...+100
# y = 0
# for x in range(1,101):
#     y = y + x
# print(y)

s = 0
t = 1
while(t<=100):
    s = s + t
    t = t + 1
print(s)
# 求出10的阶乘  1*2*3*...*10
# s = 1
# t = 1
# while(t<=10):
#     s = s * t
#     t = t + 1
# print(s)





# 输入一个年份，判断其是否为闰年 能被4整除而不能被100整除 能被400整除。
# for h in range(1,h):
