class ErasingCharacters:
    def simulate(self, s):
        while True:
            for i in xrange(len(s)-1):
                if s[i] == s[i+1]:
                    s = s[0:i] + s[i+2:]
                    break
            else:
                break
        return s

# BEGIN KAWIGIEDIT TESTING
# Generated by KawigiEdit-pfx 2.1.9
import sys
import time
def KawigiEdit_RunTest(testNum, p0, hasAnswer, p1):
	sys.stdout.write(str("Test ") + str(testNum) + str(": [") + str("\"") + str(p0) + str("\""))
	print(str("]"))
	obj = ErasingCharacters()
	startTime = time.clock()
	answer = obj.simulate(p0)
	endTime = time.clock()
	res = True
	print(str("Time: ") + str((endTime - startTime)) + str(" seconds"))
	if (hasAnswer):
		print(str("Desired answer:"))
		print(str("\t") + str("\"") + str(p1) + str("\""))
	
	print(str("Your answer:"))
	print(str("\t") + str("\"") + str(answer) + str("\""))
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
p0 = "cieeilll"
p1 = "cl"
all_right = KawigiEdit_RunTest(0, p0, True, p1) and all_right
# ------------------

# ----- test 1 -----
p0 = "topcoder"
p1 = "topcoder"
all_right = KawigiEdit_RunTest(1, p0, True, p1) and all_right
# ------------------

# ----- test 2 -----
p0 = "abcdefghijklmnopqrstuvwxyyxwvutsrqponmlkjihgfedcba"
p1 = ""
all_right = KawigiEdit_RunTest(2, p0, True, p1) and all_right
# ------------------

# ----- test 3 -----
p0 = "bacaabaccbaaccabbcabbacabcbba"
p1 = "bacbaca"
all_right = KawigiEdit_RunTest(3, p0, True, p1) and all_right
# ------------------

# ----- test 4 -----
p0 = "eel"
p1 = "l"
all_right = KawigiEdit_RunTest(4, p0, True, p1) and all_right
# ------------------

# ----- test 5 -----
p0 = "eell"
p1 = ""
all_right = KawigiEdit_RunTest(5, p0, True, p1) and all_right
# ------------------

if (all_right):
	print(str("You're a stud (at least on the example cases)!"))
else:
	print(str("Some of the test cases had errors."))

# PROBLEM STATEMENT
# Fox Ciel received a string as a birthday present. However, the string was too long for her, so she decided to make it shorter by erasing some characters.
#
#
# The erasing process will look as follows:
#
# Find the smallest i such that the i-th character and the (i+1)-th character of the string are same.
# If there is no such i, end the process.
# Remove the i-th and the (i+1)-th character of the string, and repeat from 1.
#
#
#
# For example, if she receives "cieeilll", she will change the string as follows: "cieeilll" -> "ciilll" -> "clll" -> "cl". You are given a string s. Return the string she will get after she erases characters as described above.
#
# DEFINITION
# Class:ErasingCharacters
# Method:simulate
# Parameters:string
# Returns:string
# Method signature:def simulate(self, s):
# 
# 
# CONSTRAINTS
# -s will contain between 1 and 50 characters, inclusive.
# -Each character in s will be a lowercase letter ('a'-'z').
# 
# 
# EXAMPLES
# 
# 0)
# "cieeilll"
# 
# Returns: "cl"
# 
# This is the example from the statement.
# 
# 1)
# "topcoder"
# 
# Returns: "topcoder"
# 
# She won't erase any characters at all.
# 
# 2)
# "abcdefghijklmnopqrstuvwxyyxwvutsrqponmlkjihgfedcba"
# 
# Returns: ""
# 
# 
# 
# 3)
# "bacaabaccbaaccabbcabbacabcbba"
# 
# Returns: "bacbaca"
# 
# 
# 
# 4)
# "eel"
# 
# Returns: "l"
# 
# 
# 
# END KAWIGIEDIT TESTING

#Powered by KawigiEdit-pfx 2.1.9!
