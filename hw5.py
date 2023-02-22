import re

import re

def pequod(f):
    with open(f) as file:
        contents = file.read()
    count = len(re.findall(r"(?i)\bwhite\s+whale(?:'s)?\b", contents))
    return count




def find_dotcoms(s):
    # define the regular expression pattern to match domain names that end in ".com"
    pattern = r'\b([a-zA-Z0-9\-]+\.[a-zA-Z0-9\-]+\.)?([a-zA-Z0-9\-]+)\.com\b'

    # search for all matches in the input string
    matches = re.findall(pattern, s)

    # extract just the second capture group (i.e., the domain name without the ".com" suffix)
    domains = [match[1] for match in matches]

    # return the list of matches
    return domains



def palindrome_re(n):
    # generate a regular expression that matches palindromes of length n
    mid = (n // 2) + 1
    return r'^(?:(.)(?:(?!\1)(.)){%d}\1|(.){%d})$' % ((mid-1)*2, n)

def palindrome_direct(s):
    return s == s[::-1]

#print(find_dotcoms("eff.org a.b.c.com www19.site.com bad.com.eu 1-2.3-4.com"))
