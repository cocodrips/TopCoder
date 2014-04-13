# -*- coding: utf-8 -*-
import math, string, itertools, fractions, heapq, collections, re, array, bisect


class TwoLLogo:
    def countWays(self, grid):

        W = len(grid[0])
        H = len(grid)

        cnt = 0
        L = [[[] for _ in xrange(W)] for _ in xrange(H)]
        for c1 in xrange(1, H):
            for r1 in xrange(W - 1):

                if grid[c1][r1] == '#' or grid[c1 - 1][r1] == '#' or grid[c1][r1 + 1] == '#':
                    continue
                dot_list = [(c1, r1), (c1 - 1, r1), (c1, r1 + 1)]
                sq = [dot_list]
                isC = True
                isR = True
                i = 2
                while isC or isR:

                    print i
                    add = []
                    if isC and c1 - i > 0:
                        if grid[c1 - i][r1] == ".":
                            sq.append(dot_list + [(c1 + 1, r1)])
                            add.append((c1 + 1, r1))
                    else:
                        isC = False
                    if isR and r1 + i < W:
                        if grid[c1][r1 + 1] == ".":
                            sq.append(dot_list + [(c1 + 1, r1)])
                            add.append((c1 + 1, r1))
                    else:
                        isR = False
                    dot_list.append(add)
                    i += 1

                L[c1][r1] = sq


        print L


        return cnt

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


def do_test(grid, __expected):
    startTime = time.time()
    instance = TwoLLogo()
    exception = None
    try:
        __result = instance.countWays(grid);
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
    sys.stdout.write("TwoLLogo (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("TwoLLogo.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            grid = []
            for i in range(0, int(f.readline())):
                grid.append(f.readline().rstrip())
            grid = tuple(grid)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(grid, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1397144065
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T / 60), T % 60))
    sys.stdout.write("Score  : %.2f points\n" % points)


if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
