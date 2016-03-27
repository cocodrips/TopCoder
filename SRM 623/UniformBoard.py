# -*- coding: utf-8 -*-
import math, string, itertools, fractions, heapq, collections, re, array, bisect

# .が１つもないのはk = 0と扱うと良い
class UniformBoard:
    def getBoard(self, board, K):
        N = len(board)
        dots, apples, pears = self.count(board)
        # print dots, apples, pears
        if dots == 0:
            K = 0

        table = [[0 for _ in xrange(N)] for _ in xrange(N)]

        for c in xrange(N):
            for r in xrange(N):
                total = 0
                if c != 0:
                    total += table[c - 1][r]
                if r != 0:
                    total += table[c][r - 1]
                if c != 0 and r != 0:
                    total -= table[c - 1][r - 1]
                table[c][r] = total + self.cost(board[c][r])

        maximum = 0
        for t in xrange(N):
            for b in xrange(t + 1):
                for r in xrange(N):
                    for l in xrange(r + 1):
                        cost = table[t][r]
                        if b != 0:
                            cost -= table[b - 1][r]
                        if l != 0:
                            cost -= table[t][l - 1]
                        if b != 0 and l != 0:
                            cost += table[b - 1][l - 1]

                        if cost <= K:
                            area = (t - b + 1) * (r - l + 1)
                            if area <= apples:
                                maximum = max(maximum, area)
        return maximum



    def cost(self, str):
        if str == "A":
            return 0
        if str == "P":
            return 2
        return 1

    def count(self, board):
        dots = 0
        apples = 0
        pears = 0
        for bo in board:
            for b in bo:
                if b == '.':
                    dots += 1
                if b == 'A':
                    apples += 1
                if b == 'P':
                    pears += 1
        return (dots, apples, pears)

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


def do_test(board, K, __expected):
    startTime = time.time()
    instance = UniformBoard()
    exception = None
    try:
        __result = instance.getBoard(board, K);
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
    sys.stdout.write("UniformBoard (300 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("UniformBoard.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            board = []
            for i in range(0, int(f.readline())):
                board.append(f.readline().rstrip())
            board = tuple(board)
            K = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(board, K, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1405689603
    PT, TT = (T / 60.0, 75.0)
    points = 300 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T / 60), T % 60))
    sys.stdout.write("Score  : %.2f points\n" % points)


if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
