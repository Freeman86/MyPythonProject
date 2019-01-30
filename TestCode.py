



L = [8, -8, 6.6, 'qwerty', 0.5]

c = 0
for i in L:
    if type(i) == int or type(i) == float:
        c += i

print(c)