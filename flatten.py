
def flatten(lst):
    flatten_list = []
    for i in lst:
        if isinstance(i, list):
            flatten_list.extend(flatten(i))
        else:
            flatten_list.append(i)
    return flatten_list




