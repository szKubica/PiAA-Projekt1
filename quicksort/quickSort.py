import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.dirname(dir_path)
sys.path.append(parent_dir_path) 
import time 
from main import *


def test_sorted_list(tab):
    print(type(tab))
    for i in range(len(tab)-1):
        if int(tab[i][1]) <= int(tab[i+1][1]):
           pass
        else:
            raise Exception("Test nie przeszedl")

def quickSort(tab):
    if len(tab) <= 1:
        return tab
    if len(tab) % 2 == 0:
        pivot = int((tab[len(tab)//2][1] + tab[len(tab)//2-1][1]) / 2)
    else:
        pivot = int(tab[len(tab)//2][1])
    left = []
    right = []
    middle = []
    for x in tab:
        if x[1] < pivot:
            left.append(x)
        if x[1] == pivot:
            middle.append(x)           
        if x[1] > pivot:
            right.append(x)
    return quickSort(left) + middle + quickSort(right)

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
        # test_sorted_list(x.data)
        start_time = time.time() # start measuring time
        print("ILOSC ELEMENTOW", len(x.data))
        test_sorted_list(quickSort(x.data))
        quickSort(x.data)
        end_time = time.time() # end measuring time
        print("Time taken to sort:", end_time - start_time) # print the time taken to sort
        x.get_lowest_value()
        x.get_highest_value()
        x.get_average_value()
        x.get_mediane()
