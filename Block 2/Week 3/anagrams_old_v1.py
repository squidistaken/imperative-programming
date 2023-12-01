word = str(input()).lower()


# TODO: Optimise
def find_palindromes(built_word: str, reference: str, anagrams: list) -> bool:
    # Checking for palindromes
    if reference == "":
        # Avoid duplicates
        # TODO: Account for duplicates
        if built_word == "":
            return True
        if built_word[0] == built_word[-1]:
            return find_palindromes(built_word[1:-1], reference, anagrams)
        return False
    # Building anagrams
    for c in reference:
        new_word = built_word + c
        index = reference.index(c)
        new_remaining = reference[0:index] + reference[index + 1::]
        palindrome_status = find_palindromes(new_word, new_remaining, anagrams)
        if palindrome_status:
            return True


print("YES") if find_palindromes("", word, []) else print("NO")