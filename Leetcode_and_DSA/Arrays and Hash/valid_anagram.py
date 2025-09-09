"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

"""


def isAnagram_by2Dict(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    s_hashmap = {}

    t_hashmap = {}

    for i in range(0, len(s)):

        s_char = s[i]
        t_char = t[i]

        s_hashmap[s_char] = s_hashmap.get(s_char, 0) + 1

        t_hashmap[t_char] = t_hashmap.get(t_char, 0) + 1

    return s_hashmap == t_hashmap


def isAnagram_bySort(s: str, t: str) -> bool:

    return sorted(s) == sorted(t)


def isAnagram_byAlphabet(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    s = s.lower()
    t = t.lower()

    freq_list = [0] * 26
    offset = ord('a')

    for i in range(0, len(s)):

        index_s = ord(s[i]) - offset
        index_t = ord(t[i]) - offset

        freq_list[index_s] += 1
        freq_list[index_t] -= 1

    for i in range(26):

        if freq_list[i] != 0:
            return False

    return True


if __name__ == "__main__":
    print(isAnagram_by2Dict(s="anagram", t="nagaram"))

    print(isAnagram_bySort(s="rat", t="car"))

    print(isAnagram_bySort(s="a gentleman", t="elegant man"))

    print(isAnagram_byAlphabet(s="agentleman", t="elegantman"))

    print(isAnagram_byAlphabet(s="rat", t="car"))
