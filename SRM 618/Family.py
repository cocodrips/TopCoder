# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class Family:
    def isFamily(self, parent1, parent2):
        N = len(parent1)
        G = [[False] * N for _ in xrange(N)]
        for p1, p2 in zip(parent1, parent2):
            if p1 != -1:
                G[p1][p2] = G[p2][p1] = True

        S = [0] * N
        for i in xrange(N):
            if S[i] != 0:
                continue
            if not self.check(i, 1, G, S, N):
                return "Impossible"

        return "Possible"

    def check(self, p, s, G, S, N):
        S[p] = s
        for i in xrange(N):
            if not G[p][i]:
                continue
            if S[i] == 0 and not self.check(i, -s, G, S, N):
                return False
            elif S[i] == s:
                return False
        return True


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
        return '(%s)' % (','.join( (pretty_str(y) for y in x) ) )
    else:
        return str(x)

def do_test(parent1, parent2, __expected):
    startTime = time.time()
    instance = Family()
    exception = None
    try:
        __result = instance.isFamily(parent1, parent2);
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
    sys.stdout.write("Family (250 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("Family.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            parent1 = []
            for i in range(0, int(f.readline())):
                parent1.append(int(f.readline().rstrip()))
            parent1 = tuple(parent1)
            parent2 = []
            for i in range(0, int(f.readline())):
                parent2.append(int(f.readline().rstrip()))
            parent2 = tuple(parent2)
            f.readline()
            __answer = f.readline().rstrip()

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(parent1, parent2, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1406011677
    PT, TT = (T / 60.0, 75.0)
    points = 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
