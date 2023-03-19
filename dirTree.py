# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 11:09:31 2022

@author: MartinAndersson
"""

import os
import sys
import re

os.chdir("C:/Calluna/MyGit/Python")
os.getcwd()

longFiles = list()

for bDir, sDir, fileNm in os.walk(os.getcwd()):
    for file in fileNm:
        if len(file) > 0:
            filePath=bDir+file
            if len(filePath) > 200:
                longFiles.append(filePath)
                
orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

for i in longFiles:
    i=re.sub("(å|ä)", "a", i, flags=re.I)
    i=re.sub("ö", "o", i, flags=re.I)
    print(i)

f.close()