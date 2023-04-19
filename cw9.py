# # # #import numpy as np
# # # #a = np.array([[1,2,3],[4,5,6]])
# # # ## print(a.shape)
# # # ## print(a.size)
# # # ## print(type(a))
# # # #b = a.reshape(3,2)
# # # #print(b)

# # # import numpy as np
# # # a = np.array([[0,1],[2,3]])
# # # b = np.resize(a,(2,3))

# import numpy as np
# a = np.arange(24)
# print(a.ndim)

# b = a.reshape(2,4,3)
# print(b)
# print(b.ndim)

# import numpy as np
# x = np.array([1,2,3,4,5], dtype = np.int8)
# print(x.itemsize)

# import numpy as np
# x = np.empty([3,2], dtype = int)
# print(x)
# x = np.zeros([2,2], dtype = int)
# x = np.ones([2,2], dtype = int)
# 
# x = [1,2,3]
# a = np.asarray(x)
# b = list(a)
# print(a)
# print(type(a))
# print(type(b))

# x = np.linspace(10,20,5)
# print(x)

# a = [[0,1],[0,5]]
# print(np.sum(a))
# print(np.sum(a,axis=0))
# print(np.sum(a,axis=1))

# a = np.array([[0,1,2],[2,3,4]])
# b = np.array([4,5,6])
# print(np.add(a,b))
# print(np.subtract(a,b))
# print(np.multiply(a,b))
# print(np.divide(a,b))
# print(np.dot(a,b))

import numpy as np
# a = np.array([[3,7,5],[8,4,3],[2,4,9]])
# print(np.amin(a,axis=1))
# print(np.amin(a,axis=0))
# print(np.amax(a,axis=1))
# print(np.amax(a,axis=0))

# a = np.array([[3,7,5],[8,4,3],[2,4,9]])
# print(np.ptp(a))
# print(np.ptp(a,axis=1))
# print(np.ptp(a,axis=0))


# a = np.array([[30,65,70],[80,95,10],[50,90,60]])
# print(np.median(a))
# print(np.median(a,axis=1))
# print(np.median(a,axis=0))

print(np.std([1,2,3,4]))
