import re
import vincent
import operator 
import json
from collections import Counter
from nltk.corpus import stopwords
import string
import pandas

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens
 
# tweet = "RT @marcobonzanini: just an example! :D http://example.com #NLP"
# print(preprocess(tweet))
# # ['RT', '@marcobonzanini', ':', 'just', 'an', 'example', '!', ':D', 'http://example.com', '#NLP']

fname = 'python.json'

# with open(fname, 'r') as f:
#     count_all = Counter()
#     for line in f:
#         tweet = json.loads(line)
#         # Create a list with all the terms
#         terms_all = [term for term in preprocess(tweet['text'])]
#         # Update the counter
#         count_all.update(terms_all)
#     # Print the first 5 most frequent words
#     print(count_all.most_common(5))

# search_word = 'python' # pass a term as a command-line argument
# count_terms_only = Counter()

 
# punctuation = list(string.punctuation)
# stop = punctuation + ['rt', 'via']

f = open(fname, 'r')
# for line in f:
#     tweet = json.loads(line)
#     terms_only = [term for term in preprocess(tweet['text']) 
#                   if term not in stop 
#                   and not term.startswith(('#', '@'))]
#     if search_word in terms_only:
#         count_terms_only.update(terms_only)
# # print("Co-occurrence for %s:" % search_word)
# # print(count_terms_only.most_common(20))


# word_freq = count_terms_only.most_common(20)
# labels, freq = zip(*word_freq)
# data = {'data': freq, 'x': labels}
# bar = vincent.Bar(data, iter_idx='x')
# bar.to_json('term_freq.json')
# #bar.to_json('term_freq.json', html_out=True, html_path='chart.html')

dates_ITAvWAL = []
# f is the file pointer to the JSON data set
for line in f:
    tweet = json.loads(line)
    # let's focus on hashtags only at the moment
    terms_hash = [term for term in preprocess(tweet['text']) if term.startswith('#')]
    # track when the hashtag is mentioned
    if '#NCWIT' in terms_hash:
    	print("1")
        dates_ITAvWAL.append(tweet['created_at'])
 
# a list of "1" to count the hashtags
ones = [1]*len(dates_ITAvWAL)
# the index of the series
idx = pandas.DatetimeIndex(dates_ITAvWAL)
# the actual series (at series of 1s for the moment)
ITAvWAL = pandas.Series(ones, index=idx)
 
# Resampling / bucketing
per_minute = ITAvWAL.resample('1Min', how='sum').fillna(0)

time_chart = vincent.Line(ITAvWAL)
time_chart.axis_titles(x='Time', y='Freq')
time_chart.to_json('time_chart.json',html_out=True, html_path='chart.html')

