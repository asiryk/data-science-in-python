# -*- coding: utf-8 -*-
"""1.1-nupy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ypu57fBXnlXUmUNm4mN0vxu1sdIGF_ew

# Nupmy. The library for numeric computing in Python

Numpy is the fundamental package for numeric computing with Python.  
It provides powerful ways to create, store, and/or manipulate data, which makes it able to seamlessly and speedily integrate with a wide variety of databases. This is also the foundation that Pandas is built on, which is a high-performance data-centric package that we will learn later in the course.
"""

import numpy as np
import math
from PIL import Image
from IPython.display import display

"""## Array Creation"""

# Arrays are displayed as a list or list of lists and can be created through list as well. When creating an
# array, we pass in a list as an argument in numpy array
a = np.array([1, 2, 3])
print(a)

# If we pass in a list of lists in numpy array, we create a multi-dimensional array, for instance, a matrix
b = np.array([[1,2,3],[4,5,6]])
print(b)

# We can print the number of dimensions of a list using the ndim attribute
print('number of dimensions: ' + str(b.ndim))

# We can print out the length of each dimension by calling the shape attribute, which returns a tuple
print('length of each dimension: ' + str(b.shape))

# We can also check the type of items in the array
print('type of items: ' + str(b.dtype))

# Besides integers, floats are also accepted in numpy arrays
print(np.array([2.2, 5, 1.1]).dtype.name)

# Create placeholder array
print(np.zeros((2,3)))
print(np.ones((2,3)))

# We can also generate an array with random numbers
print('\n', np.random.rand(2,3))

# Create an array of every even number from ten (inclusive) to fifty (exclusive)
print('\n', np.arange(10, 50, 2))

# Generate a sequence of floats. The third argument is the total number of items you want to generate
print('\n', np.linspace( 0, 2, 15 )) # 15 numbers from 0 (inclusive) to 2 (inclusive)

"""## Array Operations

We can do many things on arrays, such as mathematical manipulation (addition, subtraction, square,
exponents) as well as use boolean arrays, which are binary values. We can also do matrix manipulation such
as product, transpose, inverse, and so forth.
"""

# Arithmetic operators on array apply elementwise.

# Let's create a couple of arrays
a = np.array([10,20,30,40])
b = np.array([1, 2, 3, 4])

# Now let's look at a minus b
print(a - b)

# And let's look at a times b
print(a * b)

# Another useful and important manipulation is the boolean array. We can apply an operator on an array, and a
# boolean array will be returned for any element in the original.
print(a > 20)

# Here's another example, we could use the modulus operator to check numbers in an array to see if they are even.
print(a / 10 % 2 == 0)

# Besides elementwise manipulation, it is important to know that numpy supports matrix manipulation.
# Let's look at matrix product. If we want to do elementwise product, we use the "*" sign.
A = np.array([[1,1],[0,1]])
B = np.array([[2,0],[3,4]])
print(A * B)

# If we want to do matrix product, we use the "@" sign or use the dot function.
print('\n', A @ B)

# A few more linear algebra concepts are worth layering in here. You might recall that the product of two
# matrices is only plausible when the inner dimensions of the two matrices are the same. The dimensions refer
# to the number of elements both horizontally and vertically in the rendered matricies you've seen here. We
# can use numpy to quickly see the shape of a matrix:
print(A.shape)
print(A.shape == B.shape)

# Numpy arrays have many interesting aggregation functions on them, such as  sum(), max(), min(), and mean()
a = np.array([[ 8.1, 10.2, 12.1], [14.4, 16.2, 18.3]])
print('sum: ' + str(a.sum()))
print('max: ' + str(a.max()))
print('min: ' + str(a.min()))
print('mean: ' + str(a.mean()))

# For two dimensional arrays, we can do the same thing for each row or column
# let's create an array with 15 elements, ranging from 1 to 15, 
# with a dimension of 3X5
b = np.arange(1,16,1).reshape(3,5)
print(b)
# Now, we often think about two dimensional arrays being made up of rows and columns, but you can also think
# of these arrays as just a giant ordered list of numbers, and the *shape* of the array, the number of rows
# and columns, is just an abstraction that we have for a particular purpose. Actually, this is exactly how
# basic images are stored in computer environments.

# Let's look at the image
im = Image.open('datasets/chris.tiff')
display(im)

# Now, we can conver this PIL image to a numpy array
array = np.array(im)
print(array.shape)
print(array)

# Here we see that we have a 200x200 array and that the values are all uint8. For black and white
# images black is stored as 0 and white is stored as 255. So if we just wanted to invert this image we could
# use the numpy array to do so

# Let's create an array the same shape
mask=np.full(array.shape,255)

modified_array = array - mask
modified_array = modified_array * -1

# And as a last step, let's tell numpy to set the value of the datatype correctly
modified_array = modified_array.astype(np.uint8)

# And lastly, lets display this new array. We do this by using the fromarray() function in the python
# imaging library to convert the numpy array into an object jupyter can render
display(Image.fromarray(modified_array))

# Cool. We could just think of this as a giant array of bytes, and that the shape was an abstraction?
# Well, we could just decide to reshape the array and still try and render it.
# PIL is interpreting the individual rows as lines, so we can change the number of lines
# and columns if we want to. What do you think that would look like?
reshaped = np.reshape(modified_array, (100, 400))
print('Original array shape: ', modified_array.shape)
print('Reshaped array shape: ', reshaped.shape)
display(Image.fromarray(reshaped))
# By reshaping the array to be only 100 rows high but 400 columns we've essentially doubled the image
# BY TAKING EVERY OTHER LINE AND STACKING THEM OUT IN WIDTH.

