import itertools, re
alpha = {'A':[0,0,0,0,1,1,1,1], 'B':[0,0,1,1,0,0,1,1], 'C':[0,1,0,1,0,1,0,1], 'a':[1,1,1,1,0,0,0,0], 'b':[1,1,0,0,1,1,0,0], 'c':[1,0,1,0,1,0,1,0]}
num = {0:[0, 0, 0, 0, 0, 0, 1], 1:[1, 0, 0, 1, 1, 1, 1], 2:[0, 0, 1, 0, 0, 1, 0], 3:[0, 0, 0, 0, 1, 1, 0], 4:[1, 0, 0, 1, 1, 0, 0], 5:[0, 1, 0, 0, 1, 0, 0], 6:[0, 1, 0, 0, 0, 0, 0], 7:[0, 0, 0, 1, 1, 0, 1], 8:[0, 0, 0, 0, 0, 0, 0], 9:[0, 0, 0, 0, 1, 0, 0]}
combinations = {}
for s in xrange(1,4):
    for i in [''.join(i) for i in itertools.combinations('ABCabc', s)]:
        a, b = [], []
        for j in i:
            a.append(alpha[j])
        for j in zip(*a):
            b.append(reduce(lambda x, y: x and y, j))
        combinations.setdefault(i, b)
result = {'a':[1],'b':[1],'c':[1],'d':[1],'e':[1],'f':[1],'g':[1]}
digit = raw_input('Enter 7 digits number: ')
while not re.match("\d\d\d\d\d\d\d", digit):
    print 'Input Error'
    digit = raw_input('Enter 7 digits number: ')
for i in xrange(7):
    n = 0
    for j in sorted(result.keys()):
        result[j].append(num[int(digit[i])][n])
        n += 1
print '[#] a=A\', b=B\', c=C\''
for i in sorted(result.keys()):
    p = []
    if result[i] == [1 for one in xrange(8)]:
        print '%s: Vcc' % i
        continue
    if result[i] == [0 for zero in xrange(8)]:
        print '%s: GND' % i
        continue
    find = False
    for j in sorted(combinations.keys()):
        if result[i] == combinations[j]:
            p.append('%s: %s' % (i, j))
            find = True
            break
    if find:
        print min(p, key=len)
        continue
    for j in sorted(combinations.keys()):
        for k in sorted(combinations.keys()):
            tmp = map(lambda x, y: x or y, combinations[j], combinations[k])
            if result[i] == tmp:
                p.append('%s: %s+%s' % (i, j, k))
                find = True
                break
    if find:
        print min(p, key=len)
        continue
    for j in sorted(combinations.keys()):
        for k in sorted(combinations.keys()):
            for l in sorted(combinations.keys()):
                tmp = map(lambda x, y, z: x or y or z, combinations[j], combinations[k], combinations[l])
                if result[i] == tmp:
                    p.append('%s: %s+%s+%s' % (i, j, k, l))
                    find = True
                    break
    if find:
        print min(p, key=len)
        continue
    for j in sorted(combinations.keys()):
        for k in sorted(combinations.keys()):
            for l in sorted(combinations.keys()):
                for m in sorted(combinations.keys()):
                    tmp = map(lambda x, y, z, n: x or y or z or n, combinations[j], combinations[k], combinations[l], combinations[m])
                    if result[i] == tmp:
                        p.append('%s: %s+%s+%s+%s' % (i, j, k, l, m))
                        find = True
                        break
    print min(p, key=len)