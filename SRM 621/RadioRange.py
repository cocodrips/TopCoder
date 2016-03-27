# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class RadioRange:
    def RadiusProbability(self, X, Y, R, Z):
        bad_points = []
        for x, y, r in zip(X, Y, R):
            l = math.sqrt(x * x + y * y)

            small = l - r
            big = l + r

            if (small < 0 and big < 0) or (small >= 0 and big >=0):
                bad_points.append((min(abs(small), abs(big)), 1))
                bad_points.append((max(abs(small), abs(big)), -1))
            else:
                bad_points.append((0, 1))
                bad_points.append((max(abs(small), abs(big)), -1))


        bad_points.append((0, 0))
        bad_points.sort()

        bad_length = 0
        bad_num = 0
        i = 1
        while i < len(bad_points):
            if bad_points[i][0] > Z:
                break
            if bad_num == 0:
                bad_length += bad_points[i][0] - bad_points[i - 1][0]
            bad_num += bad_points[i][1]
            i += 1

        if bad_num == 0:
            bad_length += Z - bad_points[i - 1][0]

        return bad_length / Z

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

def do_test(X, Y, R, Z, __expected):
    startTime = time.time()
    instance = RadioRange()
    exception = None
    try:
        __result = instance.RadiusProbability(X, Y, R, Z);
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
    sys.stdout.write("RadioRange (275 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("RadioRange.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            X = []
            for i in range(0, int(f.readline())):
                X.append(int(f.readline().rstrip()))
            X = tuple(X)
            Y = []
            for i in range(0, int(f.readline())):
                Y.append(int(f.readline().rstrip()))
            Y = tuple(Y)
            R = []
            for i in range(0, int(f.readline())):
                R.append(int(f.readline().rstrip()))
            R = tuple(R)
            Z = int(f.readline().rstrip())
            f.readline()
            __answer = float(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(X, Y, R, Z, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1405927923
    PT, TT = (T / 60.0, 75.0)
    points = 275 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
