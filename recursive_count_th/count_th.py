"""
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""


def count_th(word):
    def recurse(word, count=0):
        if len(word) <= 1:
            return count
        if len(word) == 2 and word == "th":
            return count + 1
        else:
            if word[0] == "t" and word[1] == "h":
                count += 1
            return recurse(word[1:], count)

    return recurse(word)

    # How to get closer to our base case(s)?
    # 1- We always check the first two characters and if they're equal to "th"
    # we increment count and call count_th() by removing the first checked characters

    # TBC

