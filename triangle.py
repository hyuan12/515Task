def triangle(n):
    if n == 0:
        return []
    prev_triangle = triangle(n - 1)
    spaces = ' ' * (n - 1)
    asterisks = '* ' * n
    return prev_triangle + [spaces + asterisks]

def show_triangle(n):
    print('\n'.join(triangle(n)))
