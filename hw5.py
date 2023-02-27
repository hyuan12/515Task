import re

def pequod(f):
    with open(f) as file:
        contents = file.read()
    count = len(re.findall(r"(?i)\bwhite\s+whale(?:'s)?\b", contents))
    return count


def find_dotcoms(s):
    # Define the regular expression to match domain names ending in .com
    pattern = r'\b([a-zA-Z0-9-]+)\.com\b'
    matches = re.findall(pattern, s)
    return matches


def palindrome_re(n):
    # generate a regular expression that matches palindromes of length n
    mid = (n // 2) + 1
    return r'^(?:(.)(?:(?!\1)(.)){%d}\1|(.){%d})$' % ((mid-1)*2, n)


def palindrome_direct(s):
    return s == s[::-1]


# s = "pets.com google.com foo.org www.yahoo.com"
# print(find_dotcoms(s))
# r = palindrome_re(2)
# print(bool(re.fullmatch(r, 'ab')))
