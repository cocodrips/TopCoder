
import math
import string
import Queue

class ArcadeManao:
    def shortestLadder(self, level, coinRow, coinColumn):
        self.level = level
        self.goal = (coinRow - 1, coinColumn - 1)
        print self.goal
 
        self.R = len(level)
        self.C = len(level[0])
        queue = []
        visited = set()
        if self.add2queue(self.R - 1, 0, queue, visited):
            return 0
        for ladder_len in xrange(self.R):
            while queue:
                q = queue.pop(0)
                visited.add(q)
                if self.add2queue(q[0], q[1] + 1, queue, visited) or self.add2queue(q[0], q[1] - 1, queue, visited):
                    return ladder_len
 
                for r in xrange(1, ladder_len + 1):
                    if self.add2queue(q[0] + r, q[1], queue, visited) or self.add2queue(q[0] - r, q[1], queue, visited):
                        return ladder_len
            queue = [q for q in visited]
        return -1
 
    def add2queue(self, r, c, queue, visited):
        if (r, c) in visited or (r, c) in queue:
            return False
        if r >= self.R or c >= self.C or r < 0 or c < 0:
            return False
        if self.level[r][c] != 'X':
            return False
        if (r, c) == self.goal:
            return True
        queue.append((r, c))
        return False


# BEGIN KAWIGIEDIT TESTING
# Generated by KawigiEdit-pfx 2.1.9
import sys
import time
def KawigiEdit_RunTest(testNum, p0, p1, p2, hasAnswer, p3):
	sys.stdout.write(str("Test ") + str(testNum) + str(": [") + str("{"))
	for i in range(len(p0)):
		if (i > 0):
			sys.stdout.write(str(","))

		sys.stdout.write(str("\"") + str(p0[i]) + str("\""))

	sys.stdout.write(str("}") + str(",") + str(p1) + str(",") + str(p2))
	print(str("]"))
	obj = ArcadeManao()
	startTime = time.clock()
	answer = obj.shortestLadder(p0, p1, p2)
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
p0 = ["XXXX....","...X.XXX","XXX..X..","......X.","XXXXXXXX"]
p1 = 2
p2 = 4
p3 = 2
all_right = KawigiEdit_RunTest(0, p0, p1, p2, True, p3) and all_right
# ------------------

# ----- test 1 -----
p0 = ["XXXX","...X","XXXX"]
p1 = 1
p2 = 1
p3 = 1
all_right = KawigiEdit_RunTest(1, p0, p1, p2, True, p3) and all_right
# ------------------

# ----- test 2 -----
p0 = ["..X..",".X.X.","X...X",".X.X.","..X..","XXXXX"]
p1 = 1
p2 = 3
p3 = 4
all_right = KawigiEdit_RunTest(2, p0, p1, p2, True, p3) and all_right
# ------------------

# ----- test 3 -----
p0 = ["X"]
p1 = 1
p2 = 1
p3 = 0
all_right = KawigiEdit_RunTest(3, p0, p1, p2, True, p3) and all_right
# ------------------

# ----- test 4 -----
p0 = ["XXXXXXXXXX","...X......","XXX.......","X.....XXXX","..XXXXX..X",".........X",".........X","XXXXXXXXXX"]
p1 = 1
p2 = 1
p3 = 2
all_right = KawigiEdit_RunTest(4, p0, p1, p2, True, p3) and all_right
# ------------------

if (all_right):
	print(str("You're a stud (at least on the example cases)!"))
else:
	print(str("Some of the test cases had errors."))

# PROBLEM STATEMENT
# You might remember the old computer arcade games. Here is one about Manao.
#
# The game level is an NxM grid of equal cells. The bottom of some cells has a platform at which Manao can stand. All the cells in the bottommost row contain a platform, thus covering the whole ground of the level. The rows of the grid are numbered from 1 to N starting from the top and the columns are numbered from 1 to M starting from the left. Exactly one cell contains a coin and Manao needs to obtain it.
#
# Initially, Manao is standing on the ground, i.e., in the bottommost row. He can move between two horizontally adjacent cells if both contain a platform. Also, Manao has a ladder which he can use to climb. He can use the ladder to climb both up and down. If the ladder is L units long, Manao can climb between two cells (i1, j) and (i2, j) if both contain a platform and |i1-i2| <= L. Note that Manao carries the ladder along, so he can use it multiple times. You need to determine the minimum ladder length L which is sufficient to acquire the coin.
#
# Take a look at the following picture. On this level, Manao will manage to get the coin with a ladder of length 2.
#
#
#
# You are given a tuple (integer) level containing N elements. The j-th character in the i-th row of level is 'X' if cell (i+1, j+1) contains a platform and '.' otherwise. You are also given integers coinRow and coinColumn. The coin which Manao seeks is located in cell (coinRow, coinColumn) and it is guaranteed that this cell contains a platform.
#
# Return the minimum L such that ladder of length L is enough to get the coin. If Manao can perform the task without using the ladder, return 0.
#
# DEFINITION
# Class:ArcadeManao
# Method:shortestLadder
# Parameters:tuple (string), integer, integer
# Returns:integer
# Method signature:def shortestLadder(self, level, coinRow, coinColumn):
#
#
# NOTES
# -Manao is not allowed to fall. The only way in which he may change his vertical coordinate is by using the ladder.
#
#
# CONSTRAINTS
# -level will contain N elements, where N is between 1 and 50, inclusive.
# -Each element of level will be M characters long, where M is between 1 and 50, inclusive.
# -Each element of level will consist of '.' and 'X' characters only.
# -The last element of level will be entirely filled with 'X'.
# -coinRow will be between 1 and N, inclusive.
# -coinColumn will be between 1 and M, inclusive.
# -level[coinRow - 1][coinColumn - 1] will be 'X'.
#
#
# EXAMPLES
#
# 0)
# {"XXXX....",
#  "...X.XXX",
#  "XXX..X..",
#  "......X.",
#  "XXXXXXXX"}
# 2
# 4
#
# Returns: 2
#
# The example from the problem statement.
#
# 1)
# {"XXXX",
#  "...X",
#  "XXXX"}
# 1
# 1
#
# Returns: 1
#
# Manao can use the ladder to climb from the ground to cell (2, 4), then to cell (1, 4) and then he can walk right to the coin.
#
# 2)
# {"..X..",
#  ".X.X.",
#  "X...X",
#  ".X.X.",
#  "..X..",
#  "XXXXX"}
# 1
# 3
#
# Returns: 4
#
# With a ladder of length 4, Manao can first climb to cell (5, 3) and then right to (1, 3).
#
# 3)
# {"X"}
# 1
# 1
#
# Returns: 0
#
# Manao begins in the same cell as the coin.
#
# 4)
# {"XXXXXXXXXX",
#  "...X......",
#  "XXX.......",
#  "X.....XXXX",
#  "..XXXXX..X",
#  ".........X",
#  ".........X",
#  "XXXXXXXXXX"}
# 1
# 1
#
# Returns: 2
#
#
#
# END KAWIGIEDIT TESTING

#Powered by KawigiEdit-pfx 2.1.9!
