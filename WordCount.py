# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 19:18:41 2020

@author: ptanu
"""
#%%
f1=open("C:/Users/ptanu/Desktop/Tanuj_Java/abc.txt",'r')
d=dict()
for line in f1:
    words=str(line)
    l1=words.split()
    for word in l1:
        d[word]=d.get(word,0)+1
print(d)