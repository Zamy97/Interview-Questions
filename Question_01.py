"""Given a list of numbers and a number k, return whether any two numbers from the list add up to k.


   For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

# Stackoverflow responses
    # https://stackoverflow.com/questions/51300360/given-a-list-of-numbers-and-a-number-k-return-whether-any-two-numbers-from-the
    #https://stackoverflow.com/questions/52042370/find-two-numbers-from-a-list-that-add-up-to-a-specific-number
number_list = [10,15,3,7]
target_number = 17
def find_number(number_list, target_number):
    for i, number in enumerate(number_list[:-1]):
        complementary_number = target_number - number
        if complementary_number in number_list[i:]:
            print("Solutions Found: {} and {}".format(number, complementary_number))
            return True
            break=
        else:
            print("No solution exist")
            return False
find_number(number_list, target_number)
