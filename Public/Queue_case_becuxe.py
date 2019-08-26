#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Time    : 2019/8/8 10:28
@Author  : Careslten
@Site    : 
@File    : Queue_case_becuxe.py
@Software: PyCharm
'''


import multiprocessing,time

def write_queue(queue):
    for i in range(10):
        if queue.full():
            print('队列已满')
            break
        queue.put(i)
        print(i)
        time.sleep(0.5)

def read_queue(queue):
    # 循环读取队列消息
    while True:
        # 队列为空，停止读取
        if queue.empty():
            print("---队列已空---")
            break

        # 读取消息并输出
        result = queue.get()
        print(result)

if __name__ == '__main__':

    # 创建消息队列
    queue = multiprocessing.Queue(5)
    # 创建子进程
    p1 = multiprocessing.Process(target=write_queue, args=(queue,))
    p1.start()
    # 等待p1写数据进程执行结束后，再往下执行
    p1.join()
    p1 = multiprocessing.Process(target=read_queue, args=(queue,))
    p1.start()

