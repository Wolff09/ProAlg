#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import uniform


def max_sat(formula):
	tvs = [var.assign(int(uniform(0,2))) for var in formula]
	return sum([c.eval() for c in formula.clauses]), tvs