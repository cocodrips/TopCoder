import math
import string

class StrongPrimePower:
  def baseAndExponent(self, n):
    n = int(n)
    candi = ()
    for i in xrange(2,60):
      p = int(round(math.pow(n, 1.0/i)))
      if not self.isPrime(p):
        continue
      if p ** i  == n:
        candi = (p, i)
        print candi
    return candi

  def isPrime(self, m):
    i = 2
    while i * i < m:
      if m % i == 0:
        return False
      i += 1
    return True


# BEGIN KAWIGIEDIT TESTING
# Generated by KawigiEdit-pfx 2.1.9
import sys
import time
def KawigiEdit_RunTest(testNum, p0, hasAnswer, p1):
	sys.stdout.write(str("Test ") + str(testNum) + str(": [") + str("\"") + str(p0) + str("\""))
	print(str("]"))
	obj = StrongPrimePower()
	startTime = time.clock()
	answer = obj.baseAndExponent(p0)
	endTime = time.clock()
	res = True
	print(str("Time: ") + str((endTime - startTime)) + str(" seconds"))
	if (hasAnswer):
		print(str("Desired answer:"))
		sys.stdout.write(str("\t") + str("{"))
		for i in range(len(p1)):
			if (i > 0):
				sys.stdout.write(str(","))
			
			sys.stdout.write(str(p1[i]))
		
		print(str("}"))
	
	print(str("Your answer:"))
	sys.stdout.write(str("\t") + str("{"))
	for i in range(len(answer)):
		if (i > 0):
			sys.stdout.write(str(","))
		
		sys.stdout.write(str(answer[i]))
	
	print(str("}"))
	if (hasAnswer):
		if (len(answer) != len(p1)):
			res = False
		else:
			for i in range(len(answer)):
				if (answer[i] != p1[i]):
					res = False
				
			
		
	
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
p0 = "27"
p1 = [3,3]
all_right = KawigiEdit_RunTest(0, p0, True, p1) and all_right
# ------------------

# ----- test 1 -----
p0 = "10"
p1 = []
all_right = KawigiEdit_RunTest(1, p0, True, p1) and all_right
# ------------------

# ----- test 2 -----
p0 = "7"
p1 = []
all_right = KawigiEdit_RunTest(2, p0, True, p1) and all_right
# ------------------

# ----- test 3 -----
p0 = "1296"
p1 = []
all_right = KawigiEdit_RunTest(3, p0, True, p1) and all_right
# ------------------

# ----- test 4 -----
p0 = "576460752303423488"
p1 = [2,59]
all_right = KawigiEdit_RunTest(4, p0, True, p1) and all_right
# ------------------

# ----- test 5 -----
p0 = "999999874000003969"
p1 = [999999937,2]
all_right = KawigiEdit_RunTest(5, p0, True, p1) and all_right
# ------------------

if (all_right):
	print(str("You're a stud (at least on the example cases)!"))
else:
	print(str("Some of the test cases had errors."))

# PROBLEM STATEMENT
# 
# 
# NOTE: This problem statement contains superscripts that may not display properly if viewed outside of the applet.
#
#
#
# A number which can be represented as pq, where p is a prime number and q is an integer greater than 0, is called a prime power. If q is larger than 1, we call the number a strong prime power. You are given an integer n.  If n is a strong prime power, return an tuple (integer) containing exactly two elements.  The first element is p and the second element is q.  If n is not a strong prime power, return an empty tuple (integer).
#
# 
# DEFINITION
# Class:StrongPrimePower
# Method:baseAndExponent
# Parameters:string
# Returns:tuple (integer)
# Method signature:def baseAndExponent(self, n):
# 
# 
# CONSTRAINTS
# -n will contain digits ('0' - '9') only.
# -n will represent an integer between 2 and 10^18, inclusive.
# -n will have no leading zeros.
# 
# 
# EXAMPLES
# 
# 0)
# "27"
# 
# Returns: {3, 3 }
# 
# 27 = 33. This is a strong prime power.
# 
# 1)
# "10"
# 
# Returns: { }
# 
# 10 = 2 * 5. This is not a strong prime power.
# 
# 2)
# "7"
# 
# Returns: { }
# 
# A prime number is not a strong prime power.
# 
# 3)
# "1296"
# 
# Returns: { }
# 
# 
# 
# 4)
# "576460752303423488"
# 
# Returns: {2, 59 }
# 
# 
# 
# 5)
# "999999874000003969"
# 
# Returns: {999999937, 2 }
# 
# 
# 
# END KAWIGIEDIT TESTING
#Powered by KawigiEdit-pfx 2.1.9!