import re

import re

def pequod(f):
    with open(f) as file:
        contents = file.read()
    count = len(re.findall(r"(?i)\bwhite\s+whale(?:'s)?\b", contents))
    return count


def find_dotcoms(s):
    pattern = r'\b([a-zA-Z0-9]+\.)+([a-zA-Z0-9]+)\.com\b'

    # search for all matches in the input string
    matches = re.findall(pattern, s)

    # extract just the second capture group (i.e., the domain name without the ".com" suffix)
    domains = [match[1] for match in matches]

    # return the list of matches
    return domains


def palindrome_re(n):
    if n == 1:
        return r'.'
    elif n == 2:
        return r'(.)\1'
    else:
        inner_re = palindrome_re(n - 2)
        return r'(.).{%d}\1%s\1.' % (n - 2, inner_re)



def palindrome_direct(s):
    return s == s[::-1]


# s = "pets.com google.com foo.org www.yahoo.com"
# print(find_dotcoms(s))
# r = palindrome_re(2)
# print(bool(re.fullmatch(r, 'ab')))
