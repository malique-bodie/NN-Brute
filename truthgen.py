import pandas as pd
import numpy as np

from query_result import query_result
from scipy.spatial import distance

class truthset:

    def load_truth(self, query_txt,index_txt):
        queries = np.loadtxt(query_txt, delimiter=' ')
        vectors = np.loadtxt(index_txt, delimiter=' ')
        return(queries,vectors)


    def write_truth_file(self, results):
        np.savetxt(fname='truth_file.txt',X=results, delimiter=' ')

    def compute_distance(self, query, vector):
        return distance.euclidean(query,vector)


    

    def generate_truth(self, K):
        q,v = self.load_truth("./query_vec.txt", "./index_vec.txt")
        #check query and vector dimensions are the same
        if(q.shape[1] != v.shape[1]):
            print("query and vector have different dimensions")
            exit(1)
        #don't get it
        truthset = np.zeros((q.shape[0],K))
        distset = np.zeros((q.shape[0],K))
        #initialize query result max dist and id in results array 
        query = query_result(K)
        #loop through all of the queries
        for i in range(q.shape[0]):
            # set target query --> need to instantiate what the query is somewhere
            query.set_target(q[i]) 
            #loop through vectors 
            for j in range(v.shape[0]):
                #calculate distance | multiplying by -1 because python uses min heap
                dist = self.compute_distance(query.get_target(),v[j]) *(-1)
                #add distane to query struct
                query.add_point(j,dist)
            #sort and return results
            results = query.sort()
            for k in range(K):
                print(results[k].id)
                truthset[i][k] = results[k].id
                distset[i][k] = results[k].dist * (-1) #multiply by negative one to reset the distance
            #reset query results
            query.reset()

        self.write_truth_file(truthset)
        
