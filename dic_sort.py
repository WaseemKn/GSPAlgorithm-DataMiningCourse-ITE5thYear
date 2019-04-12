# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 17:52:12 2019

@author: Waseem Kntar
"""

def dic_sort(dic, reverse = False):
    import operator
    import collections as cllns
    sorted_dic_as_tuples = sorted(dic.items(), key=operator.itemgetter(1), reverse = reverse)
    sorted_dic = cllns.OrderedDict(sorted_dic_as_tuples)
    return sorted_dic