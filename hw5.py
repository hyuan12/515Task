import re

def pequod(f):
    with open(f) as file:
        contents = file.read()
    count = len(re.findall(r"(?i)\bwhite\s+whale(?:'s)?\b", contents))
    return count



def find_dotcoms(s):
    # Match domain names that end in ".com" and only contain Latin characters, numbers, and dashes
    pattern = r"\b([a-zA-Z0-9-]+\.[cC][oO][mM])\b"
    matches = re.findall(pattern, s)

    # Remove ".com" suffix from domain names and return them
    return [match[:-4] for match in matches]






def palindrome_re(n):
    # generate a regular expression that matches palindromes of length n
    mid = (n // 2) + 1
    return r'^(?:(.)(?:(?!\1)(.)){%d}\1|(.){%d})$' % ((mid-1)*2, n)

def palindrome_direct(s):
    return s == s[::-1]


# s = "eff.org a.b.c.com www19.site.com bad.com.eu 1-2.3-4.com"
s = "pets.com google.com foo.org www.yahoo.com"
print(find_dotcoms(s))
r = palindrome_re(2)
print(bool(re.fullmatch(r, 'ab')))
