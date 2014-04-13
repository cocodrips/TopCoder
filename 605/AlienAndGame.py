import math
import string

class AlienAndGame:
  def getNumber(self, board):
    arr = []
    for r in board:
      arr.append(list(r))

    rlen = len(arr)
    clen = len(arr[0])

    N = min(rlen, clen)

    for n in range(1, N+1)[::-1]:
      for r1 in xrange(rlen - n):
        for c1 in xrange(clen - n):
          OK = True
          for r in xrange(r1, r1 + n + 1):
            first = arr[r][c1]
            for c in xrange(c1, c1 + n + 1):
              if arr[r][c] != first:
                OK = False
                break
            if not OK:
              break
          if OK:
            return (n+1) * (n+1)
    return 1


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
	obj = AlienAndGame()
	startTime = time.clock()
	answer = obj.getNumber(p0)
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
p0 = ["BB","WW"]
p1 = 4
all_right = KawigiEdit_RunTest(0, p0, True, p1) and all_right
# ------------------

# ----- test 1 -----
p0 = ["W"]
p1 = 1
all_right = KawigiEdit_RunTest(1, p0, True, p1) and all_right
# ------------------

# ----- test 2 -----
p0 = ["WBBB","WBBB","WWWW"]
p1 = 9
all_right = KawigiEdit_RunTest(2, p0, True, p1) and all_right
# ------------------

# ----- test 3 -----
p0 = ["W","B","W","W","W"]
p1 = 1
all_right = KawigiEdit_RunTest(3, p0, True, p1) and all_right
# ------------------

# ----- test 4 -----
p0 = ["BWBBWBB","WWBWWBW","BBBBBBW","WBBBBWB","BBWWWWB","WWWWWWW","BBWWBBB"]
p1 = 9
all_right = KawigiEdit_RunTest(4, p0, True, p1) and all_right
# ------------------

p0 = ["WB" * 25] *  50
p1 = 1
all_right = KawigiEdit_RunTest(4, p0, True, p1) and all_right


if (all_right):
	print(str("You're a stud (at least on the example cases)!"))
else:
	print(str("Some of the test cases had errors."))

# PROBLEM STATEMENT
# 
# Alien Fred wants to destroy the Earth.
# But before he does that, he wants to play the following game.
# 
# 
# 
# 
# He has a rectangular board divided into unit cells.
# Each cell is initially painted black or white.
# You are given a tuple (string) board.
# The character board[i][j] represents the cell with coordinates (i, j).
# Each of those characters is either 'B' (representing a black cell) or 'W' (representing a white cell).
# The game is played in turns.
# In each turn Fred can choose any row of the board and repaint all black cells of the row to white, and vice versa.
# (Note that he can only select rows, not columns.
# Formally, he can choose an index i and change all characters of board[i].)
#
#
#
#
# Fred wants to have a large white square somewhere on his board.
# The sides of Fred's square must be parallel to the sides of the board.
# The white square may be a part of a larger white area.
# (I.e., the cells that touch the square may be both black and white.)
# Find a sequence of turns that produces the largest possible white square somewhere on the board, and return the area of that square.
#
#
# DEFINITION
# Class:AlienAndGame
# Method:getNumber
# Parameters:tuple (string)
# Returns:integer
# Method signature:def getNumber(self, board):
# 
# 
# CONSTRAINTS
# -board will contain between 1 and 50 elements, inclusive.
# -Each element of board will contain between 1 and 50 characters, inclusive.
# -Each element of board will contain the same number of characters.
# -Each character in each element of board will be either 'B' or 'W'.
# 
# 
# EXAMPLES
# 
# 0)
# {"BB",
#  "WW"}
# 
# Returns: 4
# 
# The optimal strategy is to repaint row 0. After this change the entire board will be white, and thus we have a 2*2 white square.
# 
# 1)
# {"W"}
# 
# Returns: 1
# 
# Sometimes the optimal strategy requires no repainting.
# 
# 2)
# {"WBBB",
#  "WBBB",
#  "WWWW"}
# 
# Returns: 9
# 
# We should repaint row 0 and then repaint row 1. 
# The resulting board will contain a 3*3 white square (in rows 0-2 and columns 1-3).
# 
# 3)
# {"W",
#  "B",
#  "W",
#  "W",
#  "W"}
# 
# Returns: 1
# 
# 
# 
# 4)
# {"BWBBWBB",
#  "WWBWWBW",
#  "BBBBBBW",
#  "WBBBBWB",
#  "BBWWWWB",
#  "WWWWWWW",
#  "BBWWBBB"}
# 
# Returns: 9
# 
# 
# 
# END KAWIGIEDIT TESTING
#Powered by KawigiEdit-pfx 2.1.9!
