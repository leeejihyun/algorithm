#!/bin/bash

ex1="3
10
20
40"
ex2="4
10
20
40
50"

python A26.py <<< $ex1 # 100
python A26.py <<< $ex2 # 220