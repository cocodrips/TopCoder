import math
import string

class LittleElephantAndIntervalsDiv2:
    def getNumber(self, M, L, R):
        s = set()
        count = 0
        for i in reversed(xrange(0, len(L))):
            is_paint = False
            for n in range(L[i], R[i]+1):
                if n not in s:
                    is_paint = True
                s.add(n)
            else:
                if is_paint:
                    count += 1
        return pow(2, count)



# BEGIN KAWIGIEDIT TESTING
# Generated by KawigiEdit-pfx 2.1.9
import sys
import time
def KawigiEdit_RunTest(testNum, p0, p1, p2, hasAnswer, p3):
	sys.stdout.write(str("Test ") + str(testNum) + str(": [") + str(p0) + str(",") + str("{"))
	for i in range(len(p1)):
		if (i > 0):
			sys.stdout.write(str(","))
		
		sys.stdout.write(str(p1[i]))
	
	sys.stdout.write(str("}") + str(",") + str("{"))
	for i in range(len(p2)):
		if (i > 0):
			sys.stdout.write(str(","))
		
		sys.stdout.write(str(p2[i]))
	
	sys.stdout.write(str("}"))
	print(str("]"))
	obj = LittleElephantAndIntervalsDiv2()
	startTime = time.clock()
	answer = obj.getNumber(p0, p1, p2)
	endTime = time.clock()
	res = True
	print(str("Time: ") + str((endTime - startTime)) + str(" seconds"))
	if (hasAnswer):
		print(str("Desired answer:"))
		print(str("\t") + str(p3))
	
	print(str("Your answer:"))
	print(str("\t") + str(answer))
	if (hasAnswer):
		res = answer == p3
	
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
p0 = 4
p1 = [1,2,3]
p2 = [1,2,3]
p3 = 8
all_right = KawigiEdit_RunTest(0, p0, p1, p2, True, p3) and all_right
# ------------------

# ----- test 1 -----
p0 = 3
p1 = [1,1,2]
p2 = [3,1,3]
p3 = 4
all_right = KawigiEdit_RunTest(1, p0, p1, p2, True, p3) and all_right
# ------------------

# ----- test 2 -----
p0 = 100
p1 = [47]
p2 = [74]
p3 = 2
all_right = KawigiEdit_RunTest(2, p0, p1, p2, True, p3) and all_right
# ------------------

# ----- test 3 -----
p0 = 100
p1 = [10,20,50]
p2 = [20,50,100]
p3 = 8
all_right = KawigiEdit_RunTest(3, p0, p1, p2, True, p3) and all_right
# ------------------

# ----- test 4 -----
p0 = 42
p1 = [5,23,4,1,15,2,22,26,13,16]
p2 = [30,41,17,1,21,6,28,30,15,19]
p3 = 512
all_right = KawigiEdit_RunTest(4, p0, p1, p2, True, p3) and all_right
# ------------------

if (all_right):
	print(str("You're a stud (at least on the example cases)!"))
else:
	print(str("Some of the test cases had errors."))

# PROBLEM STATEMENT
# 
# Little Elephant from the Zoo of Lviv has some balls arranged in a row. Each ball can be painted in one of two possible colors: black or white. Initially all the balls are painted white. 
# 
# 
# 
# 
# You are given an integer M, which represents the number of balls in the row. 
# The balls are numbered from left to right, starting from 1. 
# You are also given two tuple (integer)s L and R. 
# To repaint balls, Little Elephant wants to use a robot. 
# The robot will paint the balls in several consecutive stages.
# For each i, the i-th stage (1-based index) will look as follows:
# First, the robot will choose one of the two colors: white or black.
# Then, the robot will paint the balls with indices from L[i-1] to R[i-1], inclusive, using the chosen color.
# (Painting a ball covers all previous layers of paint.)
# 
# 
# 
# 
# Return the number of different colorings Little Elephant can get after the last stage. (Two colorings are considered different if there exists some ball that is white in one coloring and black in the other one).
# 
# 
# DEFINITION
# Class:LittleElephantAndIntervalsDiv2
# Method:getNumber
# Parameters:integer, tuple (integer), tuple (integer)
# Returns:integer
# Method signature:def getNumber(self, M, L, R):
# 
# 
# CONSTRAINTS
# -M will be between 1 and 100, inclusive. 
# -L will contain between 1 and 10 elements, inclusive.
# -R will contain the same number of elements as L.
# -Each element of R will be between 1 and M, inclusive.
# -i-th element of L will be between 1 and R[i], inclusive.
# 
# 
# EXAMPLES
# 
# 0)
# 4
# {1, 2, 3}
# {1, 2, 3}
# 
# Returns: 8
# 
# In the three stages the robot will choose the color for balls number 1, 2, and 3. The choices are independent of each other. The last, fourth ball will always remain white. Thus there are 2*2*2 = 8 different colorings.
# 
# 1)
# 3
# {1, 1, 2}
# {3, 1, 3}
# 
# Returns: 4
# 
# In the first stage the robot colors all three balls. The color chosen for the first stage does not matter, because in the second stage the robot will repaint ball 1, and in the third stage it will repaint balls 2 and 3.
# 
# 2)
# 100
# {47}
# {74}
# 
# Returns: 2
# 
# 
# 
# 3)
# 100
# {10, 20, 50}
# {20, 50, 100}
# 
# Returns: 8
# 
# 
# 
# 4)
# 42
# {5, 23, 4, 1, 15, 2, 22, 26, 13, 16}
# {30, 41, 17, 1, 21, 6, 28, 30, 15, 19}
# 
# Returns: 512
# 
# 
# 
# END KAWIGIEDIT TESTING
#Powered by KawigiEdit-pfx 2.1.9!
