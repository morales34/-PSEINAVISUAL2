
#Introducción a Numpy

import Numpy as np # linear algebra
import Pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

[1,2,3]

[[ 1, 2, 3],[ 4, 5, 6]]

a = np.array([1, 2, 3])
b = np.array([(1,2,3), (4,5,6)])

print("a: ",a)
print("b: ",b)

# a = np.array(1,2,3,4) # WRONG!!!

a = np.array([1, 2, 3])
b = np.array([(1,2,3), (4,5,6)])

#Return Contents
print('a=')
print(a)
print("a's ndim {}".format(a.ndim))
print("a's shape {}".format(a.shape))
print("a's size {}".format(a.size))
print("a's dtype {}".format(a.dtype))
print("a's itemsize {}".format(a.itemsize))

print('')

print('b=')
print(b)
print("b's ndim {}".format(b.ndim))
print("b's shape {}".format(b.shape))
print("b's size {}".format(b.size))
print("b's dtype {}".format(b.dtype))
print("b's itemsize {}".format(b.itemsize))

c = np.array( [ [1,2], [3,4] ], dtype=complex )
c

a = np.zeros((2,3))
print('np.zeros((2,3)= \n{}\n'.format(a))

b = np.ones((2,3))
print('np.ones((2,3))= \n{}\n'.format(b))

c = np.empty((2,3))
print('np.empty((2,3))= \n{}\n'.format(c))

d = np.arange(1, 2, 0.3)
print('np.arange(1, 2, 0.3)= \n{}\n'.format(d))

e = np.linspace(1, 2, 7)
print('np.linspace(1, 2, 7)= \n{}\n'.format(e))

f = np.random.random((2,3))
print('np.random.random((2,3))= \n{}\n'.format(f))

#Shape and operation

zero_line = np.zeros((1,3))
one_column = np.ones((3,1))
print("zero_line = \n{}\n".format(zero_line))
print("one_column = \n{}\n".format(one_column))

a = np.array([(1,2,3), (4,5,6)])
b = np.arange(11, 20)
print("a = \n{}\n".format(a))
print("b = \n{}\n".format(b))

b = b.reshape(3, -1)
print("b.reshape(3, -1) = \n{}\n".format(b))

b.reshape(3, -1)

c = np.vstack((a, b, zero_line))
print("c = np.vstack((a,b, zero_line)) = \n{}\n".format(c))

a = a.reshape(3, 2)
print("a.reshape(3, 2) = \n{}\n".format(a))

d = np.hstack((a, b, one_column))
print("d = np.hstack((a,b, one_column)) = \n{}\n".format(d))

e = np.hsplit(d, 3) # Split a into 3
print("e = np.hsplit(d, 3) = \n{}\n".format(e))
print("e[1] = \n{}\n".format(e[1]))

f = np.hsplit(d, (1, 3)) # # Split a after the 1st and the 3rd column
print("f = np.hsplit(d, (1, 3)) = \n{}\n".format(f))

g = np.vsplit(d, 3)
print("np.hsplit(d, 2) = \n{}\n".format(g))

# np.vsplit(d, 2) # ValueError: array split does not result in an equal division


#index
base_data = np.arange(100, 200)
print("base_data\n={}\n".format(base_data))

print("base_data[10] = {}\n".format(base_data[10]))

every_five = np.arange(0, 100, 5)
print("base_data[every_five] = \n{}\n".format(
    base_data[every_five]))

every_five = np.arange(0, 100, 5)
print("base_data[every_five] = \n{}\n".format(
    base_data[every_five]))

base_data2 = base_data.reshape(10, -1)
print("base_data2 = np.reshape(base_data, (10, -1)) = \n{}\n".format(base_data2))

print("base_data2[2] = \n{}\n".format(base_data2[2]))
print("base_data2[2, 3] = \n{}\n".format(base_data2[2, 3]))
print("base_data2[-1, -1] = \n{}\n".format(base_data2[-1, -1]))

print("base_data2[2, :]] = \n{}\n".format(base_data2[2, :]))
print("base_data2[:, 3]] = \n{}\n".format(base_data2[:, 3]))
print("base_data2[2:5, 2:4]] = \n{}\n".format(base_data2[2:5, 2:4]))

#Mathematics

base_data = (np.random.random((5, 5)) - 0.5) * 100
print("base_data = \n{}\n".format(base_data))

print("np.amin(base_data) = {}".format(np.amin(base_data)))
print("np.amax(base_data) = {}".format(np.amax(base_data)))
print("np.average(base_data) = {}".format(np.average(base_data)))
print("np.sum(base_data) = {}".format(np.sum(base_data)))
print("np.sin(base_data) = \n{}".format(np.sin(base_data)))

arr = np.arange(1,20)
arr = arr * arr              #Multiplies each element by itself 
print("Multpiles: ",arr)
arr = arr - arr              #Subtracts each element from itself
print("Substracts: ",arr)
arr = np.arange(1,20)
arr = arr + arr              #Adds each element to itself
print("Add: ",arr)
arr = arr / arr              #Divides each element by itself
print("Divide: ",arr)
arr = np.arange(1,20)
arr = arr + 50
print("Add +50: ",arr)

print("Sqrt: ",np.sqrt(arr))#Returns the square root of each element 
print("Exp: ",np.exp(arr))     #Returns the exponentials of each element
print("Sin: ",np.sin(arr))     #Returns the sin of each element
print("Cos: ",np.cos(arr))     #Returns the cosine of each element
print("Log: ",np.log(arr))     #Returns the logarithm of each element
print("Sum: ",np.sum(arr))     #Returns the sum total of elements in the array
print("Std: ",np.std(arr))     #Returns the standard deviation of in the array

#Matrix
base_data = np.floor((np.random.random((5, 5)) - 0.5) * 100)
print("base_data = \n{}\n".format(base_data))

print("base_data.T = \n{}\n".format(base_data.T))
print("base_data.transpose() = \n{}\n".format(base_data.transpose()))

matrix_one = np.ones((5, 5))
print("matrix_one = \n{}\n".format(matrix_one))

minus_one = np.dot(matrix_one, -1)
print("minus_one = \n{}\n".format(minus_one))

print("np.dot(base_data, minus_one) = \n{}\n".format(
    np.dot(base_data, minus_one)))

#Random Number

print("random: {}\n".format(np.random.random(20)));

print("rand: {}\n".format(np.random.rand(3, 4)));

print("randint: {}\n".format(np.random.randint(0, 100, 20)));

print("permutation: {}\n".format(np.random.permutation(np.arange(20))));





