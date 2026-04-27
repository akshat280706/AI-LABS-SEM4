#statistics:
import statistics
data=[28,9,11,2,25]

print("mean: ", statistics.mean(data))
print("median: ", statistics.median(data))
print("mode: ", statistics.mode(data))
print("variance: ", statistics.variance(data))

#math:
import math

print("factorial: ", math.factorial(9))
print("squareRoot: ", math.sqrt(25))
print("2 power 8 is: ", math.pow(2,8))
print("sine: ", math.sin(math.radians(30)))
print("cosine: ", math.cos(math.radians(60)))
print("logarithm: ", math.log(1000))

#numpy:
import numpy as np
arr= np.array([28,9,11,25,2])

print("array: ", arr)
print("mean: ", np.mean(arr))
print("median: ", np.median(arr))

m1=np.array([2,11])
m2=np.array([9,7])
print("dot product: ", np.dot(m1,m2))
print("cross product: ", np.cross(m1,m2))

#scipy:
import numpy as np
from scipy import linalg, integrate, integrate, stats

m1=np.array([[2,9], [11,7]])
print("determinant: ", linalg.det(m1))
print("inverse: ", linalg.inv(m1))

print("\n")
result, error = integrate.quad(lambda x: x**2, 0, 1)
print("Integration :", result)

print("\n")
data2=[28,9,11,25,2]
print("mean: ", stats.tmean(data2))

#pandas:
import pandas as pd

data3={
    "name":["akshat", "khushee", "manya", "devansh"],
    "roll no":[9, 65,66,39],
    "marks": [94, 92, 88, 87]
}

df= pd.DataFrame(data3)
print(df)
print("\n")
print(df.head(2))
print("\n")
print(df.tail(2))
print("\n")
print(df.describe)

#matplotlib:
import matplotlib.pyplot as plt

x= [1,2,3,4,5]
y= [60,70,80,75,85]

plt.plot(x, y)
plt.xlabel("Student Number")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()
print("\n")

plt.bar(x, y)
plt.title("Bar Graph")
plt.show()

print("\n")
plt.hist(y)
plt.title("Histogram")
plt.show()






# #statistics:
# import statistics
# data=[28,9,11,2,25]

# print("mean: ", statistics.mean(data))
# print("median: ", statistics.median(data))
# print("mode: ", statistics.mode(data))
# print("variance: ", statistics.variance(data))

# #math:
# import math

# print("factorial: ", math.factorial(9))
# print("squareRoot: ", math.sqrt(25))
# print("2 power 8 is: ", math.pow(2,8))
# print("sine: ", math.sin(math.radians(30)))
# print("cosine: ", math.cos(math.radians(60)))
# print("logarithm: ", math.log(1000))

# #numpy:
# import numpy as np
# arr= np.array([28,9,11,25,2])

# print("array: ", arr)
# print("mean: ", np.mean(arr))
# print("median: ", np.median(arr))

# m1=np.array([2,11])
# m2=np.array([9,7])
# print("dot product: ", np.dot(m1,m2))
# print("cross product: ", np.cross(m1,m2))

# #scipy:
# import numpy as np
# from scipy import linalg, integrate, integrate, stats

# m1=np.array([[2,9], [11,7]])
# print("determinant: ", linalg.det(m1))
# print("inverse: ", linalg.inv(m1))

# print("\n")
# result, error = integrate.quad(lambda x: x**2, 0, 1)
# print("Integration :", result)

# print("\n")
# data2=[28,9,11,25,2]
# print("mean: ", stats.tmean(data2))

# #pandas:
# import pandas as pd

# data3={
#     "name":["akshat", "khushee", "manya", "devansh"],
#     "roll no":[9, 65,66,39],
#     "marks": [94, 92, 88, 87]
# }

# df= pd.DataFrame(data3)
# print(df)
# print("\n")
# print(df.head(2))
# print("\n")
# print(df.tail(2))
# print("\n")
# print(df.describe)

# #matplotlib:
# import matplotlib.pyplot as plt

# x= [1,2,3,4,5]
# y= [60,70,80,75,85]

# plt.plot(x, y)
# plt.xlabel("Student Number")
# plt.ylabel("Marks")
# plt.title("Student Marks")
# plt.show()
# print("\n")

# plt.bar(x, y)
# plt.title("Bar Graph")
# plt.show()

# print("\n")
# plt.hist(y)
# plt.title("Histogram")
# plt.show()