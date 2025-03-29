def qrib(n):
        a, b, c, d = 1, 1, 2, 4
        while a < n:
                print(a, end=' ')
                a, b, c, d = b, c, d, a+b+c+d  
        print()
qrib(1000000000000000000000)

# output python3 qbnci.py 1 1 2 4 8 15 29 56 108 208 401 773 1490 2872 5536 10671 20569 39648 76424 147312 283953 547337
# how may we expand this function for a variable number for range of
# preceeding sums?

# example : a, b, c, d, e, f, g, h.....
