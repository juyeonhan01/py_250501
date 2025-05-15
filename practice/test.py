# import numpy as np

# a = np.arange(1)
# b=np.arange(1,10)
# c=np.arange(1,10,3)

# zero = np.zeros(5)
# print(zero)

# ones = np.zeros(5)
# print(ones)

# ran = np.random.randint(1,10,size=5)
# print(ran)

# import numpy as np
# d = np.array([[1, 2, 3], [4, 5, 6]])
# print(d.shape)
# print(d.size)


import numpy as np

# d = np.array([[1,2,3,4,5,6],
#              [7,8,9,10,11,12]])

# d1 = d[:,4:]
# print(d1,d1.shape)

# d1 = d[:,0:3:2]
#d1 = d[:,::2:3] #짝수열만
# print(d1, d1.shape)

a = np.array([[1,2,3],
              [3,2,5]])
b = np.array([[-1,3,5],
             [1,4,2]])
c = np.array([[1,2,3]])
print(a*c)
print(a/c)
print(a-b)