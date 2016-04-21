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
result = {'A':[1],'B':[1],'C':[1],'D':[1],'E':[1],'F':[1],'G':[1]}
digit = raw_input('Enter 7 digits number: ')
while not re.match("\d\d\d\d\d\d\d", digit):
    print 'Input Error'
    digit = raw_input('Enter 7 digits number: ')
for i in xrange(7):
    n = 0
    for j in sorted(result.keys()):
        result[j].append(num[int(digit[i])][n])
        n += 1
for i in sorted(result.keys()):
    p = []
    if result[i] == [1 for one in xrange(8)]:
        print '%s: Vcc' % i
        continue
    if result[i] == [0 for zero in xrange(8)]:
        print '%s: GND' % i
        continue
    find = False
    for j in xrange(41):
        if result[i] == combinations[combinations.keys()[j]]:
            p.append('%s: %s' % (i, combinations.keys()[j]))
            find = True
            break
    if find:
        p = [i.replace('a', 'A\'').replace('b', 'B\'').replace('c', 'C\'') for i in p]
        print min(p, key=len)
        continue
    for j in xrange(41):
        for k in xrange(41):
            tmp = map(lambda x, y: x or y, combinations[combinations.keys()[j]], combinations[combinations.keys()[k]])
            if result[i] == tmp:
                p.append('%s: %s+%s' % (i, combinations.keys()[j], combinations.keys()[k]))
                find = True
                break
    if find:
        p = [i.replace('a', 'A\'').replace('b', 'B\'').replace('c', 'C\'') for i in p]
        print min(p, key=len)
        continue
    for j in xrange(41):
        for k in xrange(41):
            for l in xrange(41):
                tmp = map(lambda x, y, z: x or y or z, combinations[combinations.keys()[j]], combinations[combinations.keys()[k]], combinations[combinations.keys()[l]])
                if result[i] == tmp:
                    p.append('%s: %s+%s+%s' % (i, combinations.keys()[j], combinations.keys()[k], combinations.keys()[l]))
                    find = True
                    break
    if find:
        p = [i.replace('a', 'A\'').replace('b', 'B\'').replace('c', 'C\'') for i in p]
        print min(p, key=len)
        continue
    for j in xrange(41):
        for k in xrange(41):
            for l in xrange(41):
                for m in xrange(41):
                    tmp = map(lambda x, y, z, n: x or y or z or n, combinations[combinations.keys()[j]], combinations[combinations.keys()[k]], combinations[combinations.keys()[l]], combinations[combinations.keys()[m]])
                    if result[i] == tmp:
                        p.append('%s: %s+%s+%s+%s' % (i, combinations.keys()[j], combinations.keys()[k], combinations.keys()[l], combinations.keys()[m]))
                        find = True
                        break
    p = [i.replace('a', 'A\'').replace('b', 'B\'').replace('c', 'C\'') for i in p]
    print min(p, key=len)