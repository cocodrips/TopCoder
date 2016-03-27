B = 20
N = 10

for i in xrange(1, B):
    for j in xrange(i, B):
        print
        s = set()
        # for n in xrange(1, 10):
        stones = [i, j]
        stones.sort()
        for t in xrange(N):
            # if tuple(stones) in s:
            #     print t, "times"
            #     break
            # s.add(tuple(stones))

            tmp = stones[0]
            stones[0] += tmp
            stones[1] -= tmp
            stones.sort()
        #     print stones,
        # print
        print i, j, "->", stones[0]
