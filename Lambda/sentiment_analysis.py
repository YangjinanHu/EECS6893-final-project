import os
import json
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
#nltk.download('vader_lexicon')

sid = SentimentIntensityAnalyzer()
company_name='Google'
#fill in your file path here
path=''
file_names=os.listdir(path)

negs=[]
neus=[]
poss=[]
times=[]

for file_name in file_names:
    neg=[]
    neu=[]
    pos=[]
    file_split=file_name.split('-')
    times.append('/'.join(file_split[2:5])+':'+file_split[5])
    with open(path+file_name, encoding='utf-8') as f:
        content=f.readlines()
        content=content[0].split('\\n", "company_name": '+'"'+company_name+'"}')[:-1]
    for line in content:
        line=json.loads(line+'"}')['Data']
        if len(line.split())>5:
            ss = sid.polarity_scores(line)
            neg.append(ss['neg'])
            neu.append(ss['neu'])
            pos.append(ss['pos'])
    negs.append(sum(neg)/len(neg))
    neus.append(sum(neu)/len(neu))
    poss.append(sum(pos)/len(pos))

#save data to file
# res=[]
# with open('sen_data.txt', 'w', encoding='utf-8') as f: #fill in your file path here
#     for i in range(len(negs)):
#         cur=str(times[i])+','+str(negs[i])+','+str(neus[i])+','+str(poss[i])
#         res.append(cur)
#     f.write('\n'.join(res))

#read the data from file
# negs=[]
# neus=[]
# poss=[]
# times=[]
# with open('sen_data.txt', encoding='utf-8') as f: #fill in your file path here
#     content=f.readlines()
#     for line in content:
#         line=line.strip().split(',')
#         neg,neu,pos=map(float,line[1:])
#         time=str(line[0])
#         negs.append(neg)
#         neus.append(neu)
#         poss.append(pos)
#         times.append(time)

#plot the graph
plt.style.use('ggplot')
plt.figure(figsize=(10,5))
plt.title("Sentiment Polarity for Reddit text ({})".format(company_name))
plt.xlabel("Time")
plt.xticks(rotation=45)
plt.ylabel("Polarity Score")
plt.plot_date(times,negs,'-',label="neg_sen")
plt.plot_date(times,neus,'-',label="neu_sen")
plt.plot_date(times,poss,'-',label="pos_sen")
plt.legend()
plt.grid(True)