# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:51:43 2019

@author: Waseem Kntar
"""
def two_list_permutations(l1, l2):
    import itertools
    return list(set(itertools.chain(itertools.product(l1, l2), itertools.product(l2, l1))))

#print(list(two_list_permutations(['a'], ('a', 'y'))[0]))
def is_there_relation(s1, s2):
    
    rel1 = None
    for i in range(len(s1)):
        if s2.startswith(s1[i:]):
            if i == 0 and s1.count(s1[0]) == len(s1): # for case: 'aaa', 'aaa'
                return True, s1+s1[0], None
            elif i==0: #for case: 'ac', 'ac'
                return False, None, None
            rel1 = s1 + s2[len(s1[i:]):]
            break
    rel2 = None
    for i in range(len(s2)):
        if s1.startswith(s2[i:]):
            rel2 = s2 + s1[len(s2[i:]):]
            break
    return rel1!=None or rel2!=None, rel1, rel2

#print(is_there_relation(''.join(['A', 'C']), ''.join(['A', 'C'])))
#print(''.join(['a', 'b']))
#print(two_list_permutations(['A', 'C', 'E'], ['A', 'C', 'E']))