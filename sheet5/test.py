#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from StringIO import StringIO
from algB import max_sat as algB
from algA import max_sat as algA
from algC import max_sat as algC
from struct import make_formula
from random import randint


def test(algo, formula, repetitions=1):
	mi, ma, avg = len(formula)+1, 0, 0
	rescue = sys.stdout
	for i in range(repetitions):
		sys.stdout = StringIO()
		x,y = algo(f)
		sys.stdout = rescue
		avg += x
		mi = min(mi, x)
		ma = max(ma, x)
		print "Result %s: %s %s" % (i+1, x, y) 
	avg = (avg*1.0)/(repetitions*1.0)
	return avg, mi, ma


if __name__ == '__main__':
	n, m, repetitions = 10, 6, 20

	# generate random formula
	def rv():
		# generate random variable (not 0)
		r = randint(-n, n)
		while r == 0:
			r = randint(-n, n)
		return r
	# 3 variables per clause
	f = make_formula([[rv(),rv(),rv()] for i in range(m)])
	print "Random formula: %s" % f

	# let the testing begin
	print "\n############ Testing Algorithm A ############"
	t1 = "Algorithm A", test(algA, f, repetitions)
	print "\n############ Testing Algorithm B ############"
	t2 = "Algorithm B", test(algB, f, repetitions)
	print "\n############ Testing Algorithm C ############"
	t3 = "Algorithm C", test(algC, f, repetitions)

	print "\n############ Performace Overview ############"
	for name, (avg, mini, maxi) in [t1,t2,t3]:
		print "%s: " % name
		print "\tAverage MAX-3-SAT: %s" % round(avg, 4)
		print "\tBest MAX-3-SAT: %s" % round(maxi, 4)
		print "\tWorst MAX-3-SAT: %s" % round(mini, 4)
