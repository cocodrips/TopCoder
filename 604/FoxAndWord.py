import math
import string

class FoxAndWord:
  def howManyPairs(self, words):
    cnt = 0

    for i, word in enumerate(words):
      for j in xrange(i + 1, len(words)):
        if len(words[j]) != len(words[i]): #Contest中書き忘れたとこ。
          continue
        if (words[j]+words[j]).find(word) >= 0:
          cnt += 1

    return cnt




# BEGIN KAWIGIEDIT TESTING
# Generated by KawigiEdit-pfx 2.1.9
import sys
import time
def KawigiEdit_RunTest(testNum, p0, hasAnswer, p1):
	sys.stdout.write(str("Test ") + str(testNum) + str(": [") + str("{"))
	for i in range(len(p0)):
		if (i > 0):
			sys.stdout.write(str(","))
		
		sys.stdout.write(str("\"") + str(p0[i]) + str("\""))
	
	sys.stdout.write(str("}"))
	print(str("]"))
	obj = FoxAndWord()
	startTime = time.clock()
	answer = obj.howManyPairs(p0)
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
p0 = ["tokyo","kyoto"]
p1 = 1
all_right = KawigiEdit_RunTest(0, p0, True, p1) and all_right
# ------------------

# ----- test 1 -----
p0 = ["aaaaa","bbbbb"]
p1 = 0
all_right = KawigiEdit_RunTest(1, p0, True, p1) and all_right
# ------------------

# ----- test 2 -----
p0 = ["ababab","bababa","aaabbb"]
p1 = 1
all_right = KawigiEdit_RunTest(2, p0, True, p1) and all_right
# ------------------

# ----- test 3 -----
p0 = ["eel","ele","lee"]
p1 = 3
all_right = KawigiEdit_RunTest(3, p0, True, p1) and all_right
# ------------------

# ----- test 4 -----
p0 = ["aaa","aab","aba","abb","baa","bab","bba","bbb"]
p1 = 6
all_right = KawigiEdit_RunTest(4, p0, True, p1) and all_right
# ------------------

# ----- test 5 -----
p0 = ["top","coder"]
p1 = 0
all_right = KawigiEdit_RunTest(5, p0, True, p1) and all_right
# ------------------

if (all_right):
	print(str("You're a stud (at least on the example cases)!"))
else:
	print(str("Some of the test cases had errors."))

# PROBLEM STATEMENT
# One day, Fox Ciel looked at the words "tokyo" and "kyoto" and noticed an unusual property:
# We can split "tokyo" into "to"+"kyo", and then swap those two parts to obtain "kyo"+"to" = "kyoto".
#
#
# Formally, let S and T be two different strings.
# We call the pair (S,T) interesting if there are two non-empty strings A and B such that S = A+B and T = B+A.
# For example, according to this definition, if S="tokyo" and T="kyoto", then the pair (S,T) is interesting, because we can find A="to" and B="kyo".
#
#
# You are given a tuple (string) words.
# Return the number of interesting pairs we can find among the elements of words.
# Only count each pair once.
# E.g., ("tokyo","kyoto") and ("kyoto","tokyo") is the same interesting pair.
# 
# DEFINITION
# Class:FoxAndWord
# Method:howManyPairs
# Parameters:tuple (string)
# Returns:integer
# Method signature:def howManyPairs(self, words):
# 
# 
# CONSTRAINTS
# -words will contain between 2 and 50 elements, inclusive.
# -Each element of words will contain between 1 and 50 characters, inclusive.
# -Each character in each element of words will be a lowercase letter ('a'-'z').
# -All the elements in words will be pairwise distinct.
# 
# 
# EXAMPLES
# 
# 0)
# {"tokyo", "kyoto"}
# 
# Returns: 1
# 
# As mentioned in the problem statement, ("tokyo", "kyoto") is an interesting pair.
# 
# 1)
# {"aaaaa", "bbbbb"}
# 
# Returns: 0
# 
# ("aaaaa", "bbbbb") is not an interesting pair.
# 
# 2)
# {"ababab","bababa","aaabbb"}
# 
# Returns: 1
# 
# There is one interesting pair: ("ababab","bababa").
# Note that for this interesting pair there is more than one way to choose the strings A and B.
# 
# 3)
# {"eel", "ele", "lee"}
# 
# Returns: 3
# 
# 
# 
# 4)
# {"aaa", "aab", "aba", "abb", "baa", "bab", "bba", "bbb"}
# 
# Returns: 6
# 
# 
# 
# 5)
# {"top","coder"}
# 
# Returns: 0
# 
# Different elements of words may have different lengths.
# 
# 
# END KAWIGIEDIT TESTING
#Powered by KawigiEdit-pfx 2.1.9!
