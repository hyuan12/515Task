

def longest_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        max_len = max(map(len, lines))
        res = [line.strip() for line in lines if len(line) == max_len]
        return res