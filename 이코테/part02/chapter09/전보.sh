#!/bin/bash

ex="3 2 1
1 2 4
1 3 2"

# 입력된 텍스트를 파이썬 스크립트에 전달하여 실행
# python 전보.py <<< "$ex"
python 9-5.py <<< "$ex"