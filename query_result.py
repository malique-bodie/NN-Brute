from collections import namedtuple
from operator import truediv
import pandas as pd
import numpy as np
import heapq 

#Basic Result structure that holds the distance and id of a result
basic_result = namedtuple('basic_result', ['dist', 'id'], defaults=[-1000000000,-1])

class query_result:

    def __init__(self, K):
        self.target = None
        self.results = []
        self.k = K
        #initializes results array with K basic_results
        for i in range(K):
            heapq.heappush(self.results, basic_result())

    def set_target(self,query):
        self.target = query
    
    def get_target(self):
        return self.target

    def set_result(self, i, VID, dist):
        self.results[i].dist = dist
        self.results[i].id = VID

    def sort(self):
        r = [heapq.heappop(self.results) for i in range(self.k)]
        return r[::-1]


    def add_point(self, index, dist):
        if(dist > self.results[0].dist or (dist == self.results[0].dist and index < self.results[0].id)):
            heapq.heapreplace(self.results, basic_result(dist,index))
            return True
        else:
            return False

    def reset(self):
        self.results = [] #making new array every time is mad slow
        for i in range(self.k):
            heapq.heappush(self.results, basic_result())



    




