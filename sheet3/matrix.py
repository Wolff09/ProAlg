#!/usr/bin/env python
# -*- coding: utf-8 -*-

class IndirectAddressedDictonary(object):
	"""
	This class wraps a common python dict object and
	addresses it indirectly by doing an additional
	dereferencing step based on a provided function.
	"""
	def __init__(self, func, init=None, default=None):
		self.index_of = func
		self.values = init or {}
		self.default = default

	def __getitem__(self, key):
		key = self.index_of(key)
		return self.values.get(key, self.default) if key != None else self.default

	def __setitem__(self, key, value):
		key = self.index_of(key)
		if key == None: return
		elif value != self.default: self.values[key] = value
		elif key in self.values: del self.values[key]

	def __delitem__(self, key):
		key = self.index_of(key)
		if key != None and key in self.values: del self.values[key]

	def __len__(self):
		return len(self.values)

	def __iter__(self):
		return self.values.iteritems()


class RowDict(IndirectAddressedDictonary):
	def __init__(self, indices):
		index_of = lambda i: indices[i]
		super(RowDict, self).__init__(index_of, default=0)


class EdgeDict(IndirectAddressedDictonary):
	def __init__(self, indices):
		def mkkey(i,j):
			if i == j: return None
			elif i > j: return mkkey(j,i)
			else: return indices[i], indices[j]
		index_of = lambda key: mkkey(*key)
		super(EdgeDict, self).__init__(index_of, default=0)


class BasicMatrix(object):
	"""
	This is an implementation on an nxn+2 matrix as proposed
	on the exercise sheet. To be performant we do not use
	a 2d array but dictonaries with tupel keys to implement
	weight matrix. This matrix is addionally indexed indirectly
	to allow a more performant delete operation.
	"""

	def __init__(self, graph, names=None):
		self.indices = range(len(graph))
		self.edges = EdgeDict(self.indices)
		self.node_sets = RowDict(self.indices)
		self.node_weights = RowDict(self.indices)
		for i in range(len(graph)):
			row_sum = 0
			for j in range(i+1, len(graph)):
				self.edges[i,j] = graph[i][j]
				row_sum += graph[i][j]
			self.node_weights[i] = row_sum
			self.node_sets[i] = [names[i]] if names else [i]

	def __getitem__(self, key):
		return self.edges[key]

	def __setitem__(self, key, value):
		i, j = sorted(key)
		self.node_weights[i] -= self.edges[i,j]
		self.edges[i,j] = value
		self.node_weights[i] += self.edges[i,j]

	def __delitem__(self, key):
		i, j = sorted(key)
		self.node_weights[i] -= self.edges[i,j]
		del self.edges[i,j]

	def __len__(self):
		return len(self.indices)


class DebugableMatrix(BasicMatrix):
	def debug(self, msg=None, rjust=3):
		print msg or "Debug Matrix:"
		for i in range(len(self)):
			row = [str(self.indices[i]).rjust(rjust) + ": "]
			row += [str(self[i,j]).rjust(rjust) for j in range(len(self))]
			row.append( "|".rjust(rjust) )
			row.append( str(self.node_weights[i]).rjust(rjust) )
			row.append( "  " + str(self.node_sets[i]) )
			print ' '.join(row)
