#!/usr/bin/env python
# coding: utf-8

# In[1]:


#matrix_1 mxn
#matrix_2 nxp
#matrix_3 =matrix_1 x matrix_2 mxp


# In[22]:


def get_value_from_row_col(r_1,c_1): # O(n) complexity
    t=0
    for i in range(len(r_1)):
        t=t+r_1[i]*c_1[i]
    return t

a=[1,2,3,4]
b=[5,6,7,8]

get_value_from_row_col(a,b)


# In[23]:


z=[[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,8]]
v=[[1,2,3,4],[5,6,7,8]]


# In[24]:


def get_row_from_matrix(a,i): #O(1)
    return a[i]

def get_column_from_matrix(a,j): #O(n)
    col=[]
    for row in a:
        col.append(row[j])
    return col

get_row_from_matrix(z,0)
get_column_from_matrix(z,2) 


# In[27]:


def matrix_multiply(m_1,m_2):     #O(m*n*p) p=sütun sayısı  #kare matris ise O(n^3)
    m=len(m_1)    #1.nin satır sayısı
    n=len(m_2[0]) #2.nin sütun sayısı
    r=[]
    for i in range(m):
        r.append([])
        for j in range(n):
            a=get_row_from_matrix(m_1,i)
            b=get_column_from_matrix(m_2,j)
            c=get_value_from_row_col(a,b)
            r[i].append(c)
    return r


# In[26]:


matrix_multiply(v,z) #doğru sırada vermeye dikkat et


# In[ ]:




