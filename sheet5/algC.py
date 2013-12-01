#!/usr/bin/env python
# -*- coding: utf-8 -*-

from algA import max_sat as algA
from algB import max_sat as algB


def max_sat(formula):
	return max(algA(formula), algB(formula))
