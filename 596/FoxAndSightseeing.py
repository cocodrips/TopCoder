import math
import string

class FoxAndSightseeing:
    def getMin(self, position):
        min_n = 10000000000
        for skip_i in xrange(1, len(position)):
            prev = position[0]
            n = 0
            for i in xrange(1, len(position)-1):
                if skip_i != i:
                    n += abs(position[i] - prev)
                    prev = position[i]
            n += abs(position[len(position)-1] - prev)
            min_n = min(min_n, n)

        return min_n

# BEGIN KAWIGIEDIT TESTING
# Generated by KawigiEdit-pfx 2.1.9
import sys
import time
def KawigiEdit_RunTest(testNum, p0, hasAnswer, p1):
	sys.stdout.write(str("Test ") + str(testNum) + str(": [") + str("{"))
	for i in range(len(p0)):
		if (i > 0):
			sys.stdout.write(str(","))
		
		sys.stdout.write(str(p0[i]))
	
	sys.stdout.write(str("}"))
	print(str("]"))
	obj = FoxAndSightseeing()
	startTime = time.clock()
	answer = obj.getMin(p0)
	endTime = time.clock()
	res = True
	print(str("Time: ") + str((endTime - startTime)) + str(" seconds"))
	if (hasAnswer):
		print(str("Desired answer:"))
		print(str("\t") + str(p1))
	
	print(str("Your answer:"))
	print(str("\t") + str(answer))
	if (hasAnswer):
		res = answer == p1
	
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
p0 = [1,4,-1,3]
p1 = 4
all_right = KawigiEdit_RunTest(0, p0, True, p1) and all_right
# ------------------

# ----- test 1 -----
p0 = [-2, 4, 3]
p1 = 5
all_right = KawigiEdit_RunTest(1, p0, True, p1) and all_right
# ------------------

# ----- test 2 -----
p0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p1 = 9
all_right = KawigiEdit_RunTest(2, p0, True, p1) and all_right
# ------------------

# ----- test 3 -----
p0 = [100, -100, 99, -99]
p1 = 199
all_right = KawigiEdit_RunTest(3, p0, True, p1) and all_right
# ------------------

# ----- test 4 -----
p0 = [74,84,92,23,5,-70,-47,-59,24,-86,-39,99,85,-42,54,100,47,-3,42,38]
p1 = 836
all_right = KawigiEdit_RunTest(4, p0, True, p1) and all_right
# ------------------

# ----- test 5 -----
p0 = [2,-3,5,7,-11,-13,17,-19,23,29,-31,-37,-41,43,-47,-53,-59,61,-67,71]
p1 = 535
all_right = KawigiEdit_RunTest(5, p0, True, p1) and all_right
# ------------------

# ----- test 6 -----
p0 = [1,1,1,1,1,1]
p1 = 0
all_right = KawigiEdit_RunTest(6, p0, True, p1) and all_right
# ------------------

# ----- test 7 -----
p0 = [1,1,1,2]
p1 = 1
all_right = KawigiEdit_RunTest(7, p0, True, p1) and all_right
# ------------------

if (all_right):
	print(str("You're a stud (at least on the example cases)!"))
else:
	print(str("Some of the test cases had errors."))

# PROBLEM STATEMENT
# 
# Fox Ciel is staying in Linear Country for sightseeing.
# The country consists of N cities numbered 0 through N-1.
# Ciel is currently staying in city 0.
# 
# 
# In this problem, we assume that the country is a straight line and that each city is a point on this line.
# You are given a tuple (integer) position with N elements.
# The i-th element in position represents the coordinate of the city i.
# The cities are numbered arbitrarily, their numbers are not related to their positions.
# Thus, distance between city i and city j is |position[i] - position[j]|,
# where |z| represents the absolute value of z.
# 
# 
# Ciel wanted to visit all the cities, so she planned a tour.
# She was going to visit city 0 on day 1, visit city 1 on day 2, and so on.
# She wanted to terminate the tour upon arrival to city N-1.
# 
# 
# Unfortunately, it turned out that Ciel's holiday has to be one day shorter.
# Of course, she must still start in city 0 and end in city N-1, so she decided to skip one of the other N-2 cities (i.e., one of cities 1 through N-2).
# She still wants to visit the other cities in the order given by their numbers.
# For example, if N=5, Ciel has three possibilities for her holiday: she will visit the cities in one of the orders (0,1,2,4), (0,1,3,4), or (0,2,3,4).
# 
# 
# Among these possibilities, Ciel will choose the one where the total distance she will have to travel is minimized.
# Compute and return this minimum total distance.
# 
# 
# 
# DEFINITION
# Class:FoxAndSightseeing
# Method:getMin
# Parameters:tuple (integer)
# Returns:integer
# Method signature:def getMin(self, position):
# 
# 
# NOTES
# -You are not given the value of N, but you can easily determine it: N is equal to the number of elements in position.
# 
# 
# CONSTRAINTS
# -position will contain between 3 and 50 elements, inclusive.
# -Each element of position will be between -100 and 100, inclusive.
# -All the elements in position will be distinct.
# 
# 
# EXAMPLES
# 
# 0)
# {1, 4, -1, 3}
# 
# Returns: 4
# 
# There are two strategies for Ciel.
# 
# Skip city 1. The total distance is |1-(-1)|+|(-1)-3| = 2+4 = 6.
# Skip city 2. The total distance is |1-4|+|4-3| = 3+1 = 4.
# 
# The second choice is better. So you should output 4.
# 
# 1)
# {-2, 4, 3}
# 
# Returns: 5
# 
# There is only one strategy for Ciel: She skips city 1. The total distance is |(-2)-3| = 5.
# 
# 2)
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# 
# Returns: 9
# 
# For any choice she makes, the total distance is 9.
# 
# 3)
# {100, -100, 99, -99}
# 
# Returns: 199
# 
# The optimum strategy is to skip city 1.
# 
# 4)
# {74,84,92,23,5,-70,-47,-59,24,-86,-39,99,85,-42,54,100,47,-3,42,38}
# 
# Returns: 836
# 
# 
# 
# 5)
# {2,-3,5,7,-11,-13,17,-19,23,29,-31,-37,-41,43,-47,-53,-59,61,-67,71}
#
# Returns: 535
#
# 
# 
# END KAWIGIEDIT TESTING

#Powered by KawigiEdit-pfx 2.1.9!
