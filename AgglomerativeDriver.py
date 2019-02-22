'''
This is a driver program that given an input file, linkage type and number of clusters
 will return a plot of the Agglomerative Clustering of the data. 

Currently it is set-up for 2 dimensions and 5 dimensions
Written by Salvador Gutierrez 
'''


import sys
import matplotlib.pyplot as plt
import numpy as np
import math
import random
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.cluster import AgglomerativeClustering as AC

def xy(line):
    coor = line.split()
    #THIS IS SPECIFIC TO THIS DATASET
    d1 = float(coor[1])
    d2 = float(coor[2])
    return[d1,d2]

def getDendogram(nparr, linkage_type):
    linkage_matrix = linkage(nparr,linkage_type)
    dendogram = dendrogram(linkage_matrix)
    plt.show()

def twoDimension(data, nclusters, linkage_type):
    arrs = []
    for line in data:
        arrs.append(xy(line))

    nparr = np.asarray(arrs)
    #getDendogram(nparr,linkage_type)
    #Agglomerative Clusters
    hc = AC(n_clusters=nclusters, affinity='euclidean',linkage=linkage_type)
    y_hc = hc.fit_predict(nparr)
    print("CLUSTER ZERO:",nparr[y_hc==0])
    print("CLUSTER ONE:",nparr[y_hc==1])
    print("CLUSTER TWO:",nparr[y_hc==2])
    print("CLUSTER THREE:",nparr[y_hc==3])
    
    plt.scatter(nparr[y_hc ==0,0], nparr[y_hc == 0,1], s=100, c='red')
    plt.scatter(nparr[y_hc==1,0], nparr[y_hc == 1,1], s=100, c='black')
    plt.scatter(nparr[y_hc ==2,0], nparr[y_hc == 2,1], s=100, c='blue')
    plt.scatter(nparr[y_hc ==3,0], nparr[y_hc == 3,1], s=100, c='cyan')
    plt.show()

def fiveDimension(data, nclusters,  linkage_type):
    arrs = []
    for line in data:
        coor = line.split()
        d1 = float(coor[0])
        d2 = float(coor[1])
        d3 = float(coor[2])
        d4 = float(coor[3])
        d5 = float(coor[4])
        arrs.append([d1,d2,d3,d4,d5])

    nparr = np.asarray(arrs)
    #getDendogram(nparr, linkage_type)
    hc = AC(n_clusters=nclusters, affinity='euclidean',linkage=linkage_type)
    y_hc = hc.fit_predict(nparr)
    print(nparr[y_hc==0][0,0])
    
    plt.scatter(nparr[y_hc ==0,0], nparr[y_hc == 0,1], s=100, c='red')
    plt.scatter(nparr[y_hc==1,0], nparr[y_hc == 1,1], s=100, c='black')
    plt.scatter(nparr[y_hc ==2,0], nparr[y_hc == 2,1], s=100, c='blue')
    plt.scatter(nparr[y_hc ==3,0], nparr[y_hc == 3,1], s=100, c='cyan')

    plt.show()

        
def main():
    try:
        fileName = sys.argv[1]
        nclusters = int(sys.argv[2])
        linkage_type = sys.argv[3]
        dimensionality = int(sys.argv[4])
    except:
        print("Insufficient or incorrect arguments")
        print("program.py <fileName> <nclusters> <linkage_type> <int dimensionality>")

    f = open(fileName,"r")
    data = f.readlines()
    if (int(dimensionality) == 5):
        fiveDimension(data, nclusters, linkage_type)
    else:
        print("2 DIMS")
        twoDimension(data, nclusters, linkage_type)
    
if __name__=="__main__":
    main()
