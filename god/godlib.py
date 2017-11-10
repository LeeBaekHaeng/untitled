# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 11:55:58 2017

@author: LeeBaekHaeng
"""


def duplicate_column_rename(columns):
    duplicate_columns_rename = []

    column_count = {}

    for lst in columns:
        try:
            column_count[lst] += 1
        except:
            column_count[lst] = 1

    id = {}

    for lst in columns:
        if column_count[lst] == 1:
            print lst
            duplicate_columns_rename.append(lst)
        else:
            try:
                id[lst] += 1
            except:
                id[lst] = 1

            if id[lst] == 1:
                print lst
                duplicate_columns_rename.append(lst)
            else:
                print lst + str(id[lst])
                duplicate_columns_rename.append(lst + str(id[lst]))

    return duplicate_columns_rename


def main():
    columns = ["a", "id", "value", "id", "id", "value", "id", "id", "z"]
    print duplicate_column_rename(columns)


if __name__ == "__main__":
    main()
