#!/bin/bash

ex1="2
5 6
0 0 1 0"
ex2="3
3 4 5
1 0 1 0"
ex3="6
1 2 3 4 5 6
2 1 1 1"

python A19.py <<< $ex1
python A19.py <<< $ex2
python A19.py <<< $ex3