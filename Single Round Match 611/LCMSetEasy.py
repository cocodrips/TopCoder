# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class LCMSetEasy:
    def include(self, S, x):
        table = self.prime_decomposition(x)
        table_cnt = collections.Counter()
        for t in table:
            table_cnt[t] += 1

        used_cnt = collections.Counter()
        for s in S:
            s_cnt = collections.Counter()
            s_table = self.prime_decomposition(s)
            for t in s_table:
                s_cnt[t] += 1
            for k in set(table + s_table):
                if s_cnt[k] > table_cnt[k]:
                    break
            else:
                for k, v in s_cnt.items():
                    used_cnt[k] = max(v, used_cnt[k])

        for k, v in table_cnt.items():
            if used_cnt[k] != v:
                return "Impossible"

        return "Possible"


    def prime_decomposition(self, n):
        i = 2
        table = []
        while i * i <= n:
            while n % i == 0:
                n /= i
                table.append(i)
            i += 1
        if n > 1:
            table.append(n)
        return table

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

def do_test(S, x, __expected):
    startTime = time.time()
    instance = LCMSetEasy()
    exception = None
    try:
        __result = instance.include(S, x);
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
    sys.stdout.write("LCMSetEasy (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("LCMSetEasy.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            S = []
            for i in range(0, int(f.readline())):
                S.append(int(f.readline().rstrip()))
            S = tuple(S)
            x = int(f.readline().rstrip())
            f.readline()
            __answer = f.readline().rstrip()

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(S, x, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1393935802
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
