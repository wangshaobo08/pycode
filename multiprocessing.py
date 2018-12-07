#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author: sober
# time: 2018/11/29
# soberwone@gmail.com

import threading
from time import sleep, ctime


def music(song):
    for i in range(4):
        print("listening music-%s:%s" % (song, ctime()))
        sleep(1)


def movie(mv):
    for i in range(2):
        print("watching movie-%s! %s" % (mv, ctime()))
        sleep(3)

songs = ['s1', 's2', 's3']
mvs = ['m1', 'm2', 'm3']
threads = []
songs_len = range(len(songs))
mvs_len = len(mvs)

for i in songs_len:
    t = threading.Thread(target=music, args=(songs[i],))
    threads.append(t)


if __name__ == "__main__":
    for i in songs_len:
        threads[i].start()
    for i in songs_len:
        threads[i].join()
    # 阻塞子线程的父线程，直到for循环中的子线程全部完成
    # join()方法位于for循环外，等到for 循环中的进程全部运行结束，才继续执行主线程
    print("all is done! %s" % ctime())
