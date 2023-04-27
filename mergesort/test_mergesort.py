import pytest

def test_sorted_list(tab):
    for i in range(len(tab)-1):
        assert int(tab[i][1]) <= int(tab[i+1][1])