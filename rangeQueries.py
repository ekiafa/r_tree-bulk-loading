#Eftihia Kiafa AM:3003

import sys
import ast


global dict_data
dict_data=dict()
global leav_in
leav_in=[]

global root_node_id
def query(node_id,window):
        global leav_in

        
        if node_id== root_node_id:
            leav_in=[]
        if dict_data[node_id][0]==1: #node
            for i in dict_data[node_id][1]:
                if window_and_mbr_intersection(i[1],window)==True:                
                   query(i[0],window)
                    

        else: #leaves
            
        
            for i in dict_data[node_id][1]: 
                if window_and_mbr_intersection(i[1],window)==True:
                    leav_in.append(i[0])
        

        return('('+(str(len(leav_in))+')'+': '+str(leav_in)[1:-1])   )
        

def window_and_mbr_intersection(mbr,window):
    window[0]=float(window[0])
    window[1]=float(window[1])
    window[2]=float(window[2])
    window[3]=float(window[3])
    window_x_low=window[0]
    window_x_high=window[1]
    window_y_low=window[2]
    window_y_high=window[3]
    mbr_x_low=mbr[0]
    mbr_x_high=mbr[1]
    mbr_y_low=mbr[2]
    mbr_y_high=mbr[3]

    # At least one  point intersecting.   
    
    if ((window_x_high < mbr_x_low) or (window_x_low > mbr_x_high)):
        return False

    elif  ((window_y_high < mbr_y_low) or (window_y_low > mbr_y_high)):

        return False
    
    # The MBR of the rectangle we examine must be inside of the MBR of the window.   

    elif ((window_x_high >= mbr_x_high) and (window_x_low <= mbr_x_low)) and ((window_y_low <= mbr_y_low) and (window_y_high >= mbr_y_high)):

        return True

    # Exactly the opposite from the previous. We can change the positions in the comparisons.
    elif((mbr_x_high >= window_x_high) and (mbr_x_low <= window_x_low)) and ((mbr_y_low <= window_y_low) and (mbr_y_high >= window_y_high)):

        return True
    return True         



#convert window query from <x_low> <y_low> <x_high> <y_high> to <x_low> <x_high><y_low><y_high>
def fix_windows(windows):
    fix_windows=[]
    for i in windows:
        
        fix_windows.append([i[0],i[2],i[1],i[3]])
    
    return fix_windows

def main():      
        windows=[]
        rtree=sys.argv[1]
        rQueries=sys.argv[2]
        global dict_data
        dict_data=dict()
        with open(rtree,mode='r') as R,open(rQueries,mode='r') as queries:
            leav_in=[]
            #get Rtree and root_node_id
            for line in R:
                cell=ast.literal_eval(line)
                dict_data[cell[1]]=[cell[0],cell[2]]
            root=list(dict_data.keys())[-1]
            global root_node_id
            root_node_id=root   
            #get windows boundaries and call range searching method         
            for line in queries:
                windows.append(line.split(' '))
            windows=fix_windows(windows) 
            count=-1
            for i in windows:
             count+=1
             print(count,query(root_node_id,i))

            


if __name__ == '__main__':
  
   main()
