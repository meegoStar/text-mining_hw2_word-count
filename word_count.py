# write your code here
import nltk
# nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# nltk.download()

from collections import Counter

stop_words = set(stopwords.words('english'))

def accept_word(token):
        if token.isalpha():
            return not token in stop_words
        else:
            return False

if __name__ == '__main__':
    lines = []
    with open('building_global_community.txt') as f:
        for line in f:
            line = line.lower()
            lines.append(line)
            
    lines = ''.join(lines)
    tokens = word_tokenize(lines)

    words = []
    for token in tokens:
        if accept_word(token):
            words.append(token)

    word_counter = Counter(words)

    for word, count in word_counter.most_common(20):
        print("'", word, "': ", count)