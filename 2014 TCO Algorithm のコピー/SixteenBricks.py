# -*- coding: utf-8 -*-
import math, string, itertools, fractions, heapq, collections, re, array, bisect


class SixteenBricks:
    def maximumSurface(self, height):
        heights = list(height)
        heights.sort()
        heights.reverse()

        array = [[-1] * 4 for _ in xrange(4)]

        maxi = -1
        for j in xrange(4):
            for i in xrange(4):
                if (i + j) % 2 == 0:
                    array[j][i] = heights.pop(0)


        maxi = 0
        for perm in itertools.permutations(heights):
            k = 0
            for j in xrange(4):
                for i in xrange(4):
                    if (i + j) % 2 != 0:
                        array[j][i] = perm[k]
                        k+=1
            maxi = max(maxi, self.menseki(array))

        return maxi + 16

    def menseki(self, array):
        s = 0
        for i in xrange(4):
            for j in xrange(4):
                if (i + j) % 2 == 0:
                    if 0 < i:
                        s += abs(array[i][j] - array[i - 1][j])
                    if i < 3:
                        s += abs(array[i][j] - array[i + 1][j])
                    if 0 < j:
                        s += abs(array[i][j] - array[i][j - 1])
                    if j < 3:
                        s += abs(array[i][j] - array[i][j + 1])

                if i == 0 or i == 3:
                    s += array[i][j]
                if j == 0 or j == 3:
                    s += array[i][j]
        return s



# CUT begin
# TEST CODE FOR PYTHON {{{
import sys, time, math


def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received): return False
            return all(tc_equal(e, r) for (e, r) in zip(expected, received))
        elif _t == float:
            eps = 1e-9
            d = abs(received - expected)
            return not math.isnan(received) and not math.isnan(expected) and d <= eps * max(1.0, abs(expected))
        else:
            return expected == received
    except:
        return False


def pretty_str(x):
    if type(x) == str:
        return '"%s"' % x
    elif type(x) == tuple:
        return '(%s)' % (','.join((pretty_str(y) for y in x)) )
    else:
        return str(x)


def do_test(height, __expected):
    startTime = time.time()
    instance = SixteenBricks()
    exception = None
    try:
        __result = instance.maximumSurface(height);
    except:
        import traceback

        exception = traceback.format_exc()
    elapsed = time.time() - startTime   # in sec

    if exception is not None:
        sys.stdout.write("RUNTIME ERROR: \n")
        sys.stdout.write(exception + "\n")
        return 0

    if tc_equal(__expected, __result):
        sys.stdout.write("PASSED! " + ("(%.3f seconds)" % elapsed) + "\n")
        return 1
    else:
        sys.stdout.write("FAILED! " + ("(%.3f seconds)" % elapsed) + "\n")
        sys.stdout.write("           Expected: " + pretty_str(__expected) + "\n")
        sys.stdout.write("           Received: " + pretty_str(__result) + "\n")
        return 0


def run_tests():
    sys.stdout.write("SixteenBricks (250 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("SixteenBricks.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            height = []
            for i in range(0, int(f.readline())):
                height.append(int(f.readline().rstrip()))
            height = tuple(height)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(height, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1400342437
    PT, TT = (T / 60.0, 75.0)
    points = 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T / 60), T % 60))
    sys.stdout.write("Score  : %.2f points\n" % points)


if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
