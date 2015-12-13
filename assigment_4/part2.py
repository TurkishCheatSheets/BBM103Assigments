import json
import string
import matplotlib.pyplot as plt
from collections import Counter
from collections import OrderedDict
from datetime import datetime

def run():
    timeList={}
    dateList={}
    dataset ={}
    dateset ={}
    topWords=[]
    allWords = []
    times=[]
    fin=open('tweet_data.json', 'r')
    for line in fin:
        tweet = json.loads(line)
        str=tweet['text']
        str=str.lower()
        L=str.split(" ")
        date=tweet["created_at"]
        time = datetime.strptime(date, "%a %b %d %H:%M:%S +0000 %Y").strftime("%Y-%m-%d %H:%M")
        timeList.update({str:time})
        for i in L:
            allWords.append(i)
        punctuation = list(string.punctuation)
        stop = punctuation + [ 'a','an','the','rt', 'via','to','of','for','and','or','i','in','at','on','out','with','by','de',' ','is','am','you','you','are','my','your','our','us','me','it','','the','no','have','has','we','her','his','them','when','who','where','which','how','that','not','this','&amp;','from','new','la','but']

    sanitized = [x for x in allWords if x not in stop]
    counts = Counter(sanitized)
    for count in counts.most_common(5):
        topWords.append(count[0])

    timeList = OrderedDict(sorted(timeList.items(), key=lambda x: x[1]))

    for word in topWords:
        for tweet in timeList.keys():
            if word in tweet:
                times.append(timeList[tweet])
                c = OrderedDict(sorted(Counter(times).items(), key=lambda x: x[0]))
        dataset.update({word:c.values()})
        dateset.update({word:c.keys()})
        times = []

    f1=open('term_frequencies_overtime.txt', 'w+')
    for word in topWords:
        word = word.encode("utf-8")
        for date in dateset[word]:
            print >>f1,"%s %s:00 %s" % (word,date,dataset[word][dateset[word].index(date)])

    fig = plt.figure()
    for word in dataset:
        plt.plot(dataset[word])
        plt.legend(dataset.keys())
    plt.xticks(range(len(c.keys())),[datetime.time(datetime.strptime(timedata, "%Y-%m-%d %H:%M")).strftime("%H:%M") for timedata in c.keys()])
    plt.xlabel("Time")
    plt.ylabel("Frequency of ocurrence")
    fig.autofmt_xdate(bottom=0.2, rotation=90, ha='left')
    plt.savefig('term_frequencies_overtime.png')
