# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 18:48:09 2021

@author: 91937
"""


def solve (N, edge):
    # Type your code here
    d={}
    for ele in edge:
        start=ele[0]
        end=ele[1]
        if start in d:
            d[start].append(end)
        else:
            d[start]=[end]
            
    print(d)

    return # Dummy return

N = int(input())
edge = [list(map(int, input().split())) for i in range(N-1)]

out_ = solve(N, edge)


#sample = {}
#sample["name"] = ["akash"]
#sample["name"].append("akash1")

#print(sample)