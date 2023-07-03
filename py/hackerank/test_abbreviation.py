# https://www.hackerrank.com/challenges/abbr/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming

def abbreviation(a: str, b: str):
    bpos = {}
    for i in range(len(b)):
        bpos[b[i]] = (bpos[b[i]] | {i}) if b[i] in bpos else {i}
    possibilities = {0}
    for i in range(len(a)):
        if a[i] in bpos:
            intersection = bpos[a[i].upper()] & possibilities
            advancement = set([i + 1 for i in intersection])
        else:
            advancement = set([])
        if a[i].upper() == a[i]:  # capitals must follow the intersection
            possibilities = advancement
        else:
            possibilities = possibilities | advancement
    return "YES" if (len(b)) in possibilities else "NO"


def abbreviation2(a: str, b: str):
    a = a.upper()
    ok = False
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            ok = True
            i += 1
            j += 1
        else:
            ok = False
            i += 1

    return "YES" if ok else "NO"


def test_abbreviation():
    assert abbreviation2("AbcDE", "ABDEB") == "YES"
    assert abbreviation2("AbcDE", "AFDE") == "NO"
    assert abbreviation2("AbCdE", "AFE") == "NO"
    assert abbreviation2("beFgH", "EFG") == "NO"
    assert abbreviation2("beFgH", "EFH") == "YES"
