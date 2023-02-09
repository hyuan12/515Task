def show_triangle(n):
    def triangle(n, i=0, res=[]):
        if i == n:
            return res
        res.append(" " * (n - i - 1) + "* " * (i + 1))
        return triangle(n, i + 1, res)
    return ("\n".join(triangle(n)))
