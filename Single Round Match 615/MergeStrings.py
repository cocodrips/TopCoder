# -*- coding: utf-8 -*-
import math, string, itertools, fractions, heapq, collections, re, array, bisect


class MergeStrings:
    def getmin(self, S, A, B):
        l = []
        self.nibun('', A, B, l, S)
        l.sort()
        # print l
        if not l:
            return ''
        return l[0]

    def nibun(self, str, A, B, l, S):
        if not A and not B:
            l.append(str)
            l.sort()
            return

        if l and str + 'A' * (len(S) - len(str)) > l[0]:
            return

        next = S[len(str)]

        if next != '?':
            if A and A[0] == next:
                self.nibun(str + A[0], A[1:], B, l, S)
            if B and B[0] == next:
                self.nibun(str + B[0], A, B[1:], l, S)

        elif A and B:
            if A[0] < B[0]:
                self.nibun(str + A[0], A[1:], B, l, S)
            elif  A[0] == B[0]:
                self.nibun(str + A[0], A[1:], B, l, S)
                self.nibun(str + B[0], A, B[1:], l, S)
            else:
                self.nibun(str + B[0], A, B[1:], l, S)
        else:
            if A:
                self.nibun(str + A[0], A[1:], B, l, S)
            else:
                self.nibun(str + B[0], A, B[1:], l, S)

        return


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


def do_test(S, A, B, __expected):
    startTime = time.time()
    instance = MergeStrings()
    exception = None
    try:
        __result = instance.getmin(S, A, B);
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
    sys.stdout.write("MergeStrings (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("MergeStrings.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            S = f.readline().rstrip()
            A = f.readline().rstrip()
            B = f.readline().rstrip()
            f.readline()
            __answer = f.readline().rstrip()

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(S, A, B, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1396610791
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T / 60), T % 60))
    sys.stdout.write("Score  : %.2f points\n" % points)


if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
