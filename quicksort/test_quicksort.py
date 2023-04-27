import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.dirname(dir_path)
sys.path.append(parent_dir_path) 
import pytest
from quickSort import tab

def test_sorted_list():
    for i in range(len(tab)-1):
        assert int(tab[i][1]) <= int(tab[i+1][1])