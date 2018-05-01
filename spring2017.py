
def gp():
    yu = 0
    def p():
        def c():
            nonlocal yu
            yu = "hhh"
            return y
        return c
    print(yu)
    return p

