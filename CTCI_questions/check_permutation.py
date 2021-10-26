"""
Check Permutation: Given two strings,write a method to decide if one is a permutation of the
other.

A Permutation of a string is another string that contains same characters, only the order of characters can be different. For example, “abcd” and “dabc” are Permutation of each other.

"""
# Approach-1


# def check_permutation(first_string, second_string):
#     first_str_len = len(first_string)
#     second_str_len = len(second_string)
#
#     if first_str_len != second_str_len:
#         return False
#
#     sorted_one = sorted(first_string)
#     first_string = " ".join(sorted_one)
#     sorted_two = sorted(second_string)
#     second_string = " ".join(sorted_two)
#
#     for char in range(first_str_len):
#         if first_string[char] != second_string[char]:
#             return False
#     return True
#
# first_string = "test"
# second_string = "ttte"
# print(check_permutation(first_string, second_string))


# Approach - 2
def check_permutation(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    return "".join(sorted(first_string)) == "".join(sorted(second_string))

first_string = "test"
second_string = "ttte"
print(check_permutation(first_string, second_string))

# sorted: Python uses timsort function which runs in O(n) in best case and O(n log n) in average/worst case.
# join: string are immutable in Python, the entire strings need to be copied. The complexity O(n) where n is the size of the output string

#Approach - 3

def permutation2(str1, str2):
    if len(str1) != len(str2):
        return False
    buffer = [0] * 128
    for c in str1:
        offset = ord(c)
        buffer[offset] += 1
    for c in str2:
        offset = ord(c)
        buffer[offset] -= 1
    for i in buffer:
        if i != 0:
            return False
    return True

# Performance complexity is O(n)
