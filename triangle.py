def show_triangle(n):
    def triangle(n, i=0, res=[]):
        if i == n:
            return res
        s = (" " * (n - i - 1) + "* " * (i + 1)).rstrip()
        res.append(s)
        return triangle(n, i + 1, res)
    #print("\n".join(triangle(n)))
    return "\n".join(triangle(n))
