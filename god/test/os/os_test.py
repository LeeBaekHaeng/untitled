# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 11:55:58 2017

@author: LeeBaekHaeng
"""

import os


# print 'os.name: ' + os.name
#
# print (os.getcwd())  # 현재 디렉토리의
# print (os.path.realpath(__file__))  # 파일
# print (os.path.dirname(os.path.realpath(__file__)))  # 파일이 위치한 디렉토리


def def1():
    print (os.getcwd())  # 현재 디렉토리의


def def2():
    return os.getcwd()


def def3():
    desktopPath = os.path.expanduser('~')
    print desktopPath


def main():
    def3()


if __name__ == "__main__":
    main()
