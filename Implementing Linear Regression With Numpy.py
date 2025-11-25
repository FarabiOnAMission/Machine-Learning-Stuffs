import numpy as np
import matplotlib.pyplot as plt

#Making Data
# X=Hours Studied , Y=Test Score
X = np.array([1,2,3,4,5])
y = np.array([92,93,96,97,98])

plt.scatter(X,y)
plt.title("Student Performance: ")

m=0
c=0

n=len(X)
learning_rate=0.01

for i in range(1000):
  y_pred=m*X + c

  D_c = (-2/n) * (sum(y-y_pred))
  D_m = (-2/n) * (sum(X*(y-y_pred)))

  m = m - learning_rate * D_m
  c = c - learning_rate * D_c

y_final= m*X + c
plt.plot(X,y_final,color='red')
plt.show()
