from collections import OrderedDict, defaultdict


# def find_anagrams_v0(words: list) -> int:
#     """ bad solution"""
#     sortedlist = ["".join(sorted(w)) for w in words]
#     ret = OrderedDict()
#     for w in words:
#         tmp = "".join(sorted(w))
#         if sortedlist.count(tmp) >= 2:
#             ret[w] = 1
#     return len(ret.values())


def find_anagrams_v1(words: list) -> int:
    store = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in store:
            store[sorted_word].append(word)
        else:
            store[sorted_word] = [word]
    return len(store.values())


def find_anagrams_v2(words: list) -> int:
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
    return len(anagrams)


def find_anagrams_v3(words: list) -> int:
    """Finds all anagrams in a list of words.

    Args:
      words: A list of words.

    Returns:
      A list of all anagrams in the list of words.
    """

    # anagrams = []
    word_to_sorted_word = defaultdict(list)
    for word in words:
        sorted_word = "".join(sorted(word))
        # if sorted_word not in word_to_sorted_word:
        #     word_to_sorted_word[sorted_word] = []
        word_to_sorted_word[sorted_word].append(word)
    # for sorted_word, words in word_to_sorted_word.items():
    #     anagrams.append(words)
    return len(word_to_sorted_word.items())


def test_find_anagrams_v3(benchmark):
    # benchmark something
    result = benchmark.pedantic(find_anagrams_v3,
                                args=(("pool", "loco", "cool", "stain", "satin", "pretty", "nice", "loop"),),
                                iterations=10000, rounds=100)

    # Extra code, to verify that the run completed correctly.
    # Sometimes you may want to check the result, fast functions
    # are no good if they return incorrect results :-)
    assert result == 5


def test_find_anagrams_v1(benchmark):
    # benchmark something
    result = benchmark.pedantic(find_anagrams_v1,
                                args=(("pool", "loco", "cool", "stain", "satin", "pretty", "nice", "loop"),),
                                iterations=10000, rounds=100)

    # Extra code, to verify that the run completed correctly.
    # Sometimes you may want to check the result, fast functions
    # are no good if they return incorrect results :-)
    assert result == 5


def test_find_anagrams_v2(benchmark):
    # benchmark something
    result = benchmark.pedantic(find_anagrams_v2,
                                args=(("pool", "loco", "cool", "stain", "satin", "pretty", "nice", "loop"),),
                                iterations=10000, rounds=100)

    # Extra code, to verify that the run completed correctly.
    # Sometimes you may want to check the result, fast functions
    # are no good if they return incorrect results :-)
    assert result == 5
