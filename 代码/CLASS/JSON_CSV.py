# encoding=utf8
import codecs
import sys
import io
import os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
import json
import csv

PATH = '/Users/whs/PycharmProjects/lstm/src/DATA/trec/test-2018/'
def loadJson(path): # 列表形式存储json数据
    with open(PATH+path,'r',errors='ignore') as f:
        setting = f.readlines()
        print('')
        for row in setting:
                print(row)
                row_json = json.loads(row)
                temp = row_json["allProperties"]
                item = {}
                item["id"] = temp["id"]
                item["text"] = temp["text"]
                saveNews(item,True) #True为列表形式
        # for i in id :
        # print (id)

def loadJsonLongList(path): # 一个id一个examples存储数据
    with open(path,'r') as f:
        setting = json.load(f)
        id = setting["informationTypes"]
        item = {}
        for i in range(len(id)):
            item["id"] = id[i]["id"]
            lens = len(id[i]["exampleLowLevelTypes"])
            for j in range(lens):
                item["content"] =  id[i]["exampleLowLevelTypes"][j]
                saveNews(item,False) # False为长列表格式

def saveNews(news, type):
        filePath = ''
        if (type):
        # 文件的路径 保存在与json文件同一个文件夹下
            filePath = '../DATA/trec/test-2018/json1.csv'
        else:
            filePath = '/Users/whs/work/trec-master/src/data/jsonLonglist.csv'
        file = open(filePath, 'a+',encoding='utf-8',errors='ignore')
        titleName = ['id','text']
        writer = csv.DictWriter(file, fieldnames = titleName)
        writer.writerow(news)


if __name__ == "__main__":
    path = '../DATA/trec/test-2018/'
    allFile = os.listdir(path)
    filePaths = []
    for fileName in allFile:
        if (fileName != '.DS_Store'):
            loadJson(fileName)
