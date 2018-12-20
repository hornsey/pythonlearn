a = [1, 2, 4, 2, 4, 5, 7, 10, 5, 5, 7, 8, 9, 0, 13]
print('a=', a)
a.sort()
print('a=', a)

last = a[-1]
x = range(len(a) - 2, -1, -1)
print('x=', list(x))
for i in x:
    if last == a[i]:
        del a[i]
    else:
        last = a[i]
print('a=', a)
