# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 11:55:58 2017

@author: LeeBaekHaeng
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import platform
import sys
import matplotlib
import matplotlib.font_manager as font_manager

import os

import god.duplicate_column_rename

import god.godlib as godlib

print '이백행 dlqorgod@naver.com'

# plt.rcParams["font.family"] = 'NanumGothic'

desktop = os.path.expanduser('~') + '/Desktop'
cwd = os.getcwd()


def pairplot():
    # plt.title('타이틀')

    # ax = plt.axes()

    # sns.plt.suptitle('title')

    # sns.pairplot(df, size=2)
    # sns.pairplot(df, size=2, ax=ax)
    # sns.pairplot(df_1, size=2)

    # ax.set_title('title')

    # sns.plt.suptitle('title')



    # fname = ('C:\Users\LeeBaekHaeng\Desktop/' + ('_').join(['user', 'pairplot']))
    fname = (desktop + '/' + ('_').join(['user', 'pairplot']))
    plt.savefig(fname, bbox_inches='tight')
    plt.show()
    plt.gcf().clear()


def pairplot2(df):
    sns.pairplot(df, size=2)
    # sns.pairplot(df_1, size=2)

    # fname = ('C:\Users\LeeBaekHaeng\Desktop/' + ('_').join(['user', 'pairplot']))
    fname = (desktop + '/' + ('_').join(['user', 'pairplot']))
    plt.savefig(fname, bbox_inches='tight')
    plt.show()
    plt.gcf().clear()


def def1():
    df_1 = pd.DataFrame([
        {'date': '2017-11-10', 'id': 4, 'value': 24},
        {'date': '2017-11-11', 'id': 4, 'value': 24},
        {'date': '2017-11-12', 'id': 6, 'value': 34}, ])

    df_2 = pd.DataFrame([
        {'date': '2017-11-10', 'id': 4, 'value': 24},
        {'date': '2017-11-11', 'id': 4, 'value': 24},
        {'date': '2017-11-12', 'id': 6, 'value': 14},
    ])

    df_3 = pd.DataFrame([
        {'date': '2017-11-10', 'id': 4, 'value': 24},
        {'date': '2017-11-11', 'id': 4, 'value': 24},
        {'date': '2017-11-12', 'id': 6, 'value': 14},
    ])

    # print df_1
    # print df_2

    # df = pd.concat([df_1, df_2])
    # df = pd.concat([df_1, df_2], axis=1)
    df = pd.concat([df_1, df_2, df_3], axis=1)
    # df.duplicated(list(df.columns));

    # cols = pd.Series(df.columns)
    # # for dup in df.columns.get_duplicates(): cols[df.columns.get_loc(dup)] = [
    # #     dup + '.' + str(d_idx) if d_idx != 0 else dup for d_idx in range(df.columns.get_loc(dup).sum())]
    # for dup in df.columns.get_duplicates():
    #     # print df.columns.get_loc(dup)
    #     # print df.columns.get_loc(dup).sum()
    #     # print sum(df.columns.get_loc(dup))
    #     print sum(list(df.columns.get_loc(dup)))
    df.columns = god.duplicate_column_rename.duplicate_column_rename(df.columns)

    print df


def def2():
    # filepath_or_buffer = 'C:/Users/LeeBaekHaeng/Documents/GitHub/untitled/test/pandas_df_test_a1.csv'
    filepath_or_buffer = cwd + '/pandas_df_test_a1.csv'
    # usecols = ['date', 'id', 'value']
    usecols = ['date', 'id']
    date_parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
    df = pd.read_csv(filepath_or_buffer,
                     parse_dates=['date'],
                     index_col=['date'],
                     # usecols=['date', 'id', 'value'],
                     usecols=usecols,
                     date_parser=date_parser,
                     low_memory=False)
    print df

    # filepath_or_buffer = 'C:/Users/LeeBaekHaeng/Documents/GitHub/untitled/test/pandas_df_test_a2.csv'
    filepath_or_buffer = cwd + '/pandas_df_test_a2.csv'
    # usecols = ['date', 'id', 'value']
    usecols = ['date', 'id']
    date_parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
    df2 = pd.read_csv(filepath_or_buffer,
                      parse_dates=['date'],
                      index_col=['date'],
                      # usecols=['date', 'id', 'value'],
                      usecols=usecols,
                      date_parser=date_parser,
                      low_memory=False)
    print df2

    # df = df['2017-11-11':'2017-11-12']
    # print df

    df_df2 = pd.concat([df, df2], axis=1)
    print df_df2

    # print df_df2.columns

    # df_df2.columns = ['아이디', '아이디2']
    # print df_df2

    # print df_df2.columns.is_unique
    #
    # print df_df2.columns
    #
    # for column in df_df2.columns:
    #     for column2 in df_df2.columns:
    #         print column + ' == ' + column

    print list(df_df2.columns)

    # df_df2.columns = god.duplicate_column_rename.duplicate_column_rename(df_df2.columns)
    df_df2.columns = godlib.duplicate_column_rename(df_df2.columns)

    print df_df2

    pairplot2(df_df2)


def def3():
    print platform.platform()

    print sys.version_info

    print ('버전: ', matplotlib.__version__)
    print ('설치위치: ', matplotlib.__file__)
    print ('설정: ', matplotlib.get_configdir())
    print ('캐시: ', matplotlib.get_cachedir())

    font_list = font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
    # 전체개수
    print(len(font_list))
    # 처음 10개만 출력
    print font_list[:10]

    font_list = [f.name for f in matplotlib.font_manager.fontManager.ttflist]
    print(len(font_list))
    print font_list[:10]


def main():
    print 'main'
    # def1()
    def2()
    # def3()


print __name__
if __name__ == "__main__": main()
