import numpy as np
import matplotlib.pyplot as plt

# a = np.array([1, 2, 3, 4, 10])
# print(a)

# print("---------------------------------------------------------------------------------")

# b = np.array([[1, 3 , 5, 9], [3, 5 , 10, 13]])
# print(b)

# print("---------------------------------------------------------------------------------")

# print(a[0])

# print("---------------------------------------------------------------------------------")

# print(a[-2:])

# print("---------------------------------------------------------------------------------")

# print(np.arange(0,10,2))

# print("---------------------------------------------------------------------------------")

# print(np.sum(a))

# print("---------------------------------------------------------------------------------")

# print(np.shape(b))

# print("---------------------------------------------------------------------------------")



# x = np.array([1,5,10])
# y = np.array([2,7,9])

# plt.plot(x,y)
# plt.show()

# x = np.array([1,5,10])
# y = np.array([2,7,9])

# plt.plot(x,y, "o")
# plt.show()

# y = np.array([2,3,6,9,15,12])
# plt.plot(y, marker=".")
# plt.show()

# x = np.array([2,3,5,10,20])
# y = np.array([3,6,9,19,30])

# plt.title("Vizuelizacija na podatocite na x i y oska preku matplotlib vo Python")
# plt.xlabel("X")
# plt.ylabel("Y")

# plt.plot(x,y)
# plt.show()

# sizes = np.array([9,3,1,15,20,25])
# x = np.array([2,3,5,10,20,25])
# y = np.array([3,6,9,19,30,35])

# plt.scatter(x,y, s=sizes)

# x = np.array([1,5,7,8,23,32])
# y = np.array([2,4,9,15,21,22])

# plt.scatter(x,y, s=sizes)
# plt.show()

# x = np.array([1,5,7,8,23,32])
# y = np.array([2,4,9,15,21,22])

# plt.subplot(1,2,1)
# plt.scatter(x,y)

# x = np.array([3,4,12,15,16,5])
# y = np.array([0,1,1,1,5,6])

# plt.subplot(1,2,2)
# plt.scatter(x,y)
# plt.show()

# x = np.array(["M","F"])
# y = np.array([25,38])

# plt.bar(x,y)
# plt.show()

# x = np.array([1,1.5,2,2.5,3])
# plt.hist(x)
# plt.show()
 
x = np.array(["M","F"])
y = np.array([25,38])

plt.pie(y, labels=x)
plt.legend(title="Komperacija za M i F", loc="lower left")
plt.show()