"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­ drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)

"""
def palindrome_permutation(given_string):
    given_string = given_string.lower()
    no_of_chars = 256
    count = [0] * no_of_chars
    for char in range(0, len(given_string)):
        count[ord(given_string[char])] = count[ord(given_string[char])] + 1

    odd_chars = 0
    for char in range(0, no_of_chars):
        if (count[char] and 1):
            odd_chars += 1

        if odd_chars > 1:
            return False
    return True

print(palindrome_permutation("Tact Coa"))
