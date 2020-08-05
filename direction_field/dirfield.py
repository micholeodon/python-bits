#%% direction field
import numpy as np
import matplotlib.pyplot as plt
#%%

# step
nx, ny = .3, .3

# range
x = np.arange(0, 5, nx)
y = np.arange(-5, 5, ny)
X, Y = np.meshgrid(x, y)


#%% UNCOMMENT ONE OF THESE dy's
# differential equation 1
dy = X + np.sin(Y)

# differential equation 2
# dy = -X

# differential equation 3
# dy = Y

# differential equation 4
# dy = Y*(1-Y)*X

# differential equation 5
# dy = (Y**2)*X*np.exp(-X)

# differential equation 6
# dy = (Y+X)/(Y*X)

# differential equation 7
# dy = -0.5*Y
 
# differential equation 8
# dy = 4*Y*X


#%%
dx = np.ones(dy.shape)
color = dy
#lw = 1
plt.figure(figsize=[10,10])
plt.streamplot(X,Y,dx, dy, color=color, density=1, cmap='jet', arrowsize=1.5)
#plt.plot(x,y)
