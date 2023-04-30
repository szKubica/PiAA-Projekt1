import sys
import os
import gc
import time 
from math import floor
from functools import wraps
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.dirname(dir_path)
parent_dir = os.path.join(dir_path, "..", "mergesort")
sys.path.append(parent_dir_path) 
sys.path.append(parent_dir) 
import random

from main import *
from mergeSort import mergeSort

def test_sorted_list(tab):
    for i in range(len(tab)-1):
        if int(tab[i][1]) <= int(tab[i+1][1]):
           pass
        else:
            raise Exception("Test nie przeszedl")


def bucketSort(tab):
    sorted_tab = []
    m = (tab.volume*3)/4
    buckets = [[] for _ in range(int(m + 1))] 

    bucket_width = (tab.highest_ranking - tab.lowest_ranking)/m
    for element in tab.data:
        i = floor((int(element[1]) - tab.lowest_ranking)/bucket_width)
        buckets[i].append(element)


    for bucket in buckets:
        mergeSort(bucket,0,len(bucket)-1)
        sorted_tab.extend(bucket)

    return sorted_tab

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
        start_time = time.time() # start measuring time
        test_sorted_list(bucketSort(x))
        print("ILOSC ELEMENTOW", len(x.data))
        end_time = time.time() # end measuring time
        print("Time taken to sort:", end_time - start_time) # print the time taken to sort
        x.get_lowest_value()
        x.get_highest_value()
        x.get_average_value()
        x.get_mediane()




