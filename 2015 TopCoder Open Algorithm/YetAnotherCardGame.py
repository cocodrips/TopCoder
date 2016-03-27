# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class YetAnotherCardGame:
    def maxCards(self, petr, snuke):
        petr = list(petr)
        snuke = list(snuke)
        petr.sort()
        snuke.sort()

        turn = min(len(petr) * 2, len(snuke) * 2)
        #[turn][max] = length
        dp = [[0 for _ in xrange(101)] for _ in xrange(turn + 1)]
        for i in xrange(1, turn + 1):
            for j in xrange(101):

                if i & 1:
                    for p in petr:
                        if p > j: # おける
                            dp[i][p] = max(dp[i - 1][j] + 1, dp[i][p])
                        dp[i][j] = max(dp[i - 1][j], dp[i][j])
                else:
                    for s in snuke:
                        if s > j: # おける
                            dp[i][s] = max(dp[i - 1][j] + 1, dp[i][s])
                        dp[i][j] = max(dp[i - 1][j], dp[i][j])

        ans = 0
        for i in xrange(101):
            ans = max(ans, dp[turn][i])

        return ans








        # p_used = 0
        # s_used = 0
        # p, s = 0, 0
        # tops = []

        # while p_used < len(petr) and s_used < len(snuke):
        #     if not tops:
        #         tops.append(petr[p])
        #         p += 1
        #     else:
        #         for i in xrange(p, len(petr)):
        #             if petr[i] > tops[-1]:
        #                 # print "p:", petr[i]
        #                 # print s < len(snuke) and petr[i] <= snuke[s], s_used < len(snuke), "||", s_used + 1 >= len(snuke)
        #
        #                 if (s < len(snuke) and petr[i] <= snuke[s] and s_used < len(snuke)) or s >= len(snuke):
        #                     tops.append(petr[i])
        #                     p = i + 1
        #                 else:
        #                     p = i
        #                 break
        #     p_used += 1
        #     print tops
        #
        #     for i in xrange(s, len(snuke)):
        #         if snuke[i] > tops[-1]:
        #             # print "s:", snuke[i]
        #             # print p < len(petr), snuke[i] <= petr[p], p_used < len(petr), "||", p_used >= len(petr)
        #             if (p < len(petr) and snuke[i] <= petr[p] and p_used < len(petr)) or p >= len(petr):
        #                 tops.append(snuke[i])
        #                 s = i + 1
        #             else:
        #                 s = i
        #             break
        #     s_used += 1
        #     print tops
        # return len(tops)





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

def do_test(petr, snuke, __expected):
    startTime = time.time()
    instance = YetAnotherCardGame()
    exception = None
    try:
        __result = instance.maxCards(petr, snuke);
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
    sys.stdout.write("YetAnotherCardGame (250 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("YetAnotherCardGame.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            petr = []
            for i in range(0, int(f.readline())):
                petr.append(int(f.readline().rstrip()))
            petr = tuple(petr)
            snuke = []
            for i in range(0, int(f.readline())):
                snuke.append(int(f.readline().rstrip()))
            snuke = tuple(snuke)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(petr, snuke, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1437199209
    PT, TT = (T / 60.0, 75.0)
    points = 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
