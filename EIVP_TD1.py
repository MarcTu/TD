

# Exercice 1 :


def is_palindrome(mot):
    mot_inverse=mot[::-1]
    if mot==mot_inverse:
        return True
    else:
        return False


    # (Bonus)

def is_palindrome2(mot):
    mot_nouveau=''
    for lettre in mot:
        if lettre=="'" or lettre=="-" or lettre=="," or lettre==" ":
            None
        
        elif lettre=="é":
            mot_nouveau+="e"
        
        else:
            mot_nouveau+=lettre.lower()
    
    return is_palindrome(mot_nouveau)
    


# Exercice 2 :

def swap(a,i,b,j,L):
    L[i]=b
    L[j]=a


def bubbleSort(L):
    n=len(L)
    for k in range(n):
        for i in range(n-1-k):
            a=L[i]
            b=L[i+1]
            if a>b:
                swap(a,i,b,i+1,L)
    return L
    
    
    
def insertionSort(L):
    n=len(L)
    for i in range(1,n):
        ref=L[i]
        j=i
        while j>0:
            a=L[j-1]
            if ref<a:
                swap(a,j-1,ref,j,L)
                j=j-1
            else:
                break
    return L




# Exercice 3 :


def partitionner(T, first, last, pivot):
    n=len(T)
    
    swap(T[pivot],pivot,T[last],last,T)         # échange le pivot avec le dernier du tableau , le pivot devient le dernier du tableau
    j = first
    for i in range(first,last):                 # la boucle se termine quand i = (dernier-1).
        if T[i] <= T[last]:
            swap(T[i],i,T[j],j,T)
            j = j + 1
    swap(T[last],last,T[j],j,T)
    return j


def choix_pivot(T,first, last):
    return (first+last)//2


def tri_rapide(T,first,last):
    if first<last:
        pivot = choix_pivot(T, first, last)
        pivot = partitionner(T, first, last, pivot)
        tri_rapide(T, first, pivot-1)
        tri_rapide(T, pivot+1, last)


def quickSort(T):
    
    tri_rapide(T,0,len(T)-1)
    
    return T




# Exercice 4 :

import pandas as pd

df = pd.read_csv("sample_data/california_housing_test.csv")

df.head(3)

df.sort_values('latitude').head(3)









  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  