#!/bin/bash

ex1="3 4
1 3 3 2 2 1 4 1 0 6 4 7"
ex2="4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2"

python 금광.py <<< $ex1 # 19
python 금광.py <<< $ex2 # 16