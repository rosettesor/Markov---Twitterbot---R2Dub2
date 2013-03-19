#!/usr/bin/env python

import sys 
import random 
import twitter

def tweet(random_text):
    post = raw_input("post to twitter?" )
    if post == "yes":
        mytwitteraccount = twitter.Api(consumer_key="o8ZGuP2NWRJNPKeqJdSziQ", 
                                consumer_secret="KKs43JnbPsugLJnlfvrUygMQ6NjOG5XKBX4ouw", 
                                access_token_key="1279577575-XuMifW57kvD710bbN1XrzOpHV0TGLapKrTQLMmV", 
                                access_token_secret="XKSr0ElVnneETT4dPPl6PiVE5BDFJ4eTAUh5awDpkhs")
        if len(random_text) <= 140:
            status = mytwitteraccount.PostUpdate(random_text)
            return status
        else:
            return
        status = mytwitteraccount.PostUpdates(random_text)

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    make_chains = corpus.split()
    stripped_words = []
    for word in make_chains:
        new_word = word.strip(".,;!?")
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
    key_list = []
    for key in chains:
        key_list.append(key)

    random_number = random.randint(0,(len(key_list)-1))   
   
    random_key = key_list[random_number] 

    # makes the tuple "random_key" into a list
    new_sentence = [random_key[0], random_key[1]]

    while len(new_sentence) < 10:
        last_two_words = (new_sentence[-2], new_sentence[-1])
        if last_two_words not in key_list:
            last_two_words = random.choice(key_list)
        # the value in the dictionary pointing to the key above
        new_add = random.choice(chains[last_two_words])
        new_sentence.append(new_add)
        # makes the list "new_sentence" into a string
        sentence = " ".join(new_sentence)
    return sentence

def main():
    args = sys.argv 
    global input_text
    filename = args[1]
    # Change this to read input_text from a file
    input_text = open(filename).read()
    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text
    tweet(random_text)
    # passing in input text to create chain_dict and chain_dict into the make_text function to generate the random text

if __name__ == "__main__":
    main()