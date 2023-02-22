import re

import re

def pequod(f):
    with open(f) as file:
        contents = file.read()
    count = len(re.findall(r"(?i)\bwhite\s+whale(?:'s)?\b", contents))
    return count



def find_dotcoms(s):
    # Match domain names that end with ".com"
    pattern = r"\b([a-zA-Z0-9-]+)\.com\b"
    # Find all non-overlapping matches of the pattern in the string
    matches = re.findall(pattern, s)
    # Return the list of matched domain names without the ".com" suffix
    return matches


def palindrome_re(n):
    # generate a regular expression that matches palindromes of length n
    mid = (n // 2) + 1
    return r'^(?:(.)(?:(?!\1)(.)){%d}\1|(.){%d})$' % ((mid-1)*2, n)

def palindrome_direct(s):
    return s == s[::-1]

