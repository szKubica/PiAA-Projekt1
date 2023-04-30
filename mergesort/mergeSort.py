import sys
import os
import gc
import time 
from functools import wraps
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.dirname(dir_path)
sys.path.append(parent_dir_path) 
from main import *
import pytest


def test_sorted_list(tab):
    for i in range(len(tab)-1):
        if int(tab[i][1]) <= int(tab[i+1][1]):
            pass
        else:
            Exception("Test nie przeszedl")


def merge(tab, l, m, r):
    a = m - l + 1
    b = r - m
    A = [0] * a
    B = [0] * b
    for i in range(a):
        A[i] = tab[l+i]
    for j in range(b):
        B[j] = tab[m + 1 + j]
    i = j = 0
    k = l
    while i < a and j < b:
        if int(A[i][1]) <= int(B[j][1]):
            tab[k] = A[i]
            i += 1
        else:
            tab[k] = B[j]
            j += 1
        k += 1
    while i < a:
        tab[k] = A[i]
        i += 1
        k += 1
    while j < b:
        tab[k] = B[j]
        j += 1
        k += 1

def mergeSort(tab, l, r):
    if l < r:
        m = l+(r-l)//2
        mergeSort(tab, l, m)
        mergeSort(tab, m + 1, r)
        merge(tab, l, m, r)


def display():
    print("tablica przed sortowaniem:")
    print(tab_before)
    print("tablica posortowana:")
    print(tab)


if __name__ == "__main__":

    data_volumes = [10000, 100000, 500000, 1000000, 1216098]

    data_set_list = []

    for i in data_volumes:
        data_set_name = "data_set{}".format(i)
        data_frame = DF(i)
        data_frame.set_data()
        data_set_instance = data_frame.data
        globals()[data_set_name] = data_set_instance
        data_set_list.append(data_frame)

    for x in data_set_list:
        test_sorted_list(x.data)
        start_time = time.time() # start measuring time
        print("ILOSC ELEMENTOW", len(x.data))
        mergeSort(x.data, 0, len(x.data)-1)
        end_time = time.time() # end measuring time
        print("Time taken to sort:", end_time - start_time) # print the time taken to sort
        x.get_lowest_value()
        x.get_highest_value()
        x.get_average_value()
        x.get_mediane()


    gc.collect()