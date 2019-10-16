def replace_negative(listnum):
    for i in range(len(listnum)):
        if(listnum[i]<0):
          listnum[i]=abs(listnum[i])
    return listnum


original=[8,-20,-10,0,-55,-777]   
print(replace_negative(original)) 

input_list=[1,2,3,4,4,5,6,7,7] 
output_list=[item for item in input_list if item % 2==0] 
print(output_list)   