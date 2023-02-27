
Hai Yuan hyuan12@stevens.edu

# bugs and issues

The regular expression pattern doesn't match all valid domain names that end with ".com" due to an incorrect pattern. For example, if the pattern only matches domain names that contain letters in lowercase, it would miss any domain names that contain uppercase letters.

# resolved issue 

To resolve this issue, one could modify the regular expression pattern to include uppercase letters as well. One way to do this is to use the re.IGNORECASE flag when calling the re.findall() function. This flag enables case-insensitive matching, which allows the pattern to match domain names regardless of whether they contain uppercase or lowercase letters.
