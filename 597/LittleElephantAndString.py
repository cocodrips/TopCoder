import math
import string

class LittleElephantAndString:
    def getNumber(self, A, B):
        if sorted(A) != sorted(B):
            return -1

        A = list(A)[::-1]
        B = list(B)[::-1]

        non_move = 0
        a_index = 0
        b_index = 0
        while(b_index < len(B) and a_index < len(A)):
            while(a_index < len(A)):
                if A[a_index] == B[b_index]:
                    non_move += 1
                    break
                a_index += 1
            b_index += 1
            a_index += 1

        return len(A) - non_move

# BEGIN KAWIGIEDIT TESTING
# Generated by KawigiEdit-pfx 2.1.9
import sys
import time
def KawigiEdit_RunTest(testNum, p0, p1, hasAnswer, p2):
	sys.stdout.write(str("Test ") + str(testNum) + str(": [") + str("\"") + str(p0) + str("\"") + str(",") + str("\"") + str(p1) + str("\""))
	print(str("]"))
	obj = LittleElephantAndString()
	startTime = time.clock()
	answer = obj.getNumber(p0, p1)
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
p0 = "ABC"
p1 = "CBA"
p2 = 2
all_right = KawigiEdit_RunTest(0, p0, p1, True, p2) and all_right
# ------------------

# ----- test 1 -----
p0 = "A"
p1 = "B"
p2 = -1
all_right = KawigiEdit_RunTest(1, p0, p1, True, p2) and all_right
# ------------------

# ----- test 2 -----
p0 = "AAABBB"
p1 = "BBBAAA"
p2 = 3
all_right = KawigiEdit_RunTest(2, p0, p1, True, p2) and all_right
# ------------------

# ----- test 3 -----
p0 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
p1 = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
p2 = 25
all_right = KawigiEdit_RunTest(3, p0, p1, True, p2) and all_right
# ------------------

# ----- test 4 -----
p0 = "A"
p1 = "A"
p2 = 0
all_right = KawigiEdit_RunTest(4, p0, p1, True, p2) and all_right
# ------------------

# ----- test 5 -----
p0 = "DCABA"
p1 = "DACBA"
p2 = 2
all_right = KawigiEdit_RunTest(5, p0, p1, True, p2) and all_right
# ------------------

if (all_right):
	print(str("You're a stud (at least on the example cases)!"))
else:
	print(str("Some of the test cases had errors."))

# PROBLEM STATEMENT
# 
# Little Elephant from the Zoo of Lviv likes strings.
# 
# 
# 
# 
# You are given a string A and a string B of the same length. In one turn Little Elephant can choose any character of A and move it to the beginning of the string (i.e., before the first character of A). Return the minimal number of turns needed to transform A into B. If it's impossible, return -1 instead.
# 
# 
# DEFINITION
# Class:LittleElephantAndString
# Method:getNumber
# Parameters:string, string
# Returns:integer
# Method signature:def getNumber(self, A, B):
# 
# 
# CONSTRAINTS
# -A will contain between 1 and 50 characters, inclusive.
# -B will contain between 1 and 50 characters, inclusive.
# -A and B will be of the same length.
# -A and B will consist of uppercase letters ('A'-'Z') only.
# 
# 
# EXAMPLES
# 
# 0)
# "ABC"
# "CBA"
# 
# Returns: 2
# 
# The optimal solution is to make two turns. On the first turn, choose character 'B' and obtain string "BAC". On the second turn, choose character 'C' and obtain "CBA".
# 
# 1)
# "A"
# "B"
# 
# Returns: -1
# 
# In this case, it's impossible to transform A into B.
# 
# 2)
# "AAABBB"
# "BBBAAA"
# 
# Returns: 3
# 
# 
# 
# 3)
# "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# "ZYXWVUTSRQPONMLKJIHGFEDCBA"
# 
# Returns: 25
# 
# 
# 
# 4)
# "A"
# "A"
# 
# Returns: 0
# 
# 
# 
# 5)
# "DCABA"
# "DACBA"
# 
# Returns: 2
# 
# 
# 
# END KAWIGIEDIT TESTING

#Powered by KawigiEdit-pfx 2.1.9!
