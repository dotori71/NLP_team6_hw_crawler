# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 01:15:57 2022

@author: rinsu
"""
import os
import nltk
def printPath(level, path):
 text_ppt=[]
 '''''
 列印一個目錄下的所有資料夾和檔案
 '''
 # 所有資料夾，第一個欄位是次目錄的級別
 dirList = []
 # 所有檔案
 fileList = []
 # 返回一個列表，其中包含在目錄條目的名稱
 files = os.listdir(path)
 # 先新增目錄級別
 dirList.append(str(level))
 for f in files:
  if(os.path.isdir(path + '/' + f)):
   # 排除隱藏資料夾。因為隱藏資料夾過多
   if(f[0] == '.'):
    pass
   else:
    # 新增非隱藏資料夾
    dirList.append(f)
  if(os.path.isfile(path + '/' + f)):
   # 新增檔案
   fileList.append(f)
 # 當一個標誌使用，資料夾列表第一個級別不列印
 i_dl = 0
 for dl in dirList:
  if(i_dl == 0):
   i_dl = i_dl + 1
  else:
   # 列印至控制檯，不是第一個的目錄
   print('-' * (int(dirList[0])), dl )
   # 列印目錄下的所有資料夾和檔案，目錄級別+1
   printPath((int(dirList[0]) + 1), path + '/' + dl)
 for fl in fileList:
  with open(path+"/"+fl,'r',encoding='utf-8') as fh:
    tmp = fh.read()
    tmps=tmp.split()
    text_ppt=text_ppt+tmps
 return text_ppt
 
if __name__ == '__main__':
 plant_text=printPath(1, 'C:/Users/rinsu/OneDrive/桌面/FreqList-Word2Vec/Plant')
 all_words = nltk.FreqDist(w.lower() for w in plant_text)
 word_features_plant = list(all_words)[:2000]
 print(word_features_plant)
 techjob_text=printPath(1, 'C:/Users/rinsu/OneDrive/桌面/FreqList-Word2Vec/Tech_Job')
 all_words2 = nltk.FreqDist(w.lower() for w in techjob_text)
 word_features_techjob = list(all_words2)[:2000]
 print(word_features_techjob)
 
