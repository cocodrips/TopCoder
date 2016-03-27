

def create(m):
    array = []
    for n in xrange(3, m + 1):
        for i in xrange(1 << n):
            str = ''
            for j in xrange(n):
                if i >> j & 1:
                    str += 'A'
                else:
                    str += 'B'
            array.append(str)
    return array

def is_create(initial, target):
    comb = create(5)




