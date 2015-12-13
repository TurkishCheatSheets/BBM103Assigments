import itertools
import json
import string
import matplotlib.pyplot as plt
from collections import Counter
from collections import OrderedDict



class MecburKaldimClassa(object):

    def findCoOccurrence(self,combList):
        count = 0
        x = combList[0]
        y = combList[1]

        for str in self.tweets:
            if x in str and y in str:
                count += 1
        return count

    def run(self):
        row = []
        matrix = []
        allWords = []
        topOn =[]
        self.tweets = []
        fin=open('tweet_data.json', 'r')
        for line in fin:
            tweet = json.loads(line)
            str=tweet['text']
            str=str.lower()
            self.tweets.append(str)
            L=str.split(" ")
            for i in L:
                allWords.append(i)
            punctuation = list(string.punctuation)
            stop = punctuation + [ 'a','an','the','rt', 'via','to','of','for','and','or','i','in','at','on','out','with','by','de',' ','is','am','you','you','are','my','your','our','us','me','it','','the','no','have','has','we','her','his','them','when','who','where','which','how','that','not','this','&amp;','from','new','la','but']

        sanitized = [x for x in allWords if x not in stop]
        counts = Counter(sanitized)

        for word in counts.most_common(10):
            topOn.append(word[0])

        c = list(itertools.product(topOn,topOn))

        f1=open('term_cooccurrences.txt', 'w+')
        for i in range(100):
            print >>f1,"%s-%s %s" % (c[i][0], c[i][1], self.findCoOccurrence(c[i]))

        for n in range(1,11):
            for i in range(10*(n-1),10*n):
                row.append(self.findCoOccurrence(c[i]))
            matrix.append(row)
            row = []

        fig=plt.figure()
        plt.matshow(matrix, fignum=False)
        plt.xticks(range(len(topOn)),topOn)
        plt.yticks(range(len(topOn)),topOn)
        fig.autofmt_xdate(bottom=0.1, rotation=30, ha='left')
        fig.savefig('term_cooccurrences.png')
