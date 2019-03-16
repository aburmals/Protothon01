L="protosem"
import itertools
import nltk
from nltk.corpus import words #importing word dictionary
for permutation in itertools.permutations(L):
    n="".join(permutation)
    print(n) #all permutations
    if n in words.words()==True:
        print(n) #correct permutations
