#%% 1
import requests
from bs4 import BeautifulSoup
import nltk
from collections import Counter

#%% 2
# Getting the moby dick HTML 
r = requests.get("https://www.gutenberg.org/cache/epub/521/pg521-images.html")

# Setting the encoding of the HTML page
r.encoding = 'utf-8'
html = r.text
#print(html[0:2000])


#%% 3
# Creating a BeautifulSoup object from the HTML
soup = BeautifulSoup(html,features = "lxml")

# Get text out of the soup
text = soup.get_text()
#print(text[32000:34000])

#%% 4
# Creating a tokenizer
tokenizer = nltk.tokenize.RegexpTokenizer("\w+")
# Tokenize the text
tokens = tokenizer.tokenize(text)
# Printing out the first 8 words / tokens 
#print(tokens[0:8])

#%% 5
# Create a list called words containing all tokens transformed to lower-case
words = [t.lower() for t in tokens]

# Printing out the first 8 words / tokens 
#print(words[0:8])

#%% 6  #if this cell raises error <<<<>>>> nltk.download('stopwords')
# Get the English stop words from nltk
sw = nltk.corpus.stopwords.words("english")
#print(sw[0:8])

#%% 7
# All words that are in words but not in sw
words_ns = [x for x in words if x not in sw]

# Check that stop words are gone
print(words_ns[0:5])

#%% 8
# Initialize a Counter object from our processed list of words
count = Counter(words_ns)

top_ten = count.most_common(20)
# Print the top ten words and their counts
print(top_ten)

print("the most common word is "+ top_ten[0][0])














