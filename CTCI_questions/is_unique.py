" Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?"



def is_unique(string):
    unique_chars = set()
    for c in string:
        if c in unique_chars:
            return False
        unique_chars.add(c)
    return True

string = "Akhtar"
print(is_unique(string))

## Runtime O(n)
