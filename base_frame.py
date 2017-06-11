# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 12:55:51 2017

@author: Marija Bebic
"""

"""
Demo of a PathPatch object.
"""
import numpy as np
from numpy import cos, sin

import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

#%% Define colors, scaling, etc
atu = 0.8 # Angle to use as a relative value to 2*pi
R = 2 # radius for the perimeter of the chart
kr = 1.1
xlims = [-R*kr,R*kr]
ylims = [-R*kr,R*kr]

#%% Input actual data 
AreaNames= ['A', 'B', 'C', 'D']
# Flows between areas, defined as a matrix
#MaxFlows = np.array([[np.nan, 100.  , 200.  , 400.],
#                     [100.  , np.nan, 200.  , np.nan],
#                     [200.  , 200.  , np.nan, 600.],
#                     [400.  , np.nan, 600.  , np.nan]])
#MaxFlows = np.array([[np.nan, 100.  , 200.],
#                     [100.  , np.nan, 400.],
#                     [200.  , 400.  , np.nan]])
MaxFlows = np.array([[np.nan, 100. , 100. , np.nan, 100.],
                     [100. , np.nan, 200. , np.nan, 100.],
                     [100. , 200. , np.nan, 100. , np.nan],
                     [np.nan, np.nan, 100. , np.nan, 100.],
                     [100. , 100. , np.nan, 100. , np.nan]])



#%% Calculate angle scale for flows
# Take max angle from MaxFlows array and the number of flows and divide the 
# circle into segments that represent flows. 
flowScale = 2.*np.pi*atu/np.nansum(MaxFlows) # rad/MW
print ('flowScale: %.3f (rad/MW)' %(flowScale))
print ('flowScale: %g (rad/MW)' %(flowScale))
print ('flowScale: %.3f (rad/MW), %.3f (deg/MW)' %(flowScale, flowScale*180./np.pi))

#%% Calculate reference zeros for flow areas
nAr = MaxFlows.shape[0] # Number of areas in input data
aStep = np.pi*2/nAr 
th1 = np.arange(0, 2*np.pi, aStep)
x1 = R*cos(th1) #x coordinates for ref. angles of area
y1 = R*sin(th1) #y coordinates for ref. angles of area

#%% Drawing the arcs
subDegs = np.linspace(10, 40, nAr)
subRads = subDegs*np.pi/180
#th2 = np.arange(0, 2*np.pi, np.pi*2/nAr)
x2 = R*cos(th1-subRads)
y2 = R*sin(th1-subRads)

#%% For loop for vector product
for i in range(0, MaxFlows.shape[0]):
    for j in range(0, MaxFlows.shape[1]):
        #print('x[%d] = %g; y[%d] = %g' %(j, x1[j], j, y1[j]))
        if i != j:
            print('Point i = %d, point j = %d' %(i, j))
            Pijx = x1[j] - x1[i]
            Pijy = y1[j] - y1[i]
            PiCx = 0 - x1[i]
            PiCy = 0 - y1[i]
            
            print('x[%d] = %g, y[%d] = %g, x to origin = %g, y to origin = %g' %(i, Pijx, j, Pijy, PiCx, PiCy))

#if j = y , skip calculation
#%%creates a circle
th = np.arange(0, 2*np.pi, np.pi/100)
x = R*cos(th)
y = R*sin(th)

#%% Plotting
#%% open figure
fig, ax = plt.subplots()
ax.plot(x,y)
# ax.scatter(x1,y1, c='lime')
ax.scatter(x1,y1, c='#535353')
ax.scatter(x2,y2, c='red')

ax.set_xlim(xlims)
ax.set_ylim(ylims)
ax.axis('equal')
ax.grid()

plt.show()
    
#%% This part is the reference for code
if False:
    fig, ax = plt.subplots()
    Path = mpath.Path
    path_data = [
        (Path.MOVETO, (1.58, -2.57)),
        (Path.CURVE4, (0.35, -1.1)),
        (Path.CURVE4, (-1.75, 2.0)),
        (Path.CURVE4, (0.375, 2.0)),
        (Path.LINETO, (0.85, 1.15)),
        (Path.CURVE4, (2.2, 3.2)),
        (Path.CURVE4, (3, 0.05)),
        (Path.CURVE4, (2.0, -0.5)),
        (Path.CLOSEPOLY, (1.58, -2.57)),
        ]
    codes, verts = zip(*path_data)
    path = mpath.Path(verts, codes)
    patch = mpatches.PathPatch(path, facecolor='b', alpha=0.3)
    ax.add_patch(patch)
    
    # plot control points and connecting lines
    x, y = zip(*path.vertices)
    line, = ax.plot(x, y, 'bo-')
    
    ax.set_xlim([-3,3])
    ax.set_ylim([-3,3])
    ax.axis('equal')
    ax.grid()
    plt.show()