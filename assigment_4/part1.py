import json
import string
import matplotlib.pyplot as plt
from collections import Counter
from collections import OrderedDict

def run():
    allWords = []
    c = OrderedDict()
    fout=open('term_frequencies.txt', 'w')
    fin=open('tweet_data.json', 'r')
    for line in fin:
        tweet = json.loads(line)
        str=tweet['text']
        str=str.lower()
        L=str.split(" ")
        for i in L:
            allWords.append(i)
            punctuation = list(string.punctuation)
            stop = punctuation + [ 'a','an','the','rt', 'via','to','of','for','and','or','i','in','at','on','out','with','by','de',' ','is','am','you','you','are','my','your','our','us','me','it','','the','no','have','has','we','her','his','them','when','who','where','which','how','that','not','this','&amp;','from','new','la','but']

    sanitized = [x for x in allWords if x not in stop]
    counts = Counter(sanitized)
    for count in counts.most_common(20):
        fout.write("('%s',%s)\n" % (count[0],count[1]))
        c.update({count[0]:count[1]})

    fig = plt.figure()
    plt.title("Tweet Miner")
    plt.bar(range(len(c)), c.values())
    plt.xticks(range(len(c)),c.keys())
    fig.autofmt_xdate(bottom=0.2, rotation=90, ha='left')
    plt.savefig('term_frequencies.png')
