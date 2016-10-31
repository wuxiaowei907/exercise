# -*- coding: utf-8 -*-
"""
    Author : allenwu

"""
def break_words(stuff):
    """This function will break up words for us.""" # help(break_words)
    words = stuff.split(stuff)
    return words

def sort_words(words):
    """Sorts the words"""
    return sorted(words)

def print_first_word(words):
    """print the first word after popping it"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """print the last word after popping it"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """sort the words in the sentence"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """print the first word and last word in the sentence"""
    words =  break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sort_sentence):
    """sorts the words in the sentence and print the first one and the last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
