# coding=gbk
import os
import time
import subprocess
import numpy as np
import multiprocessing
from multiprocessing import Queue
import matplotlib.pyplot as plt
from datetime import datetime
from multiprocessing import Process
# import datetime
import sys
import re

# mytotal=Queue()
# mytime=Queue()
totalbuf = []
timebuf = []
cpubuf=[]
memobuf=[]
# 加入写入到txt文件的功能
def write_txt(x, y,z):
    print("结果写入文件")
    x = str(x)
    y = str(y)
    z=str(z)
    filename = 'memo_info.txt'
    with open(filename, 'a+') as f:
        f.write(x)
        f.write("   ")
        f.write(y)
        f.write("    ")
        f.write(z)
        f.write("\n")

def get_cpu():
    print("获取cpu占用")
    command = 'adb shell top -n 1 | grep com.haier.uhome'
    file_out = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    lines = file_out.stdout.readlines()
    print(lines)
    line = lines[0]
    print(line)
    line = str(line)
    try:
        # 提取cpu
        #out = re.split('S', line)
        #out1=line.split('S|R')
        out1=re.split('R|S', line)
        print(out1)
        out2=out1[1].split(' ')
        print(out2)
        print(out2[2])
        cpu_int=int(out2[2])
        cpubuf.append(cpu_int)

        # memo = out[1]
        # print(memo)
        # print(type(memo))
        # memo_int = int(memo)
        # print(memo_int)
        # print(type(memo_int))
        # memobuf.append(memo_int)

    except:
        print("出现了异常")
        print("啥都不做,继续")


def get_memo():
    print("获取内存")
    command='adb shell top -n 1 | grep com.haier.uhome'
    file_out=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    lines=file_out.stdout.readlines()
    print(lines)
    line=lines[0]
    print(line)
    line=str(line)
    try:
        #提取内存
        out=re.split('M',line)
        print(out)
        memo=out[1]
        print(memo)
        print(type(memo))
        memo_int=int(memo)
        print(memo_int)
        print(type(memo_int))
        memobuf.append(memo_int)

    except:
        print("出现了异常,啥都不做,继续")


def my_plot_memo(fig):
    print("开始画图")
    ax=fig.add_subplot(111)
    ax.plot(memobuf,'b-')
    ax.set_title("Memo-info")
    ax.grid()
    plt.pause(5)
    plt.clf()
    print("画图结束")

def my_plot_cpu(fig):
    print("开始画图")
    ax=fig.add_subplot(111)
    ax.plot(cpubuf,'b-')
    ax.set_title("CPU-info")
    ax.grid()
    plt.pause(5)
    plt.clf()
    print("画图结束")

def my_main():
    fig=plt.figure(figsize=(3,3))
    while True:
        nowtime=time.time()
        nowtime=int(nowtime)
        if nowtime %10==0:
            # get_memo()
            # my_plot_memo(fig)
            get_cpu()
            my_plot_cpu(fig)
        else:
            continue


if __name__=="__main__":
    #get_memo()
    my_main()
    #get_cpu()
