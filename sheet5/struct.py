#!/usr/bin/env python
# -*- coding: utf-8 -*-


def make_formula(formula):
	"""
	Constructs a formula from a list of list of integers.
	The integers become indices and negations is implemented
	by negativeness.
	"""
	def make_name(l):
		return -l if l < 0 else l
	names = [make_name(l) for c in formula for l in c]
	names = sorted(list(set(names))) # removes duplicates the hard-core way :)
	variables = [Variable("x%s" % name) for name in names]
	def make_lit(l):
		name = make_name(l)
		index = names.index(name)
		var = variables[index]
		lit = Literal(var)
		lit.negated = l < 0
		return lit
	def make_clause(c):
		lits = [make_lit(x) for x in c]
		return Clause(lits)
	clauses = [make_clause(c) for c in formula]
	return Formula(variables, clauses)


class Formula(object):
	def __init__(self, variables, clauses):
		self.clauses = clauses
		self.variables = variables

	def __iter__(self):
		return iter(self.variables)

	def __len__(self):
		return len(self.clauses)

	def __getitem__(self, key):
		return self.clauses[key]

	def __repr__(self):
		return "{%s}" % ','.join([str(c) for c in self.clauses])

	def eval(self):
		for clause in self.clauses:
			if not clause.eval(): return False
		return True


class Clause(object):
	def __init__(self, literals):
		self.literals = literals

	def __iter__(self):
		return iter(self.literals)

	def __getitem__(self, key):
		return self.literals[key]

	def __repr__(self):
		return "{%s}" % ','.join(str(l) for l in self.literals)

	def eval(self):
		for lit in self.literals:
			if lit.eval(): return True
		return False


class Literal(object):
	def __init__(self, variable, negated=False):
		self.variable = variable
		self.negated = negated

	def __repr__(self):
		return "%s%s" % ("!" if self.negated else "", self.variable)

	def eval(self):
		return not self.variable.eval() if self.negated else self.variable.eval()


class Variable(object):
	def __init__(self, name, truth_value=None):
		self.name = name
		self.truth_value = truth_value

	def __eq__(self, other):
		return self.name == other.name

	def __repr__(self):
		return "%s" % self.name

	def assign(self, truth_value):
		self.truth_value = bool(truth_value)
		return self.truth_value

	def eval(self):
		return self.truth_value
