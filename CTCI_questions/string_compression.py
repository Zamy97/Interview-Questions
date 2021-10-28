"""
String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z)
"""

def string_compression(given_string):
    compressed_string = ""
    count = 1
    for i in range(len(given_string) - 1):
        if given_string[i] == given_string[i+1]:
            count += 1
        else:
            compressed_string += given_string[i] + str(count)
            count = 1
    compressed_string += given_string[i] + str(count)

    if len(compressed_string) >= len(given_string):
        return given_string
    else:
        return compressed_string
