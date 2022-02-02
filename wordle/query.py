from copy import deepcopy
from typing import List, Dict

from wordle.words import WORDS, WORDS_REPEAT
from wordle.statistics import CHAR_FREQUENCIES

CHARS = set(CHAR_FREQUENCIES.keys())


def query(characters: List = [CHARS, CHARS, CHARS, CHARS, CHARS], contains: set = set()):
    possible = []
    ranks = []

    def check(w) -> bool:
        for k, ch in enumerate(w):
            if ch not in characters[k]:
                return False
        return True

    def check_contains(w) -> bool:
        for c in contains:
            if c not in w:
                return False
        return True

    for word in WORDS + WORDS_REPEAT:
        if not check(word) or not check_contains(word):
            continue

        possible.append(word)
        ranks.append(word_rank(word))

    words_ranks = dict(zip(possible, ranks))
    return sorted(words_ranks.items(), key=lambda kv: kv[1])


def word_rank(word):
    frequencies = [i for i in CHAR_FREQUENCIES]
    n = len(CHAR_FREQUENCIES) or 1
    used = set()
    rank = 0

    for ch in word:
        rank += (frequencies.index(ch) + 1) / n
        if ch in used:
            rank += 1
        used.add(ch)

    return rank
