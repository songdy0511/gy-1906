# 字典的特性
# 1. 字典中的key可是唯一的
# 2. key 不可改变 数字，字符串，元组
#    元组(1,2,3,4)可作为key，（1，【3】）不可
# 3. 字典只能通过key访问value，不能直接访问value
# 4. 字典中数据是无序的
# 创建
a = {}
# 在字典中新增一对数据
a["姓名"] = '宋丹阳'
print(a)
# 改
a["姓名"] = "晓虹"
print(a)
a[1] = 333
print(a)
a[(1,2)] = 333
print(a)
# 删 pop参数只能为key
# a.pop((1,2))
# print(a)
# # 清空字典
# # a.clear()
# # print(a)
# # 查
# # 根据key查看value
# print(a['姓名'])
# # 遍历查询
# for key in a:
#     print(a[key])
# # 字典合并
# #  把一个字典合并到另一个字典中
# c = {'性别':'女'}
# d = {'姓名':'黄晓明'}
# # c.update(d)
# # print(c)
# # 两个字典合并，生成一个新字典
# print(dict(c,**d))
# print(c)
# print(d)
# # 成员判断（key）
# if ("姓名" in c):
#     print("存在列表中")
# else:
#     print("不存在列表中")
#
#
# # 获取字典长度
# print(len(c))
#
#





