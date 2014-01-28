#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import sys

grail_seekers = [
    "What is your name?",
    "What is your quest?",
]

common = [
    "What's your name?",
    "Where are you from?",
    "Hobbies?",
    "What do you want to get out of codefellows?",
]

questions_filename = "questions.txt"
pool = []
with open(questions_filename, 'r') as questions:
    pool = questions.readlines()


def ask_questions(silly=False):
    """ask five questions, for in common, one randomly selected"""
    shared = common
    if silly:
        shared = grail_seekers
    all_questions = shared + [random.choice(pool).strip()]
    for question in all_questions:
        print question

if __name__ == '__main__':
    kwargs = {}
    if (len(sys.argv) > 1) and sys.argv[1] == 'grail':
        kwargs['silly'] = True
    ask_questions(**kwargs)
