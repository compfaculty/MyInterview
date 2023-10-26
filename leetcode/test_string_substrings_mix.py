def length_of_longest_substring(s: str) -> int:
    data = set()
    max_ = head = tail = 0
    l_ = len(s)
    while head < l_ and tail < l_:
        if not s[tail] in data:
            data.add(s[tail])
            tail += 1
        else:
            max_ = max(max_, tail - head)
            data.discard(s[head])
            head += 1
    return max_ or (tail - head)


def test_length_of_longest_substring():
    assert length_of_longest_substring("aab") == 1
