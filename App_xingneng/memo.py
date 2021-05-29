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
# ����д�뵽txt�ļ��Ĺ���
def write_txt(x, y,z):
    print("���д���ļ�")
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
    print("��ȡcpuռ��")
    command = 'adb shell top -n 1 | grep com.haier.uhome'
    file_out = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    lines = file_out.stdout.readlines()
    print(lines)
    line = lines[0]
    print(line)
    line = str(line)
    try:
        # ��ȡcpu
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
        print("�������쳣")
        print("ɶ������,����")


def get_memo():
    print("��ȡ�ڴ�")
    command='adb shell top -n 1 | grep com.haier.uhome'
    file_out=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    lines=file_out.stdout.readlines()
    print(lines)
    line=lines[0]
    print(line)
    line=str(line)
    try:
        #��ȡ�ڴ�
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
        print("�������쳣,ɶ������,����")


def my_plot_memo(fig):
    print("��ʼ��ͼ")
    ax=fig.add_subplot(111)
    ax.plot(memobuf,'b-')
    ax.set_title("Memo-info")
    ax.grid()
    plt.pause(5)
    plt.clf()
    print("��ͼ����")

def my_plot_cpu(fig):
    print("��ʼ��ͼ")
    ax=fig.add_subplot(111)
    ax.plot(cpubuf,'b-')
    ax.set_title("CPU-info")
    ax.grid()
    plt.pause(5)
    plt.clf()
    print("��ͼ����")

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
