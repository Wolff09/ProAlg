#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy
from random import random
from matrix import DebugableMatrix

def randint(start, stop):
	"""
	Generates a uniformliy distributed random
	number in the interval [start, stop).
	"""
	# generates a uniformly distributed random float in [0.0,1.0)
	rand = random()
	# lift this to [start,stop)
	rand = start + (stop-start) * rand
	return int(rand)


class ContractableMatrix(DebugableMatrix):
	def contract_nodes(self, x, y):
		"""
		This method contracts the nodes x and y.
		This alters also the dimension of the matrix.
		"""
		assert x != y
		if x > y: return self.contract(y, x)

		# fuse all edges of y with the edges of x
		# then delete the edges of y
		for k in range(len(self)):
			self[x,k] += self[y,k]
			del self[y,k]
		# update the row sum and the node sets (keep track of changes)
		self.node_sets[x] += self.node_sets[y]
		del self.node_sets[y]
		del self.node_weights[y]
		del self.indices[y] # linear in len(self.indices)

	def contract(self, k=None):
		k = k or len(self)-2
		assert k <= len(self)-2
		while k > 0:
			x, y = self.select_edge()
			self.contract_nodes(x, y)
			k -= 1

	def select_edge(self):
		"""
		Subrutine of contract.

		Pick an edge of the simple weighted graph
		representat by this objectsuch that the
		liklihood of picking an edge is proportional
		to its weight. Formally:

			Probability( (i,j) is picked )
			= weight(i,j) / sum_of_all_weights

		Returns the result as tupel (row, col).

		Note that no edge is picked from a row
		where the node_weight(i) = 0.
		"""
		total_weight = reduce(lambda x,y: x+y, self.node_weights.values.values())
		rand = randint(0, total_weight)

		# backtrace row of rand
		row = 0
		while rand >= self.node_weights[row]: # no index-out-of-bounds: total_weight never hit
			rand -= self.node_weights[row] # never negative due to while condition
			row += 1

		# backtrace col of rand
		col = row + 1 # first edge entry in row
		while rand >= self[row,col]:
			rand -= self[row,col]
			col += 1

		return row, col
