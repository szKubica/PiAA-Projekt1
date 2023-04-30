import pandas as pd
from statistics import mean, median
import numpy as np


class DF:
    def __init__(self, volume):
        self.volume = volume
        self.data = None
        self.average_value = None
        self.median_value = None
    
    def __str__(self):
        return "{}, \n Avarage:{}, Mediane: {}".format(self.data, self.average_value, self.median_value)

    def set_data(self):
        df = pd.read_csv("dane.csv").iloc[:, [1, 2]]
        df = pd.concat([df]*3, ignore_index=True)
        df.columns = ["Film", "rank"]
        df['rank'] = pd.to_numeric(df['rank'], errors='coerce')
        df = df[pd.notnull(df['rank'])]
        mask = df["rank"].notna()
        records = df[mask].to_records(index=False)
        self.data = list(map(tuple, records))[:self.volume]
        self.average_value = mean(map(lambda x: int(x[1]), self.data))
        self.median_value = median(map(lambda x: int(x[1]), self.data))    
        self.highest_ranking = int(max(self.data, key=lambda x: int(x[1]))[1])
        self.lowest_ranking = int(min(self.data, key=lambda x: int(x[1]))[1])

    def get_data(self):
        return self.data
    
    def get_average_value(self):
        print("Average", self.average_value)

    def get_mediane(self):
        print("Mediane", self.median_value)
    
    def get_highest_value(self):
        print("Highest ranking", self.highest_ranking)
    
    def get_lowest_value(self):
        print("Lowest value", self.lowest_ranking)


def test_sorted_list(tab):
    for i in range(len(tab)-1):
        if int(tab[i][1]) <= int(tab[i+1][1]):
            print(int(tab[i][1]), "<=", int(tab[i+1][1]))
        else:
            raise Exception("Test nie przeszedl")

if __name__ == "__main__":
    data_set1 = DF(1000)
    data_set1.set_data()
    tab = data_set1.get_data()
    test_sorted_list(tab)
    print(tab)

    # print(data_set1)