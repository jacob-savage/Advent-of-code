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
    return open('day5.txt').readlines()

def filter_string(input_string, allowed_chars):
    filtered_chars = filter(lambda x: x in allowed_chars, input_string)
    if len(list(filtered_chars)) >= 3:
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

# print(solution1(file))

'''
--- Part Two ---
Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
'''

import re

def check_line(line):
    nice = 0
    for index,_ in enumerate(line):
        if index == len(line) -2:
            break

        substring = line[index:index+2]
        mod_line = line[:index] + line[index+2:]

        print(substring, mod_line)

        result = re.findall(substring, mod_line)
        if result:
            nice = 1
    return nice

def solution2(file):
    nice = 0
    for line in file:
        nice += check_line(line)
    return nice


test = ['uurcxstgmygtbstg']


print(solution2(test))


