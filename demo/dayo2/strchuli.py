# a = "qwertyuiopasdfghjkl"
# print(a[1:5])
# print(a[0:5])
# print(a[5:10])
# print(a[-5:])
# print(a[-5:-1])
# print(a[-7:-2])
# print(a[2:8:2])
# print(a[::-1])
# print(len(a))
# print(a.replace('er','34'))
# print(a[1:])
# 按照扑克牌的规则，现在有6张牌，只要5张
# 黑桃（S）红桃（H）方块（D）梅花（C）
# 牌：2.3.4.5.6.7.8.9.10.J.Q.K.A
# 数据库存的是下面格式的数据，写脚本验证满足3带2的牌型
# [''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
# ["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
# ["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]


# 第一步：统一符号  对字符串的处理，用replace（）
# 第二步：去掉中括号 字符串截取  [::]
# 第三步：变成list  字符串切片  .split（） 新建一个list变量
# 第四步：取出后面的数字  循环遍历取出list里面的每个值，对这个值进行截取
# 第五步：统计相同的数字个数  用字典去统计
# 第六步：判断数据中有没有同时存在三个相同数字和两个相同数字  if判断
# 如果key对应的数值有3的 v1 = 1，如果没有则为0
# 如果key对应的数值有2的 v2 = 1，如果没有则为0


# b = '''["D1" , "H1" , "H10" , "H7" , "S1" , "S7"]'''
# b = b[2:-2]
# print(b)
# b_li = b.split('" , "')
# print(b_li)
# c = '''["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]'''
# c = c[2:-2]
# print(c)
# [''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']


# def是方法定义的关键字，juge_3_2方法名，可以自定义不能以数字开头， ()参数列表
def juge_3_2(d):
    #d = input("请输入牌型：")
    d = d.replace("''",'"')
    d = d[2:-2]
    d = d.split('" , "')
    #print(d)
    e = {}
    for f in d:
        #print(f)
        g = f[1:]
        if(g in e):
            e[g] += 1
        else:
            e[g] = 1
    #print(e)
    v1 = 1 # 如果v1等于0 ，表示key对应的值有等于3的，如果v1 = 1，则表示没有
    v2 = 1 # 如果v1等于0 ，表示key对应的值有等于2的，如果v1 = 1，则表示没有
    for key in e:
        if(e[key] == 3 ):
            v1 = 0
        if(e[key] == 2):
            v2 = 0
    if(v1 == 0 and v2 == 0):
        print('可以三带二')
    else:
        print('不可以三带二')
# for k in range(3):
#     juge_3_2()
# open python提供的一個内置函數：作用就是打開一個文件，参数一：文件路径，参数二：文件的打开模式 r只读，w可写入（清空后写入），a可读可写入
# with open（）as f 类似于 f = open（），可以在with的代码执行出问题的时候，做一些资源释放的工作
with open("E:\\sofewaredate\\python\\gy-1906\\demo\\day04\\cards.txt",'r') as f:
    # 读文件，readlines()作用就是把文件中所有的内容按行读取出来,存到一个list中;read()把整个文件的内容读取出来,存到一个字符串中
    lines = f.readlines()
    #print(lines)
    # for循环遍历这个列表
    for line in lines:
        # 去掉每一行末尾的换行符
        line = line.replace("\n",'')
        print(line)
        # 调用一个方法，判断牌型是否3带2
        juge_3_2(line)

# print(len(d))
# c = "http://qa.yansl.com/swagger-ui.html"
# xieyi = c.split('://')[0]
# print(xieyi)
# d = c.split('://')[1]
# yuming = d[:d.find("/")]
# print(yuming)
# uri = d[d.find("/"):]      # uri = d[d.find("/")+1:]
# print(uri)





