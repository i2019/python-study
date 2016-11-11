#encoding:utf-8

#list

#定义list并赋初值
ns=[1,2,3,4,5]



#访问list指定位置的元素
print ('ns[0]=',ns[0]);

#在末尾增加元素
ns.append(996)

#清空列表
ns.clear()

#在list指定位置插入不同数据类型的元素
ns.insert(9,1001);
ns.insert(0,'零')
ns.insert(-1,True)
ns.insert(-2,9.000)
#负数下标表示倒数第几个
print ('ns[-4]=',ns[-4]);

ns.count
#打印list
print (ns)
#打印list长度
print (len(ns))

