from typing import List, Dict

from wordle.words import WORDS, WORDS_REPEAT


def get_character_frequencies(words: List) -> List:
    frequencies = {}

    for word in words:
        for ch in word:
            frequencies[ch] = frequencies.get(ch, 0) + 1

    return sorted(frequencies.items(), key=lambda kv: kv[1], reverse=True)


# Pre-run get_character_frequencies(WORDS + WORDS_REPEAT)
CHAR_FREQUENCIES: Dict = {
    "s": 6665,
    "e": 6662,
    "a": 5990,
    "o": 4438,
    "r": 4158,
    "i": 3759,
    "l": 3371,
    "t": 3295,
    "n": 2952,
    "u": 2511,
    "d": 2453,
    "y": 2074,
    "c": 2028,
    "p": 2019,
    "m": 1976,
    "h": 1760,
    "g": 1644,
    "b": 1627,
    "k": 1505,
    "f": 1115,
    "w": 1039,
    "v": 694,
    "z": 434,
    "j": 291,
    "x": 288,
    "q": 112,
}
