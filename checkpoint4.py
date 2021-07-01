#!/usr/bin/env python
# coding: utf-8

# In[1]:


#qst 1
n1 = int(input("entrez un premier nombre: "))
n2 = int(input("entrez un deuxième nombre: "))
n3 = int(input("entrez un troisème nombre: "))
liste = [n1,n2,n3]
m = max(liste)
print("Le plus grand nombre de la liste est:", m)


# In[2]:


# qst 2
def calculation(a,b):
    c = a + b
    d = a - b
    return c,d
print(calculation(40,10))


# In[3]:


# qst 3
import numpy as np
liste = [0,1,2,3,4,5,6,7,8,9]
base = 0
base2 = 1
def add(liste):
    adt = sum(liste)
    return adt
print("addition:",add(liste)) # ajouter autant de nombres voulus à la liste

def prod(liste):
    pd = np.prod(liste)
    return pd
print("multiplication:",prod(liste))

for i in liste:
    if i%2 == 0:
        base += i
    else:
        base2 *= i
print("l'addition des nombres pairs:",base)
print("la multiuplication des nombres pairs:",base2)


# In[4]:


# qst 4
colors = "-" .join(sorted("green-red-yellow-black-white".split("-")))
print(colors)


# In[5]:


# qst 5 (bonus)
from math import *
C = 50
H = 30
D = input("entrez des valeurs en les sépérant avec une virgule:")
D = str(D)
liste = D.split(",")
for i in liste:
    i = float(i)
    Q = sqrt((2*C*i)/H)
    Q = int(Q)
    print(Q)


# In[ ]:




