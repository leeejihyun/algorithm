#!/bin/bash

ex1="3 3
1 0 2
0 0 0
3 0 0
2 3 2"
ex2="3 3
1 0 2
0 0 0
3 0 0
1 2 2"

python A17.py <<< $ex1
python A17.py <<< $ex2