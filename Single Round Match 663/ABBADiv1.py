# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class ABBADiv1:
    def canObtain(self, initial, target):
        iA = initial.count("A")
        iB = len(initial) - iA

        tA = target.count("A")
        tB = len(target) - tA
        # print tA - iA, tB - iB

        if (tB - iB) == 0:
            if (initial == target[:len(initial)]):
                return "Possible"
            return "Impossible"

        is_match = []
        add_b = (tB - iB)
        for i in xrange(len(target) - len(initial) + 1):
            if add_b % 2 == 0 and initial == target[i:i+len(initial)]:
                is_match.append(i)
            elif add_b % 2 == 1 and initial[::-1] == target[i:i+len(initial)]:
                is_match.append(i)

        for j in is_match:
            if target[:j].count('B') == add_b - (add_b / 2) and target[0] == 'B':
                return "Possible"

        return "Impossible"

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

def do_test(initial, target, __expected):
    startTime = time.time()
    instance = ABBADiv1()
    exception = None
    try:
        __result = instance.canObtain(initial, target);
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
    sys.stdout.write("ABBADiv1 (300 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("ABBADiv1.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            initial = f.readline().rstrip()
            target = f.readline().rstrip()
            f.readline()
            __answer = f.readline().rstrip()

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(initial, target, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1437663637
    PT, TT = (T / 60.0, 75.0)
    points = 300 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
