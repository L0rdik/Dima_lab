def Print (_i, _j): 
    print(_i, "+", _j) 
     
nums = [2, 4, 8, 1, 6, 9] 
 
for i in nums: 
    for j in nums: 
        if i + j == 10: 
            print(i,j)
