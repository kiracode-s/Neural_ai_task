import numpy as np 
 

X = np.array([    [10, 20, 30],    [40, 50, 60],    [70, 80, 90],    [100, 110, 120] ])
#part 1
print(X.shape)
print(X.ndim)
print(type(X))
#part 2
print(X[:,1])
#part 3
print(X[:2])
#part 4
print(X[-1:-3:-1])
#part 5
print(np.where(X>80,0,X))
#part 6
print(np.std(X,axis=0))
print(np.mean(X,axis=0))
print(np.max(X,axis=0))
print(np.min(X,axis=0))
