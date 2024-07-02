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

python 감시-피하기.py <<< $ex1 # YES
python 감시-피하기.py <<< $ex2 # NO