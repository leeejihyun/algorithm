#!/bin/bash

ex1="7 2
1 1 2 2 2 2 3"
ex2="7 4
1 1 2 2 2 2 3"

python A27-2.py <<< $ex1 # 4
python A27-2.py <<< $ex2 # -1