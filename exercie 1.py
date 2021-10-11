#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#calcule l'indice de masse corporelle d'un adulte

def TMimc():
    taille = float(input("Votre taille (en cm)?"))
    masse = float(input("Votre masse (en kg)?"))
    taille = taille/100
    imc = masse / (taille * taille)
    imc = round(imc,2)
    
    print("==> Votre IMC vaut ", imc, "kg/m²")
    if imc < 16.0:
        print("==> Denutrition")
    elif imc < 18.5:
        print("==> Maigreur")
    elif imc < 25.0:
         print("==> Corpulence normale")
    elif imc < 30.0:
        print("==>Surpoids")
    elif imc < 35.0:
        print("==> Obesite modere")
    elif imc < 40.0:
        print("==>Obesite severe")
    else:
        print("==> Obesite massive")
TMimc() 


# In[2]:


# une fonction qui recupere la note au bac

def notebac():
    note = float(input("entre votre note au bac?"))
    
    if  note < 10:
        print(" vous etez recalé")
    elif note < 12:
        print(" Felicitation !vous avez votre BAC avec mention passable")
       
    elif note < 14:
        print("Felicitation !vous avez votre BAC avec mention Assez bien")
    elif note < 16:
        print("Felicitation !vous avez votre BAC avec mention Bien")
    else: 
        print("Felicitation !vous avez votre BAC avec mention très bien")
notebac()
    


# In[3]:


# fonction qui retourne l'aire de la surface d'un disque de rayon R
from math import pi
r = float(input("Saisissez la valeur du rayon r: "))
airedisque = pi*(r**2)  
print(" airedisque = ", airedisque)


# In[8]:


from math import pi
r = float(input("Saisissez la valeur du rayon r: "))
airedisque2 = pi*(r**2) 
print(" airedisque2 = ", airedisque2 ,'cm²')  


# In[ ]:




