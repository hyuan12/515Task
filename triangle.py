def show_triangle(n):
    if n == 0:
        return

    triangle_rows = triangle(n)
    for row in triangle_rows:
        print(row)

def triangle(n):
    if n == 0:
        return []
    if n == 1:
        return ['*']

    previous_rows = triangle(n - 1)
    current_row = ' ' * (len(previous_rows) - 1) + '* ' * n
    return previous_rows + [current_row]
