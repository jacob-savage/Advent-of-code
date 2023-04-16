'''
--- Day 5: Doesn't He Have Intern-Elves For This? ---
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?
'''

def import_file():
    return open(' 2015/day5.txt').read()

def filter_string(input_string, allowed_chars):
    filtered_chars = filter(lambda x: x in allowed_chars, input_string)
    if len(set(filtered_chars)) >= 3:
        return True
    return False

def contains_adjacent_chars(input_string):
    for i in range(len(input_string) - 1):
        if input_string[i] == input_string[i+1]:
            return True
    return False

def contains_no_forbidden_substrings(target_string):
    forbidden_substrings = ["ab", "cd", "pq", "xy"]
    for substring in forbidden_substrings:
        if substring in target_string:
            return False
    return True


test_string = 'ugknbfddeeeeeegicrmoapn'

def string_check(input_string):
    allowed_chars = 'aeiou'

    #find count of unqiue vowels
    unique_vowels = filter_string(input_string, allowed_chars)

    #find if string contains the same char two in a row
    double_char = contains_adjacent_chars(input_string)
    
    #find if target string contains any forbidden strings
    forbidden_substrings = contains_no_forbidden_substrings(input_string)

    if unique_vowels == True and double_char == True and forbidden_substrings == True:
        return True
    else:
        return False

def solution1(input_strings):
    return sum(map(string_check, input_strings))


file = import_file()

