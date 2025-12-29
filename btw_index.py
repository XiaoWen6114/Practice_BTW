# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 22:52:18 2025

@author: XiaoWen6114
"""

x=input("test: ")

#Step 1: Transform and find F column and L column
#1
x=str(x)+'$'
temp=[]
for i in range(len(x)):
    x=x[-1]+x[:-1]
    temp.append(x)
temp.sort()
M_array=temp

#2
F_list=[i[0] for i in M_array]
L_list=[i[-1] for i in M_array]
L=''.join(L_list)
print('Step 1: L list: '+L)

#Step 2: Create suffix array
SA_array=[]
for i in range(len(M_array)):
    for j in range(len(x)):
        if M_array[i][j] == '$':
            SA_array.append(str(len(x)-1-j))
            break
print('Step 2: SA array: '+''.join(SA_array))

#Step 3: Calculate C(c) array
C_dic={}
temp=F_list[0]
C_dic[F_list[0]]=0
for i in range(len(F_list)):
    if F_list[i] != temp:
        C_dic[F_list[i]]=i
        temp=F_list[i]
print('Step 3: C(c) array: '+', '.join(f'{cha}:{pos}' for cha,pos in sorted(C_dic.items(), key=lambda x: x[1])))

#Step 4: Calculate Occ(c,i)
print('step 4: Occ(c,i):')
Occ_dic={}
temp=''.join(sorted(set(x)))
for i in temp:
    temp1=0
    Occ_dic[i+',0']=temp1
    for j in range(len(L_list)):
        if L_list[j] == i:
            temp1+=1
            print(i+','+str(j+1)+': '+str(temp1), end='\t')
        if j or L_list[0] == i:
            Occ_dic[i+','+str(j+1)]=temp1
        else:
            Occ_dic[i+','+str(j+1)]=0

#FM index is Occ_dic.
