#Eftihia Kiafa AM:3003

import sys 
from heapq import heapify, heappush, heappop
import ast
import heapq
import math


global dict_data
dict_data=dict()
global leaves_data
leaves_data=dict()
global root_node_id
global points
points=[]
k=0



def bfs_init(q,root_node_id):
   
    heap=[]
    result=[]
    heapify(heap)   
    
    for i in dict_data[root_node_id][1]:
        heapq.heappush(heap,i) 
    
    result=bfs_next(q,heap)
    return result






def bfs_next(q,heap):

    onn=[] # list for sorted by distance,distance of objects and query

    on=[] #list for dictances between q's and mbr's
    seen_leaves=[]
    seen_nodes=[]
    while len(heap)!=0:
        e=heapq.heappop(heap)
        #node       
        if root_node_id>=e[0] and dict_data[e[0]][0]==1 and e[0] not in seen_nodes : 
            seen_nodes.append(e[0])
            for i in dict_data[e[0]][1]:                   
                heapq.heappush(heap,i)

                
                   
        #leaves        
        elif root_node_id>=e[0] and dict_data[e[0]][0]==0 and e[0] not in seen_leaves:
            seen_leaves.append(e[0])
            o=dict_data[e[0]]
            for i in o[1]: 
                heapq.heappush(heap,i)

        elif leaves_data[e[0]][0]==-1 and leaves_data[e[0]][1]==e[1]:

            on.append([dist(q,e[1]),e[0]])
    heapq.heapify(on)
    for i in heapq.nsmallest(k,on):
        onn.append(i[1])
    return onn[:k]
        

def dist(q,mbr):
    
    if mbr==[]:
        distance=math.inf
        return distance
    
    #for x
    if float(q[0])<float(mbr[0]):
        dx=float(mbr[0])-float(q[0])
    elif float(q[0])>float(mbr[1]):
        dx=float(q[0])-float(mbr[1])
    else:
        dx=0

    #for y
    if float(q[1])<float(mbr[2]):
        dy=float(mbr[2])-float(q[1])
    elif float(q[1])>float(mbr[3]):
        dy=float(q[1])-float(mbr[3])
    else:
        dy=0

    distance=math.sqrt(dx**2+ dy**2)
    return distance



def main():      
        rtree=sys.argv[1]
        nnQueries=sys.argv[2]
        global k
        k=sys.argv[3]
        k=int(k)
        with open(nnQueries,mode='r') as nqueries,open(rtree,mode='r') as R:
            for line in nqueries:
                line=line.split(' ')
                points.append((float(line[0]),float(line[1])))
            for line in R:
                cell=ast.literal_eval(line)
                dict_data[cell[1]]=[cell[0],cell[2]]
            #fill leaves_data dictionary with objects in leaves
            for i in dict_data:
                
                if dict_data[i][0]==0:
                    for j in dict_data[i][1]:
                      leaves_data[j[0]]=[-1,j[1]]
            root=list(dict_data.keys())[-1]
        
            global root_node_id
            root_node_id=root 
            count=-1 
            for q in points:
                count+=1  
                l=str(bfs_init(q,root_node_id))
                print(str(count)+': '+l[1:-1])








if __name__ == '__main__':
  
   main()
