# 任意两个数的加减乘除
def yuns (a,b):
    print("和",a + b,"减",a - b,"成绩",a * b,"商",a / b)
with open("E:\\sofewaredate\\python\\gy-1906\\demo\\day04\\lianxishuzi.txt") as c:
    lines = c.readlines()
    for line in lines:
        line = line.replace("\n","")
        line_li = line.split(",")
        yuns (int(line_li[0]),int(line_li[1]))

def jia (q,w):
    e = q + w
    print(q,"+",w,"=",e)
    return e

def jian (q,w):
    e = q - w
    print(q,"-",w,"=",e)
    return e

def cheng (q,w):
    e = q * w
    print(q,"x",w,"=",e)
    return e

def shang (q,w):
    if(w!=0):
        e = q / w
        print(q, "/", w, "=", e)
        return e
    else:
        print("除数不能为0")
        return

jia(jia(3,8),10)
jian(jian(3,8),10)
cheng(cheng(3,8),10)
shang(shang(3,8),10)


def xx (t,y,u):
    return '{t1}欠{y1}{u1}元'.format(t1=t,y1=y,u1=u)
print(xx ("小田","小邵","一百万"))

def buy_coffees(cash=100,cups=1):
    #去咖啡店
    print("去咖啡店")
    #告诉服务员要几杯咖啡
    cup_num = cups
    print("告诉服务员要",cup_num,"杯咖啡")
    #服务员告诉你要多少钱
    print("服务员告诉你要",cup_num*30,"钱")
    #你给服务员多少钱
    money = cash
    print("你给服务员",money,"钱")
    #服务员找零，给你咖啡
    print("服务员找零",money-cup_num*30,"，给你",cup_num,"杯咖啡")
buy_coffees()
buy_coffees(300,7)









