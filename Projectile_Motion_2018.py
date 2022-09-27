#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt


get_ipython().run_line_magic('matplotlib', 'inline')


#Create arrays for your data
theta_array = np.array([47.8, 44.8, 41.8, 38.8, 35.8])
ymean_array = np.array([53.12, 56.86, 58.18, 55.54, 50.1])
yerr_array = np.array([1.82, 2.12, 1.74, .3, 29])
#Create an array for your y-axis uncertainties

#Reassign variables
x = theta_array
y = ymean_array
dy = yerr_array

#size the plot
plt.figure(figsize=(15,10))

#create scatter plot
plt.scatter(x, y, color='blue', marker='o')

#create labels
plt.xlabel('$\\theta$ (degrees)')
plt.ylabel('$y_{mean}$ (m)')
plt.title('Height on wall vs Launcher Angle')

#fitting to a 2nd degree polynomial
c,b,a=np.polynomial.polynomial.polyfit(x,y,2,w=dy)

#Annotate with values of A, B, C from best fit polynomial
plt.annotate('A = {value:.{digits}E}'.format(value=a, digits=3),
             (0.05, 0.9), xycoords='axes fraction')

plt.annotate('B = {value:.{digits}E}'.format(value=b, digits=3),
             (0.05, 0.85), xycoords='axes fraction')
             
plt.annotate('C = {value:.{digits}E}'.format(value=c, digits=3),
             (0.05, 0.8), xycoords='axes fraction')
#Create fit line
xnew = np.linspace(x.min(), x.max(), 300)
fit = a*xnew**2 + b*xnew +c

plt.scatter(xnew, fit, color='red')
plt.show()

print ("C = ",c , "B = ",b, "A = ",a)


# In[ ]:





# In[ ]:




