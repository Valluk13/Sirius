import pandas as pd
from itertools import permutations
import math

df = pd.read_csv('data.csv', skipinitialspace=True, sep=';')

cl2 = []

df1 = pd.DataFrame()
for i in df['phrase']:
    if isinstance(i, str) and len(i.split()) <= 5:
        cl2.append(i)

df1['phrase'] = cl2 
df1.to_csv('text.txt', sep='\t', index=False)
f = open('text.txt', 'r', encoding='UTF-8')
text = f.read()

from nltk import word_tokenize
text_tokens = word_tokenize(text)

import nltk
text = nltk.Text(text_tokens)

from nltk.probability import FreqDist
fdist = FreqDist(text)

from nltk.corpus import stopwords
words = stopwords.words('english')

text_tokens = [token.strip() for token in text_tokens if token not in words]
text = nltk.Text(text_tokens)
fdist_sw = FreqDist(text)

words = list(map(lambda x: x[0], fdist_sw.most_common(100)))

df_with_words = pd.DataFrame()
df_with_words['words'] = words 
df_with_words.to_csv('bad_words.csv')