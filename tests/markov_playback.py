from __future__ import division
from random import random

def get_next_word(word_dictionary):
    total_count = 0
    for word,count in word_dictionary.items():
        total_count+=count

    rand_value = random()
    probability_sum = 0

    for word,count in word_dictionary.items():
        probability_sum += count/total_count
        if(probability_sum >= rand_value):
            return word

def build_output(markov_chain,number_of_words, first_word):
    previous_word = first_word
    output = ""
    for i in range(number_of_words):
        next_word = get_next_word(markov_chain[previous_word])
        output += '{} '.format(next_word)
        previous_word = next_word

    return output

def build_markov_chain(token_stream):
    previous_token = "_____"
    markov_chain = {}
    for token in token_stream:
        # if(previous_token in markov_chain):
        if(previous_token not in markov_chain):
            markov_chain[previous_token] = {}

        if(token in markov_chain[previous_token]):
            markov_chain[previous_token][token] += 1
        else:
            markov_chain[previous_token][token] = 1
        previous_token = token

    return markov_chain

# def render_output(token_stream):
#     capitalize_next_token = True
#     rendered_output = ""
#     for token in token_stream:
#         if(capitalize_next_token):
#            token = token.capitalize()

#         if(token not in ',.)"\''):
#             token = " " + token
#             capitalize_next_token = False
#         else:
#             capitalize_next_token = True
