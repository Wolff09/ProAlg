Sheet 5
=======

Installation
------------

Install lp_solve seems to be hassel. My favorite LP/ILP solver,
the GLPK is also a standalone package which needs additional
bindings to use with Python.

So we go along with cvxopt since it is a pure python implementation
available throug pip. And it feels much more pythonic...

So to install just type

```
pip install cvxopt
# or
easy_install cvxopt
```

test.py
-------

Testing script for the implementation. It runs all threee algorithms
with the same random formula for some iterations and puts out their
performace.


struc.py
--------

Here we establish some structures to work with Formulas. We
define the following:
- Formula
- Clauses
- Literals
- Variables

Formulas represent KNF formulas, i.e. a formula is conjunct
of clauses which are a disjunct of literals. Literals are
either a variable or a negated variable.


algA.py
-------

Algorithm A simply randoms some truth values for each variable.


algB.py
-------

Algorithm B solves a relaxation of MAX-CUT using linear programming.
We want to solve:
```
max	sum(z_j, j=1...m)
s.t	sum(x_i, i in C+) + sum(1-x_i, i in C-) >= zj
	z_j, x_i in [0,1]
```

Thus we solve the following equivalent linear program:
```
min	sum(-z_j, j=1...m)
s.t	z_j + sum(-x_i, i in C+) + sum(x_i, i in C-) <= sum(1, i in C-)
	-z_j <= 0
	-x_i <= 0
	z_j <= 1
	x_i <= 1
```

This linear program is represented by a matrix of size (m+n)x(3m+2n).
A more verbose description of the matix:
- rows m+1 to 2m+n form a negative diagonal unity matrix
- the last m+n rows for a unity matrix
- the first m rows:
  - first m columns form a unity matrix
  - for the other columns: A[row r, column c] = -1 | 0 | 1
    * -1 => x_c appears in clause r non-negated
    *  0 => x_c does not appear in clause r
    *  1 => x_c appears in clause r negated


algC.py
-------

Implementation of Algorithm B. Really easy one... thanks Python!




