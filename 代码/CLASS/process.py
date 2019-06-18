import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import string
import nltk
import warnings
import os
label_list = ["GoodsServices",
        "SearchAndRescue",
        "InformationWanted",
        "Volunteer",
        "FundRaising",
        "Donations",
        "MovePeople",
        "FirstPartyObservation",
        "ThirdPartyObservation",
        "Weather",
        "EmergingThreats",
        "NewSubEvent",
        "MultimediaShare",
        "ServiceAvailable",
        "Factoid",
        "Official",
        "CleanUp",
        "Hashtags",
        "ContextualInformation",
        "News",
        "Advice",
        "Sentiment",
        "Discussion",
        "Irrelevant",
        "OriginalEvent"]
warnings.filterwarnings("ignore", category=DeprecationWarning)

path = '../DATA/'
# path = '../DATA/muticlassification/'
# path = '../data/training_data/training1/'
allFile = os.listdir(path)
filePaths = []
temp = {}
temp['id'] = []
temp['text'] = []
for i in label_list:
    temp[i] = []

for fileName in allFile:
    if (fileName != '.DS_Store'):
        name = path + fileName
        filePaths.append(name)
for file in filePaths:
        print(file)
        combi = pd.read_csv(file, header=0,names=['id','label','import_label','text'])
        # combi = pd.read_csv(file,  names=['id', 'label', 'text'])
        def remove_pattern(input_txt, pattern):
            r = re.findall(pattern, input_txt)
            for i in r:
                input_txt = re.sub(i, '', input_txt)

            return input_txt
        combi['text'] = np.vectorize(remove_pattern)(combi['text'],
                                                     "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+] | [!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
        combi['text'] = np.vectorize(remove_pattern)(combi['text'], "@[\w]*")
        # pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-FA-F][0-9a-FA-F]))+')
        # remove special characters, numbers, punctuations
        combi['text'] = combi['text'].str.replace("[^a-zA-Z#]", " ")
        combi['text'] = combi['text'].apply(lambda x: ' '.join([w for w in x.split() if len(w) > 3]))
        combi.head()
        for row_index, row in combi.iterrows():
            for i in label_list:
                if i in row['label']:
                    temp[i].append(1)
                else:
                    temp[i].append(0)
            temp['id'].append(row['id'])
            temp['text'].append(row['text'])
        df = pd.DataFrame(temp)
        df.to_csv('../DATA/new.csv',index=False)
        # print(df.head())



        # # remove twitter handles (@user)
        # combi['text'] = np.vectorize(remove_pattern)(combi['text'], "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+] | [!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
        # combi['text'] = np.vectorize(remove_pattern)(combi['text'], "@[\w]*")
        # # pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-FA-F][0-9a-FA-F]))+')
        # # remove special characters, numbers, punctuations
        # combi['text'] = combi['text'].str.replace("[^a-zA-Z#]", " ")
        # combi['text'] = combi['text'].apply(lambda x: ' '.join([w for w in x.split() if len(w) > 3]))
        # # def  jugde(x):
        # #     if x == 'high' or x == 'medium' or x == 'low':
        # #         x=x
        # #     elif float(x) > 0.7 :
        # #         x = 'high'
        # #     elif float(x) < 0.3 :
        # #         x = 'low'
        # #     elif float(x) < 0.7 and float(x)>0.3 :
        # #         x = 'medium'
        # #     else:
        # #         print('error')
        # combi['id'] = combi["id"].apply(lambda x: eval(x) )
        # #
        # # combi['import_label'] = combi['import_label'].apply(lambda x: '0.6' if float(x) <= 0.7 and float(x) >= 0.5 else x)
        # # combi['import_label'] = combi['import_label'].apply(lambda x: '0.8' if float(x) > 0.7 else x)
        # # combi['import_label'] = combi['import_label'].apply(lambda x: '0.2' if float(x) < 0.5 else x)
        # # combi['import_label'] = combi['import_label'].apply(lambda x: 'medium' if x == '0.6' else x)
        # # combi['import_label'] = combi['import_label'].apply(lambda x: 'high' if x == '0.8' else x)
        # # combi['import_label'] = combi['import_label'].apply(lambda x: 'low' if x == '0.2' else x)
        # # Let’s take another look at the First Few rows oF the combined dataFrame.
        # # combi.head()
        # from nltk.stem.porter import *
        # stemmer = PorterStemmer()
        # tokenized_tweet = combi['text'].apply(lambda x: [stemmer.stem(i) for i in x])  # stemming
        # name = file.split('/')[-1]
        # combi.to_csv("../DATA/clean1/"+name, header=False,index=False,columns=['id', 'label','text'])


