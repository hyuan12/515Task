import re

def pequod(f):
    # read contents of the file
    with open(f) as file:
        contents = file.read()

    # search for the phrase "white whale" ignoring spaces and capitalization
    count = len(re.findall(r'white\s+whale', contents, re.IGNORECASE))

    return count


def find_dotcoms(s):
    # match domain names that end in ".com" and extract the domain name
    pattern = r'(?:https?://)?([\w-]+)\.com'
    matches = re.findall(pattern, s)

    # remove duplicate domain names and return as a list
    return list(set(matches))


def palindrome_re(n):
    # generate a regular expression that matches palindromes of length n
    mid = (n // 2) + 1
    return r'^(?:(.)(?:(?!\1)(.)){%d}\1|(.){%d})$' % ((mid-1)*2, n)

def palindrome_direct(s):
    return s == s[::-1]

