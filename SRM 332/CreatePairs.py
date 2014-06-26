# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class CreatePairs:
    def maximalSum(self, data):
        data = sorted(list(data), reverse=True)
        plus = [d for d in data if d > 0]
        minus = [d for d in data if d <= 0]
        minus.sort()
        print plus, minus

        largest = 0
        i = 0
        while i < len(plus):
            if i + 1 >= len(plus):
                largest += plus[i]
                i+=1
            else:
                if plus[i] * plus[i + 1] >= plus[i] + plus[i+1]:
                    largest += plus[i] * plus[i + 1]
                    i+=2
                else:
                    largest += plus[i]
                    i+=1

        i = 0
        while i < len(minus):
            if i + 1 >= len(minus):
                largest += minus[i]
                i+=1
            else:
                largest += minus[i] * minus[i + 1]
                i+=2

        return largest

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

def do_test(data, __expected):
    startTime = time.time()
    instance = CreatePairs()
    exception = None
    try:
        __result = instance.maximalSum(data);
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
    sys.stdout.write("CreatePairs (250 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("CreatePairs.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            data = []
            for i in range(0, int(f.readline())):
                data.append(int(f.readline().rstrip()))
            data = tuple(data)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(data, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1403765849
    PT, TT = (T / 60.0, 75.0)
    points = 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
