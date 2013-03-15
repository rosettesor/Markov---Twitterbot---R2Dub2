#!/usr/bin/env python

import sys  
from random import choice

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    make_chains = input_text.split()
    
    stripped_words = []
    for word in make_chains:
        ind_word = word.strip(".,;?")
        stripped_words.append(ind_word)

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
    # print chain_dict


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    markov_chain = make_chains()
    for key,value in markov_chain:
        print key + " " + choice(value)

def main():
    args = sys.argv 
    global input_text
    filename = args[1]
    # Change this to read input_text from a file
    input_text = open(filename).read()
    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()
