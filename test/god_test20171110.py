# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 16:20:46 2017

@author: LeeBaekHaeng
"""


def def1():
    w_count = {}
    lists = ["a", "id", "value", "id", "id", "value", "id", "id", "z"]
    for lst in lists:
        try:
            w_count[lst] += 1
        except:
            w_count[lst] = 1
    # print w_count

    # print w_count['id']

    id = {}

    for lst in lists:
        # print lst

        # if list == w_count['id']:
        #     print lst + w_count['id']
        # else:
        #     print lst

        # print lst+str(w_count[lst])

        # id = {lst: 0}

        # print id

        if w_count[lst] == 1:

            print lst

        else:

            try:
                id[lst] += 1
            except:
                id[lst] = 1

                # print lst + str(w_count[lst])

                # print lst

            # print lst + str(id[lst])

            if id[lst] == 1:
                print lst
            else:
                print lst + str(id[lst])

                # if id[lst] == 0:
                #     print lst
                #     id[lst] += 1
                # else:
                #     # try:
                #     #     id[lst] += 1
                #     # except:
                #     #     id[lst] = 1
                #
                #     print lst + str(id[lst])
                #
                #     id[lst] += 1

                # try:
                #     id[lst] += 1
                # except:
                #     id[lst] = 1
                #
                # print lst + str(id[lst])


# def def2():
#     cols = pd.Series(df.columns)
#     for dup in df.columns.get_duplicates(): cols[df.columns.get_loc(dup)] = [
#         dup + '.' + str(d_idx) if d_idx != 0 else dup for d_idx in range(df.columns.get_loc(dup).sum())]
#     df.columns = cols


def god_rename_columns(columns):
    rename_columns = []

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
            rename_columns.append(lst)
        else:
            try:
                id[lst] += 1
            except:
                id[lst] = 1

            if id[lst] == 1:
                print lst
                rename_columns.append(lst)
            else:
                print lst + str(id[lst])
                rename_columns.append(lst + str(id[lst]))

    return rename_columns


# def1()

# def2()

rename_columns = god_rename_columns(["a", "id", "value", "id", "id", "value", "id", "id", "z"])
print rename_columns
