#%% 1
# Importing requests, BeautifulSoup, nltk, and Counter
import requests
from bs4 import BeautifulSoup
import nltk
from collections import Counter

#%% 2
# Getting the Moby Dick HTML 
r = requests.get("https://www.gutenberg.org/cache/epub/521/pg521-images.html")

# Setting the correct text encoding of the HTML page
r.encoding = 'utf-8'

# Extracting the HTML from the request object
html = r.text

# Printing the first 2000 characters in html
#print(html[0:2000])


#%% 3
# Creating a BeautifulSoup object from the HTML
soup = BeautifulSoup(html,features = "lxml")

# Getting the text out of the soup
text = soup.get_text()

# Printing out text between characters 32000 and 34000
#print(text[32000:34000])
#%% 4
# Creating a tokenizer
tokenizer = nltk.tokenize.RegexpTokenizer("\w+")

# Tokenizing the text
tokens = tokenizer.tokenize(text)

# Printing out the first 8 words / tokens 
#print(tokens[0:8])
#%% 5
# Create a list called words containing all tokens transformed to lower-case
words = [t.lower() for t in tokens]

# Printing out the first 8 words / tokens 
#print(words[0:8])

#%% 6  #if this cell raises error <<<<>>>> nltk.download('stopwords')
# Getting the English stop words from nltk
sw = nltk.corpus.stopwords.words("english")

# Printing out the first eight stop words
print(sw[0:8])

#%% 7
# Create a list words_ns containing all words that are in words but not in sw
words_ns = [x for x in words if x not in sw]

# Printing the first 5 words_ns to check that stop words are gone
print(words_ns[0:5])

#%% 8
# Initialize a Counter object from our processed list of words
count = Counter(words_ns)

# Store 10 most common words and their counts as top_ten
top_ten = count.most_common(20)

# Print the top ten words and their counts
print(top_ten)

print("most common word is unsuprisingly > '"+ top_ten[0][0]+"'!" )














