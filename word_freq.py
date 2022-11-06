import sys
import json

words = {}
with open(sys.argv[1], 'r+') as f:
    for line in list(f):
        for word in line.split(' '):
            word = word.strip()
            if word.isalpha():
                word = word.lower()
            else:
                word = word[:-1].lower()
            if len(word) == 0:
                continue
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

print(json.dumps(words))
