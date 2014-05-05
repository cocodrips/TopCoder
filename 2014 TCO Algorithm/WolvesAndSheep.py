# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect, copy

class WolvesAndSheep:
    def getmin(self, field):
        C = len(field)
        R = len(field[0])
        cnt = 0
        if self.isDivide(field, [0, R], [0, C]):
            return cnt

        fc = []
        fr = []
        for c in xrange(C):
            last = field[c][0]
            l = last
            for r in xrange(R):
                next = field[c][r]
                if r in fc:
                    continue
                if (last == 'W' and next == 'S') or (last == 'S' and next == 'W'):
                    fc.append(r)
                    last = next
                l = next

        for r in xrange(R):
            last = '.'
            for c in xrange(C):
                next = field[c][r]
                if c in fr:
                    continue
                elif last == 'W' and next == 'S':
                    fr.append(c)
                    last = next
                elif last == 'S' and next == 'W':
                    fr.append(c)
                    last = next
                elif next != '.':
                    last = next


        fc.sort()
        fr.sort()
        print fc, fr, len(fc + fr)

        for c in xrange(C):
            if c in fr:
                print '_'
            for r in xrange(R):
                if r in fc:
                    print '|',
                print field[c][r],
            print

        minus = 0
        fc.append(-1)



        return len(fc + fr)




    def isDivide(self, field, rr, cc):
        S = 0
        W = 0
        for c in field[cc[0]:cc[1]]:
            for r in c[rr[0]:rr[1]]:
                if r == 'W':
                    W += 1
                if r == 'S':
                    S += 1
        if S > 0 and W > 0:
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

def do_test(field, __expected):
    startTime = time.time()
    instance = WolvesAndSheep()
    exception = None
    try:
        __result = instance.getmin(field);
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
    sys.stdout.write("WolvesAndSheep (600 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("WolvesAndSheep.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            field = []
            for i in range(0, int(f.readline())):
                field.append(f.readline().rstrip())
            field = tuple(field)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(field, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1397923510
    PT, TT = (T / 60.0, 75.0)
    points = 600 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
