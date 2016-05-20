#!/usr/bin/env python2
import random, math
maxNum = raw_input("How many points are required for a win? ")
print (str(maxNum) + " it is!")
S_Human = 0
S_Computer = 0
C_Human = 0
C_Computer = 0

d = {'Rock': 1, 'Paper': 2, 'Sissors': 3}

class A(object):

	def Rock(self):
		C_Human = 1
		if(C_Computer == C_Human):
			print("Nothng happens")
			return 0
		else if(C_Computer == C_Human+1):
			print("Paper beats rock. Computer Wins!")
			return -1
		else if(C_Computer == C_Human+2):
			print("Rock beats Sissors. Human Wins")
			return 1

	def Paper(self):
		C_Human = 2
		if(C_Computer == C_Human):
			print("Nothng happens")
			return 0
		else if(C_Computer == C_Human+1):
			print("Sissors beats Paper. Computer Wins!")
			return -1
		else if(C_Computer == C_Human-1):
			print("Paper beats Rock. Human Wins!")
			return 1

	def Sissors(self):
		C_Human = 3
		if(C_Computer == C_Human):
			print("Nothing happens")
			return 0
		if(C_Computer == C_Human-1):
			print("Sissors beats paper. Human Wins!")
			return 1
		if(C_Computer == C_Human-2):
			print("Rock beats sissors. Computer Wins!")
			return -1

	def ScoreKeeper(self):


if __name__ == __main__:
	inst = A()
	C_Human = raw_input("1) Rock, 2) Paper or 3) Sissors? ")
	C_Computer = random.randint(0,3)
	if C_Human == 1:
		score = inst.Rock()
	else if C_Human == 2:
		score = inst.Paper()
	else if C_Human == 3:
		score = inst.Sissors

	if(score<0):
		S_Computer += 1
	else if(score==0):
		pass
	else:
		S_Human += 1
