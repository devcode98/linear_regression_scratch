import sys
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import math as mt


'''Linear Regression From Scratch '''
# let the equation be y=4x+3
''' this part is for the purpose of calculus'''
def sum_func1(m,n):
    i=0
    cost_1=0
    while i<50:
        cost_1=cost_1+((m[i]-n[i])*(n[i]))
        i=i+1
    cost_1=(cost_1)/50
    return (-1*cost_1)    
def sum_func2(m,n):
        i=0
        cost_1=0
        while i<50:
            print(i)
            cost_1=cost_1+(m[i]-n[i])
            i=i+1
        cost_1=(cost_1)/50    
        return (cost_1*-1)    

def cost_1(m,n):
    cost_1=0
    i=0
    while i<50:
        cost_1=cost_1+((0.5)*((m[i]-n[i])**2))
        i=i+1
    cost_1=(cost_1)/50
    return cost_1    
    
''' starting of the program'''

import random as rd
x=0
y=(4*x)+(3)
x_data_list=[]
y_data_list=[]
''' first we will be creating a set of data points for ourselves wrt to this line '''
i=0
while i<50:
    x=rd.randrange(1,100,1)
    x_data_list.append(x)
    y=(4*x)+(3)
    y_data_list.append(y)
    i=i+1
    
''' now we will be trying to generate random points wrt to the line'''
y_data_given=[]
i=0
while i<50:
   m=rd.randrange(1,100,1)
   y=(4*x_data_list[i])+m+3
   plt.scatter(x_data_list[i],y)
   y_data_given.append(y)
   i=i+1    
   
''' now we will be trying to fit a curve via these set of points '''
# let the new eqaution be y=ax+b
a=1
b=1

'''these our our initial values'''
''' since we have a set of 100 values for ourselves '''
y_init=[]
i=0
cost=0
while i<50:
    cost=cost+((y_data_given[i]-0)**2)
    i=i+1
    y_init.append(0)
initial_cost=(cost)/100

i=0
while i<4000:
   
   
   a=a-0.00009*(sum_func1(y_data_given,y_init))
   b=b-0.00009*(sum_func2(y_data_given,y_init))
       
       
   print(a)
   print(b)
   k=0
   y_init=[]
       
   while k<50:
       y_init.append((a*x_data_list[k]+b))
       k=k+1
   
   initial_cost=cost_1(y_data_given,y_init)
   print(initial_cost)
   i=i+1
y_new=[]
y_n=0
i=0
while i<50:
    y_n=a*x_data_list[i]+b
    y_new.append(y_n)
    i=i+1

plt.plot(x_data_list,y_new,color='r')  
plt.scatter(x_data_list,y_data_given,color='b')  

x_train=np.array(x_data_list)
y_train=np.array(y_data_given)

x_train=x_train.reshape(-1,1)

from sklearn.linear_model import LinearRegression
lin=LinearRegression()
t=lin.fit(x_train,y_train)   
print(lin.intercept_)

i=0
while i<50:
    plt.scatter(x_data_list[i],((x_data_list[i]*lin.coef_)+lin.intercept_),color='y')
    i=i+1
    