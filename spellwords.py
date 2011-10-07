#!/usr/bin/env python

# This script is to help me find something cool to spell on my macbook, it may
# or may not get published and it'll sure as hell stop getting active
# development once I achieve my (evil?) goal.
#
# nb, I say that now D:

#keys['b'] = list("qwertyuiopzxcvbnm")
#keys['w'] = list("asdfghjkl")

# TODO - Do a replacement on both the wordlist and the mappings for synonymous
# letters

def keys():
    """Returns a fresh dict with the lists"""
    b = "qwertyuiopzxcvbnm"
    w = "asdfghjklo"
    return { 'b' : list(b), 'w' : list(w) }

WORDS = None
def words():
    global WORDS
    if WORDS:
        return WORDS
    with open('wordlist.txt') as wordlist:
        WORDS = [word.replace("\n", "") for word in wordlist]
        return WORDS
    raise SystemExit, "No wordlist"






spellnums = "bwbwbbwwbbwbw"
spell1 = "wbwbwbwbwbw"
spell2 = "wbwwbbwwbwb"
spell3 = "wbwbbbwbwb"


# Algorithm:
# 1) Take a wordlist. A big one. Assume for now left alignment, potentially make a
# second pass one key over, etc.
#
# TODO: Have some kind of letter grouping, ie, 0=o. In the meantime, we can
# probably get away with putting the target letter in twice.
# * Get a new set of keys from keys()
# 2) Iterate through the word, first checking to see if the letter is in the correct place
# * If it is, pop it out of the list.
# * if we get to the end, print the word and continue

# FIXME, we use spell2 because it's easy

def test(_row):
    for word in words():
        prefix = ""
        row = _row
        while len(word) <= len(row):
            _keys = keys()
            for letter, desired in zip(word, row):
                if letter in _keys[desired]:
                    _keys[desired].pop(_keys[desired].index(letter))
                else:
                    break
            else:
                print prefix + word
                break
            row = row[1:]
            prefix += "_"
print "== numrow"
test(spellnums)
print "== Row1"
test(spell1)
print "== Row2"
test(spell2)
print "== Row3"
test(spell3)

