"""
Simulation/solver of the infinite
monkey theorem: a monkey hitting keys at random 
on a keyboard for an infinite amount
of time will almost surely type a given text,
such as the complete works of William Shakespeare. 
"""

import random
import string



def gen_string(gen_length):
    gen_s = ''
    chars = string.ascii_lowercase + ' '
    for i in range(gen_length):
        gen_s += chars[random.randrange(len(chars))]
    return gen_s

def score_sentence(generated_s, target_s):
    score = 0
    for i in range(len(generated_s)):
        if generated_s[i] == target_s[i]:
            score += 1
        else:
            break
    return score


# Simple vesrion:
def run_simulation_simple(target_s):
    matched = False
    num_tries = 0
    st_len = len(target_s)
    best_score = 0
    while not matched:
        generated_s = gen_string(st_len)
        score = score_sentence(generated_s, target_s)

        if score > best_score:
            best_score = score
        if score == st_len:
            matched = True
            num_tries += 1
        if num_tries % 1000 == 0:
            print best_score, target_s[:best_score]


# Better vesrion (will end in our lifetime!!):
# keeps the best_score string so far and builds
# each try.
def run_simulation_better(target_s):
    matched = False
    num_tries = 0
    st_len = len(target_s)
    best_score = 0
    while not matched:
        generated_s = target_s[:best_score] + gen_string(st_len - best_score)
        print generated_s
        score = score_sentence(generated_s, target_s)

        if score > best_score:
            best_score = score
        if score == st_len:
            matched = True
            num_tries += 1
        if num_tries % 1000 == 0:
            print best_score, target_s[:best_score]



run_simulation_better("methinks it is like a weasel")
