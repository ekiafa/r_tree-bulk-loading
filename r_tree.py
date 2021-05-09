#Eftihia Kiafa AM:3003


import pymorton
import sys
import csv
import node
import math

global no_of_rectangles
count=-1
nodes=0
child_no=-1
global level
level=-1
global tree
tree=[]
global n
n=0

def find_mbr(mbr):

        x_array=[]
        y_array=[]

        for i in mbr:
          
          x_array.append(float(i[0]))
          x_array.append(float(i[1]))
          y_array.append(float(i[2]))
          y_array.append(float(i[3]))
        
        x_low=min(x_array)
        x_high=max(x_array)
        y_low=min(y_array)
        y_high=max(y_array)

        return [float(x_low), float(x_high), float(y_low), float(y_high)]


def minimum_bounding_rectangle(coords_array):
        
        x_array=[]
        y_array=[]
        for i in coords_array:
          i=i.split(",")
          x_array.append(float(i[0]))
          y_array.append(float(i[1]))
        x_low=min(x_array)
        x_high=max(x_array)
        y_low=min(y_array)
        y_high=max(y_array)
        
        return [float(x_low), float(x_high), float(y_low), float(y_high)]

def divide_chunks(lst, n):
    
    
    global tree
    global child_no
    global lst2
    global count
    #this is for leaves slice not for nodes
    lst2=[]
    if int(len(lst)/20)==absolute:
      
      for i in range(0, len(lst), n):
          if (len(lst[i+n:i + 2*n])<8 and lst[i+n:i + 2*n]!=[]):
            n=20-(8-len(lst[i+n:i + 2*n]))
          if i== len(lst)-len(lst)%20 and len(lst)%20!=0 :
            lst2=lst[-8:]
          else:
            lst2=lst[i:i + n] 
          count+=1
          yield lst2
          tree.append([0,count,lst[i:i + n]])

    else:
      #this is for nodes

      
      lst2=[]
      for i in range(0, len(lst),n):
          if (len(lst[i+n:i + 2*n])<8 and lst[i+n:i + 2*n]!=[]):
            n=20-(8-len(lst[i+n:i + 2*n]))

          
          count+=1     
          if i== len(lst)-len(lst)%20 and len(lst)%20!=0 :
            lst2=lst[-8:]
          else:
            lst2=lst[i:i + n] 
          recs=list()#this is child list for each node
          for k in lst2:
           
            child_no+=1
            k_mbrs=[]#this is for node mbrs
            for r in k:
              k_mbrs.append(r[1])
            #collect mbrs and child_no for the list
            recs.append([child_no,find_mbr(k_mbrs)])
            
          lst[i:i + n]=recs
          yield lst[i:i + n]
          tree.append([1,count,recs])
          

      
   
  

      


def construct(no_of_rectangles,rectangles):
        
        global leaves
        global nodes
        global level
        #if no_of_rectangles<=1 then we can't bulk load anymore and we corrupt the recursion
        if no_of_rectangles >1:
          level+=1
          max_capacity=20
          no_of_nodes=math.ceil(no_of_rectangles/max_capacity)
          print(str(no_of_nodes)+" nodes at level "+str(level))
          leaves=divide_chunks(rectangles,max_capacity)
          leaves=list(leaves)          
          no_of_rectangles=len(leaves)
          construct(no_of_rectangles,leaves)
        

def main():      
       
        coords_file=sys.argv[1]
        offsets_file=sys.argv[2]
        coords_count=0
        with open(coords_file,mode='r') as coords,open(offsets_file,mode='r')as offsets,open('Rtree.txt',mode='w',encoding='UTF8') as rtree:
          
          coords_line=coords.readline()
          offsets_line=offsets.readline()
          global mbr_centres 
          global rectangle_objects
          mbr_centres=dict()
          rectangle_objects=dict()
          while offsets_line and coords_line:
              id=offsets_line.split(",")[0] 
              start=offsets_line.split(",")[1]              
              finish=offsets_line.split(",")[2]

              coords_array=[]
              while coords_count >= float(start) and float(finish) >= coords_count:
                coords_array.append(coords_line)                
                coords_line=coords.readline()
                coords_count+=1
              #calculate minimum bounding rectangle and get its higher and lower point
              mbr=minimum_bounding_rectangle(coords_array)
              #reshape of mbr centre
              x=float(float(mbr[0])+float(mbr[1]))/2
              y=float(float(mbr[2])+float(mbr[3]))/2
              #convert mbr centre to z-order value
              centre=pymorton.interleave_latlng(y,x)
              
              #collect all centres in dictionary by object id   
              mbr_centres[id]=int(centre)        
              rectangle_objects[id]=mbr
              offsets_line=offsets.readline()
          #sorting of reshaped mbr's z-order value array
          mbr_centres=sorted(mbr_centres, key=lambda mbr : mbr_centres[mbr])
          #convert array of strings to array of ints
          m_c = [int(i) for i in mbr_centres]
          
          rectangle_objects=[rectangle_objects[k] for k in mbr_centres]
          
          rectangles=list(map(list, zip(m_c, rectangle_objects)))
          global absolute
          absolute=int(len(rectangle_objects)/20)
          
          #beginning of tree construction
          construct(len(rectangle_objects),rectangles)  
          for i in tree:
            #change stdout for printing in file and not in terminal
            sys.stdout = rtree
            print(i)
          rtree.close()
                  
              


        
              
            
       


if __name__ == '__main__':
  
   main()
