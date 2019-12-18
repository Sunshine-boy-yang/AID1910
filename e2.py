"""
模拟生产,入库,销售场景
假定企业自产,自存,自销.将工厂生产的产品不定时的运到仓库
同时,仓库货物需要运到商场销售
编写程序模拟过程(主要对仓库的存取)
*仓库的最大存量可以设置为一个常量(max=10)
*仓库满了不能存储货物
*仓库空了不能提供货物
*写多线程分别表达货物的存储提取(同时进行)
*不能出现先存满再取完或者先取完再存满
"""
import random
import time
from threading import Thread

max=50
a=number01 = random.randint(0,50)
print("仓库存货为%d"%a)
def get():
    while True:
        number_time = random.randint(0,8)
        time.sleep(number_time)
        global a
        number = random.randint(0, 15)
        if a >= number:
            a -= number
            print("取走货物%d,仓库存货为%d"%(number,a))
        else:
            a=0
            print("货物不够,以清仓")
def give():
    while True:
        number_time = random.randint(0,8)
        time.sleep(number_time)
        global a
        number = random.randint(0, 15)
        if a <= 50 - number:
            a += number
            print("存了放货物%s,仓库存货为%d"%(number,a))
        else:
            a=50
            print("仓库位置不够已存满")
lisfun=[get,give]
jobs=[]
for i in lisfun:
    t=Thread(target=i)
    t.start()
    jobs.append(t)
[i.join() for i in jobs]



