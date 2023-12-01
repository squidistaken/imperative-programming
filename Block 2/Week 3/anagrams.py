"""
File: anagrams.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This program checks to see if an anagram of a word can be considered a palindrome.
"""
word = [_ for _ in input().lower()]


def compare_letters(_word: list[str]) -> bool:
    # If there is less than one or one character left in the word, this is a palindrome
    if len(_word) <= 1:
        return True
    # Check if the first character is in remaining word.
    if _word[0] in _word[1:]:
        x = _word[1:]
        # We remove all mentions of _word[0] in the "new word"
        x.remove(_word[0])
        return compare_letters(x)
    else:
        compare_letters(_word[1:])
    # Word is not a palindrome
    return False


print("YES" if compare_letters(word) else "NO")
