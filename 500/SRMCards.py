import math
import string

class SRMCards:
    def maxTurns(self, cards):
        cards = list(cards)
        cards.sort()

        i = 0
        while i < len(cards) - 1:
          if cards[i] + 1 == cards[i+1]:
            cards.pop(i+1)
          i+=1

        return len(cards)

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
	obj = SRMCards()
	startTime = time.clock()
	answer = obj.maxTurns(p0)
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
p0 = [498,499]
p1 = 1
all_right = KawigiEdit_RunTest(0, p0, True, p1) and all_right
# ------------------

# ----- test 1 -----
p0 = [491,492,495,497,498,499]
p1 = 4
all_right = KawigiEdit_RunTest(1, p0, True, p1) and all_right
# ------------------

# ----- test 2 -----
p0 = [100,200,300,400]
p1 = 4
all_right = KawigiEdit_RunTest(2, p0, True, p1) and all_right
# ------------------

# ----- test 3 -----
p0 = [11,12,102,13,100,101,99,9,8,1]
p1 = 6
all_right = KawigiEdit_RunTest(3, p0, True, p1) and all_right
# ------------------

# ----- test 4 -----
p0 = [118,321,322,119,120,320]
p1 = 4
all_right = KawigiEdit_RunTest(4, p0, True, p1) and all_right
# ------------------

# ----- test 5 -----
p0 = [10,11,12,13,14,1,2,3,4,5,6,7,8,9]
p1 = 7
all_right = KawigiEdit_RunTest(5, p0, True, p1) and all_right
# ------------------

if (all_right):
	print(str("You're a stud (at least on the example cases)!"))
else:
	print(str("Some of the test cases had errors."))

# PROBLEM STATEMENT
# Dmitry likes TopCoder Single Round Matches. Once, he registered for an SRM and was waiting for the coding phase to begin. To entertain himself while waiting, he decided to play the following game.
#
# He makes a pile of cards, and on each card, he writes the number of an SRM in which he has competed.  No two cards contain the same number.  He then takes turns until the pile is empty.  Each turn consists of the following sequence of actions:
#
# Dmitry chooses an arbitrary card from the pile. Let A be the number written on this card.
# The card with number A is removed from the pile.
# If the pile contains a card with number A-1, that card is removed from the pile.
# If the pile contains a card with number A+1, that card is removed from the pile.
#
# The game is finished when the pile becomes empty. It's fun to play the game, so Dmitry wants to spend as much time as possible playing it.
#
# You are given a tuple (integer) cards containing the numbers written on the cards in the pile before the start of the game. Return the largest possible number of turns in which Dmitry can finish the game.
#
# DEFINITION
# Class:SRMCards
# Method:maxTurns
# Parameters:tuple (integer)
# Returns:integer
# Method signature:def maxTurns(self, cards):
# 
# 
# CONSTRAINTS
# -cards will contain between 1 and 50 elements, inclusive.
# -Each element of cards will be between 1 and 499, inclusive.
# -All elements of cards will be distinct.
# 
# 
# EXAMPLES
# 
# 0)
# {498, 499}
# 
# Returns: 1
# 
# In the first turn, Dmitry can choose A = 498 or A = 499. In any of these cases both cards will be removed from the pile and the game will be finished.
# 
# 1)
# {491, 492, 495, 497, 498, 499}
# 
# Returns: 4
# 
# One out of many possible ways to spend 4 turns playing this game is to choose the following numbers in each turn: 497, 499, 495, 492.
# 
# 2)
# {100, 200, 300, 400}
# 
# Returns: 4
# 
# 
# 
# 3)
# {11, 12, 102, 13, 100, 101, 99, 9, 8, 1}
# 
# Returns: 6
# 
# Note that the elements of cards are not necessarily sorted in ascending order.
# 
# 4)
# {118, 321, 322, 119, 120, 320}
# 
# Returns: 4
# 
# 5)
# {10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# 
# Returns: 7
# 
# 
# 
# END KAWIGIEDIT TESTING
#Powered by KawigiEdit-pfx 2.1.9!