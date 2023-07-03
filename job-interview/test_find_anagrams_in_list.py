from collections import OrderedDict

args = ["pool", "loco", "cool", "stain", "satin", "pretty", "nice", "loop"]


def find_anagrams_v0(words: list) -> OrderedDict:
    sortedlist = ["".join(sorted(w)) for w in words]
    ret = OrderedDict()
    for w in words:
        tmp = "".join(sorted(w))
        if sortedlist.count(tmp) >= 2:
            ret[w] = 1
    return ret


def find_anagrams_v1(words: list) -> dict:
    store = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in store:
            store[sorted_word].append(word)
        else:
            store[sorted_word] = [word]
    return store


def find_anagrams_v2(words: list) -> list:
    """Finds all anagrams in a list of words.

    Args:
      words: A list of words.

    Returns:
      A list of all anagrams in the list of words.
    """

    anagrams = []
    word_to_sorted_word = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word not in word_to_sorted_word:
            word_to_sorted_word[sorted_word] = []
        word_to_sorted_word[sorted_word].append(word)
    for sorted_word, words in word_to_sorted_word.items():
        anagrams.append(words)
    return anagrams


print([item for item in find_anagrams_v1(args).values() if len(item) >= 2])
