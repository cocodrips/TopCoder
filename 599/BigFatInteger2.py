import collections
import math

class BigFatInteger2:
  def isDivisible(self, A, B, C, D):
    if C == 1:
      return "divisible"

    As = self._prime_decomposition(A)
    Cs = self._prime_decomposition(C)

    print As, Cs
    for c in set(Cs):
      if c not in As:
        return "not divisible"

    Acount = collections.Counter(As)
    Ccount = collections.Counter(Cs)

    for a_key, a_value in Acount.items():
      if a_value * B < Ccount[a_key] * D:
        return "not divisible"

    return "divisible"

  def _prime_decomposition(self, n):
    array = []
    primes = self.primetable(int(math.ceil(math.sqrt(n))))
    for p in primes:
      while n % p == 0:
        n /= p
        array.append(p)
      if n == 1:
        break
    else:
      array.append(n)

    return array

  def primetable(self, max):
    sq = math.sqrt(max)
    table = []

    t = range(0, max+1)
    t[0] = 0
    t[1] = 0
    p = 2
    while p <= sq:
      if t[p] != 0:
        j = p + p
        while j <= max:
          t[j] = 0
          j += p
      p += 1
    for p in t:
      if p != 0:
        table.append(p)
    return table



# BEGIN KAWIGIEDIT TESTING
# Generated by KawigiEdit-pfx 2.1.9
import sys
import time
def KawigiEdit_RunTest(testNum, p0, p1, p2, p3, hasAnswer, p4):
	sys.stdout.write(str("Test ") + str(testNum) + str(": [") + str(p0) + str(",") + str(p1) + str(",") + str(p2) + str(",") + str(p3))
	print(str("]"))
	obj = BigFatInteger2()
	startTime = time.clock()
	answer = obj.isDivisible(p0, p1, p2, p3)
	endTime = time.clock()
	res = True
	print(str("Time: ") + str((endTime - startTime)) + str(" seconds"))
	if (hasAnswer):
		print(str("Desired answer:"))
		print(str("\t") + str("\"") + str(p4) + str("\""))
	
	print(str("Your answer:"))
	print(str("\t") + str("\"") + str(answer) + str("\""))
	if (hasAnswer):
		res = answer == p4
	
	if (not res):
		print(str("DOESN'T MATCH!!!!"))
	elif ((endTime - startTime) >= 2):
		print(str("FAIL the timeout"))
		res = False
	elif (hasAnswer):
		print(str("Match :-)"))
	else:
		print(str("OK, but is it right?"))
	
	print(str(""))
	return res

all_right = True


# ----- test 0 -----
p0 = 6
p1 = 1
p2 = 2
p3 = 1
p4 = "divisible"
all_right = KawigiEdit_RunTest(0, p0, p1, p2, p3, True, p4) and all_right
# ------------------

# ----- test 1 -----
p0 = 2
p1 = 1
p2 = 6
p3 = 1
p4 = "not divisible"
all_right = KawigiEdit_RunTest(1, p0, p1, p2, p3, True, p4) and all_right
# ------------------

# ----- test 2 -----
p0 = 1000000000
p1 = 1000000000
p2 = 1000000000
p3 = 200000000
p4 = "divisible"
all_right = KawigiEdit_RunTest(2, p0, p1, p2, p3, True, p4) and all_right
# ------------------

# ----- test 3 -----
p0 = 8
p1 = 100
p2 = 4
p3 = 200
p4 = "not divisible"
all_right = KawigiEdit_RunTest(3, p0, p1, p2, p3, True, p4) and all_right
# ------------------

# ----- test 4 -----
p0 = 999999937
p1 = 1000000000
p2 = 999999929
p3 = 1
p4 = "not divisible"
all_right = KawigiEdit_RunTest(4, p0, p1, p2, p3, True, p4) and all_right
# ------------------

# ----- test 5 -----
p0 = 2
p1 = 2
p2 = 4
p3 = 1
p4 = "divisible"
all_right = KawigiEdit_RunTest(5, p0, p1, p2, p3, True, p4) and all_right
# ------------------

if (all_right):
	print(str("You're a stud (at least on the example cases)!"))
else:
	print(str("Some of the test cases had errors."))

# PROBLEM STATEMENT
# This problem statement contains superscipts that may not display properly outside the applet.
# 
# You are given four integers A, B, C and D. Return "divisible" (quotes for clarity) if AB is divisible by CD. Return "not divisible" otherwise.
# 
# DEFINITION
# Class:BigFatInteger2
# Method:isDivisible
# Parameters:integer, integer, integer, integer
# Returns:string
# Method signature:def isDivisible(self, A, B, C, D):
# 
# 
# NOTES
# -The return value is case-sensitive.
# -Positive integer y divides a positive integer x if and only if there is a positive integer z such that y*z=x. In particular, for each positive integer x, both 1 and x divide x.
# 
# 
# CONSTRAINTS
# -A, B, C and D will each be between 1 and 1,000,000,000 (109), inclusive.
# 
# 
# EXAMPLES
# 
# 0)
# 6
# 1
# 2
# 1
# 
# Returns: "divisible"
# 
# Here, AB = 61 = 6 and CD = 21 = 2. 6 is divisible by 2.
# 
# 1)
# 2
# 1
# 6
# 1
# 
# Returns: "not divisible"
# 
# 2 is not divisible by 6.
# 
# 2)
# 1000000000
# 1000000000
# 1000000000
# 200000000
# 
# Returns: "divisible"
# 
# Now the numbers are huge, but we can see that AB is divisible by CD from the fact that A=C and B>D.
# 
# 3)
# 8
# 100
# 4
# 200
# 
# Returns: "not divisible"
# 
# We can rewrite 8100 as (23)100 = 2300.
# Similarly, 4200 = (22)200 = 2400.
# Thus, 8100 is not divisible by 4200.
# 
# 4)
# 999999937
# 1000000000
# 999999929
# 1
# 
# Returns: "not divisible"
# 
# Here A and C are distinct prime numbers, which means AB cannot have C as its divisor.
# 
# 5)
# 2
# 2
# 4
# 1
# 
# Returns: "divisible"
# 
# 
# 
# END KAWIGIEDIT TESTING
#Powered by KawigiEdit-pfx 2.1.9!
