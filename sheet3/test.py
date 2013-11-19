#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastcut import fastcut, Matrix


def test_contract():
	g = [
		[0,2,0,0,4],
		[0,0,2,0,5],
		[0,0,0,3,0],
		[0,0,0,0,3],
		[0,0,0,0,0]
	]
	m = Matrix(g);
	m.debug("Input for testing CONTRACT, example from lecture:")
	m.contract(3)
	m.debug("Output of CONTRACT(3):")


def test_fastcut():
	g = [
		[0,2,0,0,4],
		[0,0,2,0,5],
		[0,0,0,3,0],
		[0,0,0,0,3],
		[0,0,0,0,0]
	]
	m = Matrix(g)
	mc, v1, v2 = fastcut(m)
	format = lambda set: (', '.join([str(x) for x in set]))
	v1, v2 = format(sorted(v1)), format(sorted(v2))
	print ">>> %i=Min-Cut, with\n\tV1={%s}\n\tV2={%s}" % (mc, v1, v2)


if __name__ == '__main__':
	test_contract()
	print "\n\n++++++++ 25 fast-cut trials ++++++++"
	for i in range(25): test_fastcut()