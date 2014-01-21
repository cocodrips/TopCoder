import math
import string

class SplitIntoPairs:
  def makepairs(self, A, X):
    A = list(A)
    A.sort()

    pl = 0
    ch = False
    ch_i = 0
    for i, a in enumerate(A):
      if a >= 0:
        if not ch:
          ch = True
          ch_i = i
        pl += 1

    if pl % 2 == 1:
      if A[ch_i] * A[ch_i - 1] < X:
        return len(A) / 2 - 1


    return len(A) / 2

# BEGIN KAWIGIEDIT TESTING
# Generated by KawigiEdit-pfx 2.1.9
import sys
import time
def KawigiEdit_RunTest(testNum, p0, p1, hasAnswer, p2):
	sys.stdout.write(str("Test ") + str(testNum) + str(": [") + str("{"))
	for i in range(len(p0)):
		if (i > 0):
			sys.stdout.write(str(","))
		
		sys.stdout.write(str(p0[i]))
	
	sys.stdout.write(str("}") + str(",") + str(p1))
	print(str("]"))
	obj = SplitIntoPairs()
	startTime = time.clock()
	answer = obj.makepairs(p0, p1)
	endTime = time.clock()
	res = True
	print(str("Time: ") + str((endTime - startTime)) + str(" seconds"))
	if (hasAnswer):
		print(str("Desired answer:"))
		print(str("\t") + str(p2))
	
	print(str("Your answer:"))
	print(str("\t") + str(answer))
	if (hasAnswer):
		res = answer == p2
	
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
p0 = [2,-1]
p1 = -1
p2 = 0
all_right = KawigiEdit_RunTest(0, p0, p1, True, p2) and all_right
# ------------------

# ----- test 1 -----
p0 = [1,-1]
p1 = -1
p2 = 1
all_right = KawigiEdit_RunTest(1, p0, p1, True, p2) and all_right
# ------------------

# ----- test 2 -----
p0 = [-5,-4,2,3]
p1 = -1
p2 = 2
all_right = KawigiEdit_RunTest(2, p0, p1, True, p2) and all_right
# ------------------

# ----- test 3 -----
p0 = [5,-7,8,-2,-5,3]
p1 = -7
p2 = 3
all_right = KawigiEdit_RunTest(3, p0, p1, True, p2) and all_right
# ------------------

# ----- test 4 -----
p0 = [3,4,5,6,6,-6,-4,-10,-1,-9]
p1 = -2
p2 = 4
all_right = KawigiEdit_RunTest(4, p0, p1, True, p2) and all_right
# ------------------

# ----- test 5 -----
p0 = [1000000,1000000]
p1 = -5
p2 = 1
all_right = KawigiEdit_RunTest(5, p0, p1, True, p2) and all_right
# ------------------


p0 = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80, -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, 1]
p1 = -52
p2 = 25
all_right = KawigiEdit_RunTest(5, p0, p1, True, p2) and all_right

p0 = [-1, -1, 0, 1]
p1 = -1
p2 = 2
all_right = KawigiEdit_RunTest(5, p0, p1, True, p2) and all_right

p0 = [0, 1, 0, 1]
p1 = -1
p2 = 2
all_right = KawigiEdit_RunTest(5, p0, p1, True, p2) and all_right

p0 = [-11, -10, -10,  1, 1, 1]
p1 = -9
p2 = 2
all_right = KawigiEdit_RunTest(5, p0, p1, True, p2) and all_right

if (all_right):
	print(str("You're a stud (at least on the example cases)!"))
else:
	print(str("Some of the test cases had errors."))

# PROBLEM STATEMENT
# You are given a tuple (integer) A with N elements, where N is even.
# Note that some elements of A may be negative.
# You are also given a integer X which is guaranteed to be negative.
# You must divide the elements of A into N/2 disjoint pairs.
# (That is, each element of A must be in exactly one of those pairs.)
# Your goal is to maximize the number of pairs in which the product of the two elements is greater than or equal to X.
# Return the largest possible number of such pairs.
# 
# DEFINITION
# Class:SplitIntoPairs
# Method:makepairs
# Parameters:tuple (integer), integer
# Returns:integer
# Method signature:def makepairs(self, A, X):
# 
# 
# CONSTRAINTS
# -A will contain between 2 and 50 elements, inclusive.
# -The number of elements in A will be even.
# -Each element in A will be between -1,000,000,000 and 1,000,000,000, inclusive.
# -X will be between -1,000,000,000 and -1, inclusive.
# 
# 
# EXAMPLES
# 
# 0)
# {2,-1}
# -1
# 
# Returns: 0
# 
# One possible pair has product -2, which is lower than needed.
# 
# 1)
# {1,-1}
# -1
# 
# Returns: 1
# 
# Here product is -1, it's enough.
# 
# 2)
# {-5,-4,2,3}
# -1
# 
# Returns: 2
# 
# If first pair contains numbers -5 and -4, and second contains 2 and 3, both will have positive product.
# 
# 3)
# {5,-7,8,-2,-5,3}
# -7
# 
# Returns: 3
# 
# Acceptable splitting is {5,8}, {-7,-5} and {-2,3}.
# 
# 4)
# {3,4,5,6,6,-6,-4,-10,-1,-9}
# -2
# 
# Returns: 4
# 
# 
# 
# 5)
# {1000000,1000000}
# -5
# 
# Returns: 1
# 
# Beware overflow.
# 
# END KAWIGIEDIT TESTING
#Powered by KawigiEdit-pfx 2.1.9!
