#!/usr/bin/python3

def multiple_returns(input_sentence):
    """
    Analyzes a sentence and returns a tuple containing its length and first character
    """
    sentence_length = len(input_sentence)
    if sentence_length == 0:
        first_character = None
    else:
        first_character = input_sentence[0]
    return (sentence_length, first_character)
