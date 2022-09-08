#!/usr/bin/env python
# coding: utf-8

# # 1. Linechart or plot()

# In[1]:


import numpy as np


# In[2]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


x = np.arange(10,20) #for one array


# In[4]:


x


# In[5]:


#plot (plt.plot())

plt.plot(x)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("My First Graph")


# In[6]:


y = np.arange(20,30) #for one array


# In[7]:


y


# In[8]:


plt.plot(y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("My Second Graph")


# In[9]:


###combine two arrays in a single graph

###Line Chart###


plt.plot(x)
plt.plot(y)
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
plt.xlabel("x-axis",fontdict=font)
plt.ylabel("y-axis",fontdict=font)
plt.title("My Final Graph",fontdict=font)


# In[10]:


###combine two arrays in a single graph

###Line Chart###
##or ### plot ##

plt.plot(x, c = "m" ,linewidth = 10, linestyle = "--") # c = colour
plt.plot(y, c = "y", linewidth = 15, linestyle = "-.")

font = {'family': 'serif',  ####family is key and serif is value (key-value pair)
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
plt.xlabel("x-axis",fontdict=font)
plt.ylabel("y-axis",fontdict=font)
plt.title("My Final Graph",fontdict=font,loc = 'left') #above graph only change the location of the Title (left,center,right)


# In[11]:


###combine two arrays in a single graph

###Line Chart or plot###


plt.plot(x,marker = "o",c = "g", ms = 10) #ms - markersize, c = colour
plt.plot(y,marker = "*",c = "m", ms = 12)
font = {'family': 'serif',                 ####family is key and serif is value (key-value pair)
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
plt.xlabel("x-axis",fontdict=font)
plt.ylabel("y-axis",fontdict=font)
plt.title("My Final Graph",fontdict=font)


# In[12]:


x = np.arange(0,20)
y = np.arange(20,40)

plt.plot(x, linestyle = '--', c = "y") #dashed
plt.plot(y, linestyle = ':', c = "r") #dotted
plt.show()


# # 2. Scatter Plot()

# In[13]:


# Example 1)

##plt scatter### (plt.scatter)


x1 = np.arange(20,40)
y1 = np.arange(40,60)

plt.scatter(x,y,c = "g")
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.title(" Graph in 2D")
plt.savefig("Test.png")


# In[14]:


#Example - 2)

#scatter plot (plt.scatter)
x


# In[15]:


y = x*x


# In[16]:


y


# In[17]:


plt.scatter(x,y,c = "g")

plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.title(" Graph in 2D")
plt.savefig("Test1.png")


# # 3. Subplot()

# In[98]:


#(2,2,1) = (no.of rows, no.of columns, plots position)

x11 = np.array([1,2,3,4,5])
y11 = np.array([45,56,78,88,89])

plt.subplot(2,2,1) 
plt.plot(x11,y11,"r--") #you can add parameters here like markersize, marker, linestyle, linewidth, colour
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("1st graph - Line Chart")
plt.show()


plt.subplot(2,2,2)
plt.bar(x11,y11)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("2st graph - Bar Graph")
plt.show()


plt.subplot(2,2,3)
plt.plot(x11,y11, "bo")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("3rd graph - Scatter Graph")
plt.show()


# # 4. Bar Plot or chart()

# # 1. Vertical Bar Chart()

# In[75]:


#Example 1)

x = [10,20,30]
y = [11,16,9]


plt.bar(x,y, color = "g",width=5)
plt.xlabel("x- axis")
plt.ylabel('y - axis')
plt.title("Bar Graph")
plt.grid(color='y')
plt.show()


# In[99]:


#Example 2)
company = ['Google','Amzn','Apple','Facebook']
revenue = [90,136,89,27]
profit = [40,2,34,12]


# In[103]:


x = np.arange(len(company))


# In[105]:


x


# In[111]:


plt.bar(x-0.2,revenue, width = 0.4, label = "Revenue")
plt.bar(x+0.2,profit, width = 0.4, label = "Profit")
plt.ylabel("Revenue(bln)")
plt.title("US Tech Stocks")

plt.xticks(x,company)
plt.legend()
plt.show()


# # 2 . Horizontal Bar Chart()

# In[115]:


plt.barh(x-0.2,revenue, label = "Revenue")
plt.barh(x+0.2,profit, label = "Profit")
plt.ylabel("Revenue(bln)")
plt.title("US Tech Stocks")

plt.yticks(x,company)
plt.legend()
plt.show()


# In[ ]:





# # 5. Histograms()

# In[60]:


a = np.array([12,23,44,54,57,55,11,66,10])
plt.hist(a, bins = 5)
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.title("histogram")
plt.show()


# # 5. Piechart()

# In[74]:


labels = "python", "c++", "mysql", "java"
sizes = [215,130,245,210]
colors = ["gold", "yellowgreen", "lightcoral", "blue"]
explode = (0.4,0,0,0)

plt.pie(sizes, labels = labels, colors = colors, autopct = "%1.1f%%", explode = explode, shadow = True)

plt.axis("equal")
plt.show()

