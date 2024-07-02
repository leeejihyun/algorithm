#!/bin/bash

ex1="5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X"
ex2="4
S S S T
X X X X
X X X X
T T T X"

python A20.py <<< $ex1 # YES
python A20.py <<< $ex2 # NO