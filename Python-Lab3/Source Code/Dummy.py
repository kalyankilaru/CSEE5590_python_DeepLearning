import collections

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.util import bigrams


def generate_word_tokens(text):

    lemmatizer = WordNetLemmatizer()

    return [lemmatizer.lemmatize(x.lower()) for x in word_tokenize(text) if x.isalpha()]


all_tokens = generate_word_tokens(open("input.txt").read())


all_bigrams = [bigram for bigram in bigrams(all_tokens)]


print(" 5 Most frequent Bi-grams")

counter = {}

for bigram in all_bigrams:

    counter[bigram] = 1 if bigram not in counter else counter[bigram] + 1

output = collections.Counter(counter).most_common(5)

output_keys = set()

for key, value in output:

    print(key, "->", value)

    output_keys.add(key)

print("Summarization")

output = ""

with open("input.txt") as infile:

    for line in infile:

        for sentence in sent_tokenize(line):

            current_key_set = set(bigram for bigram in bigrams(generate_word_tokens(sentence)))

            if output_keys & current_key_set:

                output += sentence + " "

                continue

print(output)