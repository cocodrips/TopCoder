s = set()
stones = [1, 1000000000]
stones.sort()
for t in xrange(1000000):
    if tuple(stones) in s:
        print t, "times"
        break
    s.add(tuple(stones))

    tmp = stones[0]
    stones[0] += tmp
    stones[1] -= tmp
    stones.sort()
    print stones
print
