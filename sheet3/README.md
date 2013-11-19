Sheet 3
=======

matrix.py
---------

This file contains a basic matrix implementation which represents
a semetric matrix. The implementation is based on the python
dict data structure. It only stores non-zero values of the upper
triangle of the matrix, and is thus as storage efficient as the
underlying dict allows.

Furthermore, this matrix implementation is indexed indirectly for
the sake of usability.

Note: matix.py does not contain any 'real' logic, but implements
some rapper classes which ease the use of the matrix and the
implementation of further algorithms upon it.


contract.py
-----------

Contains an implementation of the CONTRACT(k) algorithm. It is
split up into three parts:

	- contract(k): establishing a loop to execute k iterations of contraction
	- contract_node(x,y): contracts the nodes x and y (contracts the edge between x and y)
	- select_edge(): selecting an edge with the liklihood being proportional to its weight

The computational as well as the storage complexity of the implemented
contraction algorithm is O(n^2)


fastcut.py
----------

Contains a straight forward implementation of the Fast-Cut algorithm.


test.py
-------

Two rudimentary test, one for contract (example graph from lecture),
and one for Fast-Cut.
