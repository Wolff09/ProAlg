#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from StringIO import StringIO
from random import uniform
from cvxopt import matrix, solvers


def max_sat(formula):
	# solve the lp
	solution = approx_lp(formula)
	rands = [uniform(0,1) for i in range(len(solution))]
	# round randomized
	solution = [1 if r < s else 0 for s,r in zip(solution, rands)]
	for i,v in enumerate(formula):
		v.assign(solution[i])
	return sum([c.eval() for c in formula.clauses]), solution


def approx_lp(formula):
	m = len(formula) # numer of clauses
	n = len(formula.variables) # total number variables

	# objective:
	# minimize z_1 + z_2 + ... z_m
	# = maximize -z_1 + -z_2 + ... + -z_m
	c = [1.0 for j in range(m)] + [0.0 for i in range(n)]

	# matrix for side conditions:
	# -1 if a literal is a negated variable, 1 otherwise -> see README
	def valueOf(var, clause):
		for lit in clause:
			if lit.variable == var:
				if lit.negated: return 1.0 # var negated in clause
				else: return -1.0 # var non-negated in clause
		return 0.0 # var not in clause
	def elemAt(i,j):
		var = formula.variables[j-m]
		clause = formula[i]
		return valueOf(var, clause)
	def col_part(j):
		if j < m:
			return unit(j, length=m)
		else:
			return [elemAt(i,j) for i in range(m)]
	def unit(j, value=1.0, length=n+m):
		return [value if i == j else 0.0 for i in range(length)] # unit vector j times value
	def column(j):
		return col_part(j) + unit(j, -1.0) + unit(j)
	A = [column(j) for j in range(n+m)]


	# vector for side condition:
	def nneg(clause): # computes the number of negations of a clause
		return sum([1.0 for lit in clause if lit.negated])
	b = [nneg(formula[j]) for j in range(m)] + [0.0 for x in range(m+n)] + [1.0 for x in range(m+n)]

	# solve it
	# opt_debug(A, b, c)
	sol = solvers.lp(matrix(c),matrix(A),matrix(b))
	return [round(x,4) for x in sol['x']][m:]


def opt_debug(A, b, c):
	print "----------------------- BEGIN OPT DEBUG -----------------------"
	print "Objective function vector c:\n\t%s" % c
	print "Side condition vector b:\n\t%s" % b
	print "Sice condtion matrix A:"
	for row in A:
		print ' '.join([str(x).rjust(4) for x in row])
	print "------------------------ END OPT DEBUG ------------------------"
