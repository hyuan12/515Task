
def flatten(item):
    def helper(item, l):
        if isinstance(item, list):
            for s in item:
                helper(s, l)

        else:
            l.append(item)



