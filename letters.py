t = 'abcdefghijklmnopqrstuvwxyz'

def ordinal(letter):
    index = t.index(letter) + 1
    if index in [11, 12, 13]:
        return f"{index}th"
    if index % 10 == 1:
        return f"{index}st"
    if index % 10 == 2:
        return f"{index}nd"
    if index % 10 == 3:
        return f"{index}rd"
    return f"{index}th"


try:
    while True:
        s = input('Enter a letter: ')
        if s in ('stop', '^C', '^D'):
            print('Goodbye.')
            break
        if len(s) != 1 or not s.isalpha():
            print('Please enter a single letter.')
            continue
        s = s.lower()
        print(f"'{s}' is the {ordinal(s)} letter of the alphabet.")

except KeyboardInterrupt as e:
    print(e)
except EOFError:
    print("Goodbye.")


