#!/usr/bin/env python
# coding: utf-8

# In[47]:


#fonction  qui retourne la factorielle
def factorielle(nb):
    fact = 1
    for i in range(1, nb+1):
        fact = fact * i
        
    return fact
factorielle(5)


# In[128]:


# fonction qui retourne un parametre N et qui donne la liste des nombres impairs
def impaire(N):
    ab = 1
    while (N>1 ):
        N = N -1
        if (N % 2 == 1):
            print(N)
          
impaire(15)


# In[77]:


# action pour effectuer des tries 
liste = [17,38,10,25,72]
liste.sort()
liste

#action pour ajoute l'element 12
liste.append(12)
liste

#action pour renverse
liste.reverse()
liste
#affichez le nombre d'element
liste
len(liste)
#supprimez l'element 38
liste.remove(38)
liste
#affichez la sous-liste du 2e au 3e element
liste[1:3]
#affichez la sous liste du debut au 2e élément
liste[:2]
#affichez la sous-liste du 3e element a la fin
liste[2:]


# In[ ]:




