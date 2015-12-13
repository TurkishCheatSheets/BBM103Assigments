# -*- coding: utf-8 -*-

import json
import string
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

f=open('tweet_data.json', 'r')
line = f.readline() # read only the first tweet/line
tweet = json.loads(line) # load it as Python dict
print tweet.keys()
created_at_format = '%a %b %d %H:%M:%S +0000 %Y'
str=tweet['text']#tweet
str=str.lower()
L=str.split(" ");
date=tweet["created_at"];#date-time in ISO format
dt=datetime.strptime(date, "%a %b %d %H:%M:%S +0000 %Y") #reading date in ISO format
print date
print dt.year
print dt.month
print dt.day
print dt.hour
print(str)
print L;
print('\n')
punctuation = list(string.punctuation)
stop = punctuation+[ 'a','an','the','rt', 'via','to','of','for','and','or','i','in','at','on','out','with','by','de',' ','is','am','are','my','your','our','us','me','you','it','','the','no','have','has','we','her','his','them','when','who','where','which','how','that','not','this','&amp;','from','new','la','but']



#Saving a plot figure as image
fig=plt.figure()
x=np.linspace(0,10,30)
y=x*x;
plt.plot(x,y)
plt.savefig('sample_plot.png')
plt.show()