"""## Indexing, Slicing and Iterating

Indexing, slicing and iterating are extremely important for data manipulation and analysis because these
techinques allow us to select data based on conditions, and copy or update data.

### Indexing
"""

# First we are going to look at integer indexing. A one-dimensional array, works in similar ways as a list -
# To get an element in a one-dimensional array, we simply use the offset index.
a = np.array([1,3,5,7])
print(a[2] == 5)

# For multidimensional array, we need to use integer array indexing, let's create a new multidimensional array
a = np.array([[1,2], [3, 4], [5, 6]])
print(a[1,1])

# If we want to get multiple elements 
# for example, 1, 4, and 6 and put them into a one-dimensional array
# we can enter the indices directly into an array function
print(np.array([a[0, 0], a[1, 1], a[2, 1]]))

# We can also do that by using another form of array indexing, which essentiall "zips" the first list and the
# second list up
print(a[[0, 1, 2], [0, 1, 1]])

"""### Boolean Indexing"""

# Boolean indexing allows us to select arbitrary elements based on conditions.
# For example, in the matrix we just talked about we want to find elements that are greater than 5
# so we set up a conditon a > 5
a = np.array([[1,2], [3, 4], [5, 6]])
print(a > 5)
# This returns a boolean array showing that if the value at the corresponding index is greater than 5

# We can then place this array of booleans like a mask over the original array to return a one-dimensional 
# array relating to the true values.
print(a[a > 5])

# As we will see, this functionality is essential in the pandas toolkit which is the bulk of this course

"""### Slicing
Slicing is a way to create a sub-array based on the original array.
"""

# For one-dimensional arrays, slicing works in similar ways to a list.
# To slice, we use the : sign. For instance, if we put :3 in the indexing
# brackets, we get elements from index 0 to index 3 (excluding index 3)
a = np.array([0,1,2,3,4,5])
print(a[:3]) # From the first element to third (excluding)
print(a[:]) # The whole original array shallow copy

# For multi-dimensional arrays, it works similarly, lets see an example
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

# First, if we put one argument in the array, for example a[:2] then we would get all the elements from the 
# first (0th) and second row (1th)
a[:2]

# If we add another argument to the array, for example a[:2, 1:3], we get the first two rows but then the
# second and third column values only
print(a[:2, 1:3]) # a[rows_slice, columns_slice]

"""## Trying Numpy with Datasets"""

# To load a dataset in Numpy, we can use the genfromtxt() function. We can specify data file name, delimiter
# (which is optional but often used), and number of rows to skip if we have a header row, hence it is 1 here

# The genfromtxt() function has a parameter called dtype for specifying data types of each column this
# parameter is optional. Without specifying the types, all types will be casted the same to the more
# general/precise type

wines = np.genfromtxt("datasets/winequality-red.csv", delimiter=";", skip_header=1)
print(wines)

# All rows combined but only the first column from them would be
print("one integer 0 for slicing: ", wines[:, 0])
# But if we wanted the same values but wanted to preserve that they sit in their own rows we would write
print("0 to 1 for slicing: \n", wines[:, 0:1])

# What if we want several non-consecutive columns? We can place the indices of the columns that we want into
# an array and pass the array as the second argument. Here's an example
print(wines[:, [0,2,4]])

# We can also do some basic summarization of this dataset. For example, if we want to find out the average
# quality of red wine, we can select the quality column. We could do this in a couple of ways, but the most
# appropriate is to use the -1 value for the index, as negative numbers mean slicing from the back of the
# list. We can then call the aggregation functions on this data.
print(wines[:,-1].mean())

# We can specify data field names when using genfromtxt() to loads CSV data. Also, we can have numpy try and
# infer the type of a column by setting the dtype parameter to None
names = ('Serial No','GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 
         'LOR','CGPA','Research', 'Chance of Admit')
graduate_admission = np.genfromtxt('datasets/Admission_Predict.csv', names=names, 
                                   delimiter=',', skip_header=1, dtype=None)
print(graduate_admission[-1])

# Notice that the resulting array is actually a one-dimensional array with 400 tuples
print(graduate_admission.shape)

# We can retrieve a column from the array using the column's name for example, let's get the CGPA column and
# only the first five values.
graduate_admission['CGPA'][0:5]

# Recall boolean masking. We can use this to find out how many students have had research experience by
# creating a boolean mask and passing it to the array indexing operator
print(len(graduate_admission[graduate_admission['Research'] == 1]))

# Since we have the data field chance of admission, which ranges from 0 to 1, we can try to see if students
# with high chance of admission (>0.8) on average have higher GRE score than those with lower chance of
# admission (<0.4)

# So first we use boolean masking to pull out only those students we are interested in based on their chance
# of admission, then we pull out only their GPA scores, then we print the mean values.
print(graduate_admission[graduate_admission['Chance_of_Admit'] > 0.8]['GRE_Score'].mean())
print(graduate_admission[graduate_admission['Chance_of_Admit'] < 0.4]['GRE_Score'].mean())

# Take a moment to reflect here, do you understand what is happening in these calls?

# When we do the boolean masking we are left with an array with tuples in it still, and numpy holds underneath
# this a list of the columns we specified and their name and indexes
print((graduate_admission[graduate_admission['Chance_of_Admit'] > 0.8])[:5])

# Let's also do this with GPA
print(graduate_admission[graduate_admission['Chance_of_Admit'] > 0.8]['CGPA'].mean())
print(graduate_admission[graduate_admission['Chance_of_Admit'] < 0.4]['CGPA'].mean())