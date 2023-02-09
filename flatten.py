
def flatten(item):
    l = []
    for i in item:
        helper(i,l)
    print(l)

def helper(item, l):
    if isinstance(item, list):
        for s in item:
            helper(s, l)
    else:
        l.append(item)



