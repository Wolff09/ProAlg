#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt, ceil
from copy import deepcopy
from contract import ContractableMatrix


class Matrix(ContractableMatrix):
	def copy(self):
		graph = [[self[i,j] for j in range(len(self))] for i in range(len(self))]
		return Matrix(graph)


def fastcut(M):
	"""
	Fast-Cut implementation based on contract,
	as presented in the lecture
	"""
	if len(M) <= 3:
		# enumerate all solutions for size <= 3
		return min_cut(M)
	else:
		p = int(ceil(len(M)/sqrt(2)))
		k = len(M)-p

		# create two independent contractions
		M1, M2 = M.copy(), M
		M1.contract(k)
		M2.contract(k)

		# return smaller cut
		return min(fastcut(M1), fastcut(M2))


def min_cut(M):
	assert len(M) >= 2 and len(M) <= 3
	if len(M) == 2:
		return M[0][1], M.node_sets[0], M.node_sets[1]
	else: # len(M) == 3
		return min([
			(M[0,1]+M[0,2], M.node_sets[0], M.node_sets[1]+M.node_sets[2]),
			(M[0,1]+M[1,2], M.node_sets[1], M.node_sets[0]+M.node_sets[2]),
			(M[0,2]+M[1,2], M.node_sets[2], M.node_sets[0]+M.node_sets[1]),
		])
