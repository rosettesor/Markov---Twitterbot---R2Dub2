#!/usr/bin/env python

import sys 
import random 
from random import choice

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    make_chains = input_text.split()
    stripped_words = []
    for word in make_chains:
        new_word = word.strip(".,;?")
        stripped_words.append(new_word)
    chain_dict = {}  
    counter = 0
    for word in stripped_words[0:-2]:
        key = (stripped_words[counter], stripped_words[counter+1])
        value = (stripped_words[counter+2])
        if key in chain_dict:
            chain_dict[key].append(value)
        else: 
            chain_dict[key] = [value]
        counter += 1
    return chain_dict

#Takes a dictionary of markov chains and returns random text based off an original text
def make_text(chains):
    for key, value in chain_dict:
          
          
          #rand_keys = random.choice(key)
       # return rand_keys
    
   # if rand_keys == key in chain_dict:
    #   print value
    #print rand_keys
     #^ is NOT returning a random key, keeps giving me back the first one    
    #for i in dict_keys:
     #   print chain_dict[random.choice(chain_dict.keys())]
        
        
def main():
    args = sys.argv 
    global input_text
    global chain_dict
    filename = args[1]
    # Change this to read input_text from a file
    input_text = open(filename).read()
    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    # passing in input text to create chain_dict and chain_dict into the make_text function to generate the random text
    
if __name__ == "__main__":
    main()
