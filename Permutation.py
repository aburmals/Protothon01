L="protosem"
import itertools
import nltk
#nltk.download('words')
from nltk.corpus import words
for permutation in itertools.permutations(L):
    n="".join(permutation)
    print(n)
    if n in words.words()==True:
        print(n)
