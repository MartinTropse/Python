# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 20:43:31 2022
@author: marti
"""

import os
import pandas as pd
import time 
import re

"""
ompF-F TACGTGATGTGATTCCGTTC
RevComp ompF-F - GAACGGAATCACATCACGTA
ompF-R TGTTATAGATTTCTGCAGCG
RevComp ompF-R - CGCTGCAGAAATCTATAACA
csgD-F 	       GGACTTCATTAAACATGATG - 49283 
RevComp csgD-F CATCATGTTTAATGAAGTCC
csgD-R	       TGTTTTTCATGCTGTCAC
RevComp csgD-R GTGACAGCATGAAAAACA
Start csgD #CGCACACCTGACAG
Close to end #CTTTGGTATGAAC
Start ompF #GAGCCAGCG
End ompF #GAGGGTAATAAAT
"""

os.chdir("C:/Bas/AquaBiota/Projekt/ECWA-NOR/Download_Ecoli_Human/Unlabeled/1_ncbi-genomes-2022-04-03")
path = "C:/Bas/AquaBiota/Projekt/ECWA-NOR/Download_Ecoli_Human/Unlabeled/"

os.listdir()

primerL_ompF = ["TACGTGATGTGATTCCGTTC","GAACGGAATCACATCACGTA","TGTTATAGATTTCTGCAGCG","CGCTGCAGAAATCTATAACA"]
primerL_csgD = ["GGACTTCATTAAACATGATG","CATCATGTTTAATGAAGTCC","TGTTTTTCATGCTGTCAC","GTGACAGCATGAAAAACA"]

aFile=open("GCF_021228975.1_ASM2122897v1_genomic.txt", "r")
fFile=open("GCF_021228975.1_ASM2122897v1_genomic.fna", "r")
fLines = fFile.readlines()

"""
ompF-F TACGTGATGTGATTCCGTTC
RevComp ompF-F - GAACGGAATCACATCACGTA
ompF-R TGTTATAGATTTCTGCAGCG
RevComp ompF-R - CGCTGCAGAAATCTATAACA
#csgD ConservedEnd AAAATACAGGTTGCGT
#csgD ConservedEnd RevCo ACGCAACCTGTATTTTG
#ompF ConservedStart CTCTTTTTTTATCCTTTCT
#ompF ConservedStart_RevCo AGAAAGGATAAAAAAAGAG
#ompF ConservedStart_RevCo  CAAACAGATAACTTGAC
#ompF ConservedStart        GAGCCAGCGCCTGCT
#ompF ConservedEnd CCATGAGGGTAATAAATA
#ompF ConservedEnd_RevCo TATTTATTACCCTCATGG
"""
#>NZ_JAKNIX010000140.1 Escherichia coli strain MSK.23.64 DNELBDIN_140, whole genome shotgun sequence
#NZ_JAKNIX010000051.1 Escherichia coli strain MSK.23.64 DNELBDIN_51

primerD_ompF = {"ompF-F":"TACGTGATGTGATTCCGTTC","RevComp ompF-F":"GAACGGAATCACATCACGTA","ompF-R":"TGTTATAGATTTCTGCAGCG","RevComp ompF-R":"CGCTGCAGAAATCTATAACA"}
primerD_csgD = {"csgD-F":"GGACTTCATTAAACATGATG","csgD-F_RevCo":"CATCATGTTTAATGAAGTCC","csgD-R":"TGTTTTTCATGCTGTCAC","csgD-R_RevCo":"GTGACAGCATGAAAAACA"}

xMatch=re.search("CGCTGCAGAAATCTATAACA", x)
#key, value = list(lsDict[0].items())[0]

errorList = []

for root, dirs, files in os.walk(path):   
    for file in files:     
        if file.endswith("genomic.fna"):
            seqFile=open(root+"/"+file,'r')
            seqLines=seqFile.readlines()
            seqStr="".join(str(e) for e in seqLines)
            seqStr=re.sub("\\n","",seqStr)
            seqList = list()
            for oPrim in primerD_ompF:
                oMatch=re.search(primerD_ompF[oPrim], seqStr)
                try:
                    if len(oMatch[0])>0:
                        seqList.append(oMatch.start())
                        seqList.append(oMatch.end())
                        print("A match in:\n",root, "/", file)
                        print("With primer ", oPrim)
                        del(oMatch)
                        if len(seqList)>3:
                            expStr=str(">"+file+"\n"+seqStr[min(seqList):max(seqList)])
                            text_file = open(root+"/"+"ompF_"+file, "w")
                            text_file.write(expStr)
                            text_file.close()
                            print("Exported ompF region in:\n", root)
                            print(len(seqList))
                except Exception as e:
                    errorList.append(e)


for aX in primerD_csgD:
    primerD_csgD[aX]

errorList = []

for root, dirs, files in os.walk(path):   
    for file in files:     
        if file.endswith("genomic.fna"):
            seqFile=open(root+"/"+file,'r')
            seqLines=seqFile.readlines()
            seqStr="".join(str(e) for e in seqLines)
            seqStr=re.sub("\\n","",seqStr)
            seqList = list()
            for cPrim in primerD_csgD:
                cMatch=re.search(primerD_csgD[cPrim], seqStr)
                try:
                    if len(cMatch[0])>0:
                        print("A match in:\n",root, "/", file)
                        print("With primer ", cPrim)
                        seqList.append(cMatch.start())
                        seqList.append(cMatch.end())    
                        del(cMatch)
                        if len(seqList)>2:
                            expStr=str(">"+file+"\n"+seqStr[min(seqList):max(seqList)])
                            text_file = open(root+"/"+"csgD"+file, "w")
                            text_file.write(expStr)
                            text_file.close()
                            print("Exported csgD region in:\n", root)
                            print(len(seqList))
                except Exception as e:
                    errorList.append(e)


for root, dirs, files in os.walk(path):   
    for file in files:     
        if file.endswith("genomic.fna"):
            seqFile=open(root+"/"+file,'r')
            seqLines=seqFile.readlines()
            headLine=seqLines[0]
            seqStr="".join(str(e) for e in seqLines[1:len(seqLines)])
            seqStr=re.sub("\\n","",seqStr)
            seqStr=headLine+seqStr
            newFile = open(root+"/"+file[0:-3]+"txt","w")
            newFile.write(seqStr)
            newFile.close()


for root, dirs, files in os.walk(path):   
    for file in files:     
        if file.endswith("genomic.fna"):
            seqFile=open(root+"/"+file,'r')
            seqLines=seqFile.readlines()
            seqStr="".join(str(e) for e in seqLines)
            seqStr=re.sub("\\n","",seqStr)
            print(seqStr[1:1000])
            time.sleep(5)            





pd.read_csv()


seqStr=re.sub("\\n","",seqStr) 
