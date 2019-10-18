# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 09:43:12 2019

@author: ki10m
"""

import datetime

d1 = datetime.date(2019,10,18)
d2 = datetime.date(2019,10,30)

print('日付：'+str(d1)+'\n日付：'+str(d2)+'\n日付間の日数:'+str(abs(int(d1.day)-int(d2.day))))
