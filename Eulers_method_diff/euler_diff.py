#%%

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf
#%%
# EDIT METHOD PARAMETERS
h = 0.1 # integration step
N = 100; # number of iterations

# EDIT diff. equation
xi = 0 # initial x
yi = 0 # initial x
def f(x,y): 
    return np.exp(-x**2) # equation y = f(x)

# MANUALLY ENTER correct solution
def y_true(x,y):
    return 0.5*np.sqrt(np.pi)*erf(x)


#%% Euler's method evaluation
X = np.ones(N)*np.nan;
Y = np.ones(N)*np.nan;
Y_true = np.ones(N)*np.nan;
for ii in np.arange(1, N+1):
    print(ii)
    
    X[ii-1] = xi;
    Y[ii-1] = yi;
    
    # true value
    Y_true[ii-1] = y_true(xi,yi)
    
    # estimation
    yi = yi + h*f(xi,yi)
    xi = xi + h
    
plt.figure(figsize=[10,6])
plt.scatter(X,Y)
plt.scatter(X,Y_true,marker='x')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['estimate', 'true'])
# plt.ylim([0,2]) # ADJUST or COMMENT
plt.show()




