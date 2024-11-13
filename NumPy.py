# no =("my name is divine")
# print(no)



# import numpy as np
# a = np.array([1,2,3])
# print(a) 


# import numpy as np
# arr = np.array([1,2,3,4,5])
# print(arr)
# print(type(arr))

# import numpy as np
# array_a = np.array([1, 2, 3, 4])
# print(array_a)




# import numpy as np
# a = np.array([1, 2,])



#create an array
# arr = np.arange(9)
# print("Original array:")
# print(arr)

# result = np.split(arr, 3)
# print("\nsplit array into three equal parts:")
# for i, sub_array in enumerate(result):
#    print(f"sub_array {i+1}:")
#    print(sub_array)





######    NUMPY   ########

# import numpy as np
# a = np.array([1, 2, 3, 4])
# print(a)

##

# import numpy as np 
# array_a = np.array([1, 2, 3, 4, "Divine" ])  ### numpy array are homogenous data type ,
# print(array_a)
# print(array_a.shape)



## multi dimensional array#########
# import numpy as np
# array_b = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 8]])  ##### the first value represent the row and the second represent the clumn###
# print(array_b)
# print(array_b.shape)


#### 3*3 numpy array shape
# import numpy as np
# seq_a = [1, 2, 3]
# seq_b = [4, 5, 6]
# seq_c = [7, 8, 9]
# x = np.array([seq_a,seq_b,seq_c,seq_d])
# print(x.shape)

# import numpy as np
# seq_a = [1, 2, 3]
# seq_b = [4, 5, 6]
# seq_c = [7, 8, 9]
# x = np.array([seq_a,seq_b,seq_c])
# print(x.shape)


#### Difference between python list and numpy array: 

# python list##
# a = [1, 2, 3, "divine", "favour"]
# print(a)

# numpy array##
# import numpy as np
# a = np.array([1, 2, 3, "divine", "favour"])
# print(a)



########## Numpy array shape ######### Numpy array size is determined by the product of the rows and column ####
# import numpy as np
# arrray_a = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
# print(arrray_a.size)


#### Numpy array indexing #####

# import numpy as np
# arrray_x = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
# print(arrray_x[:,2])

## 
# import numpy as np
# x = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
# print(x[0], (x[2]))    #### when calling a specific row by calling the variable ##



## Reshaping the no of row and column in numpy array ###
# import numpy as np
# array_a = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
# array_y = array_a.reshape(4,2)
# print(array_y)

#### Tranpose in numpy array ### simply means changing the rows to ccolumn and vice versal###
# import numpy as np
# array_a = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
# array_y = array_a.T
# print(array_y)

### Returning the transpose to it's original pattern ####
# import numpy as np
# array_a = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
# array_y = array_a.T
# print(array_y.T)  ### it can return to it's originaL pattern by adding '.T ' to the print statement ###


###### Default array ##########
     ## dtype###
# import numpy as np
# arr = np. array([1, 2, 3, 4], dtype=float)  ## dtype argument is used to change to another data type which is float in this case ##
# print(arr)

    ## zeros value ## You can have zero value by passing "np.zeros" as an argument ##
# import numpy as np
# array_b = np.zeros((3,5))
# print(array_b)

    ## ones value###
# import numpy as np
# array_c = np.ones((3,5))
# print(array_c)


   ## Getting numbers as value apart from "1 and 0" 
# import numpy as np
# b = np.full((3,5),9)  ## To print any random value , you can pass two argument , "the first argument is for the pattern while the second argument is for the numbers you want assign to it by using "np.full"######"
# print(b)

   ## Getting random values ##
# import numpy as np
# b = np.random.random((3,5)) 
# print(b)
    
