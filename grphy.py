# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:49:43 2019

@author: hp
"""
def gplot(emotion):
    import numpy as np
    from scipy.interpolate import make_interp_spline, BSpline
    from matplotlib import pyplot as plt
    
    count = len(emotion)   #count of tweets or points
    Y = [0]*count
    x = np.array([i for i in range(count)])
    #y = np.array([3,-3,0,-2,3,0,0,-1])  #sentiment polarity array
    y = np.array(emotion)
    x_smooth = np.linspace(x.min(),x.max(),900)
    spl = make_interp_spline(x,y,k=3)
    y_smooth = spl(x_smooth)
    
    plt.clf()
    plt.plot(x,Y,color='g')
    plt.plot(x_smooth,y_smooth)
    plt.title('Sentiment')
    plt.xlabel('timeline')
    plt.ylabel('mood')
    plt.savefig('C:/Users/hp/cj/project/static/images/new_plot.png')