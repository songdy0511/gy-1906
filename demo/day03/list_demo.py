# 创建
a = []
print(a)
# 列表最后新增单个值
a.append(8)
print(a)
a.append("sadkef")
print(a)
a.append("789")
print(a)
# 合并
b = [2,4,5,7,9,12]
print(a + b)
print(a)
# 使用extend 合并
a.extend(b)
print(a)
# 删
# 根据下标删除某个元素
a.pop(0)
print(a)
# 默认删除列表中最后一个元素
a.pop()
print(a)
# 清空一个列表
# a = []
# print(a)
# a.clear()
# print(a)
# 改
# 根据下标修改某个元素的值
a[0]=3
a[1]=9
# 等价
a[0],a[1]=3,9
print(a)
# 查
# 根据下标查询某个元素
print(a[0])
print(a[2])
# 遍历（借助循环）
for i in a:
    print(i)
# 截取
# 截取部分数据
print(a[1:3])
# 倒叙
print(a[::-1])
# 隔一个取一个
print(a[::2])
# 长度
print(len(a))
# 成员判断
if (10 in a):
    print("存在列表中")
else:
    print("不存在列表中")