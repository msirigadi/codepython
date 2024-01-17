"""
This article gives us the methods to find the frequency of minimum occurring character
in a python string. This is quite important utility nowadays and knowledge of it is always
useful. Let’s discuss certain ways in which this task can be performed.
"""

#Solution1
def min_character_freq(str):
    freq = {}

    for ch in str:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    return min(freq, key = freq.get)

if __name__ == "__main__":
    str = "geeksforgeeks"
    print(min_character_freq(str))