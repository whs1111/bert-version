import json
import csv
import pandas as pd
# path = '/Users/whs/work/search/ITR-H.types.json'
def loadJson(path): # 列表形式存储json数据
    data = pd.read_csv("../DATA/trec/test-2018/json.csv", name=['id', 'text'])
    with open(path,'r') as f:
        setting = json.load(f)
        events = setting["events"]
        print(len(events))
        for i in range(len(events)):
            tweetslist = events[i]["tweets"]
            for j in range(len(tweetslist)):
                item = {}
                item["id"] = (tweetslist[j]["postID"])
                text = data.loc[item["id"],'text']
                print(text)

                item["label1"] = tweetslist[j]["categories"]  
                item["label2"] = tweetslist[j]["priority"] 
                saveNews(item,True) #True为列表形式
        # for i in id :
        # print (id)



def saveNews(news, type):
        filePath = ''
        if (type):
        # 文件的路径 保存在与json文件同一个文件夹下
            filePath = '/Users/whs/jsontest.csv'
        else:
            filePath = '/Users/whs/work/trec-master/src/data/jsonLonglist.csv'
        file = open(filePath, 'a+')
        titleName = ['id','label1','label2']
        writer = csv.DictWriter(file, fieldnames = titleName)
        writer.writerow(news)


if __name__ == "__main__":
    filePath = '../DATA/trec/test-2018/json.csv'
    # for i in range(6):
    #     loadJson("/Users/whs/label/assr"+str(i+1)+".json")
    with open(filePath,'r',errors='ignore') as f:
        line = csv.reader(f)
        for li in line :
            print(li[0]) 







