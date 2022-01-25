# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 18:08:16 2022

@author: victo
"""

import load_databases as db
import math

class Data_process(db.Load_databases):
    
    def kpxT(self,edad,t=0):
        kpxt=[]
        for k in range(self.n-t):
            if(k>0):
                kpxt.append(kpxt[k-1]*self.table["px(T)"][edad+t+k-1])
            else:
                kpxt.append(1)
        
        return kpxt
    
    
    def qxtk1(self,edad,t=0):
        qxk1=[]
        for k in range(self.n-t):   
            qxk1.append(self.table["qx(1)"][edad+k+t+1])
        return qxk1
    
    def qxtk2(self,edad,t=0):
        qxk1=[]
        for k in range(self.n-t):   
            qxk1.append(self.table["qx(2)"][edad+k+t+1])
        return qxk1
    
    def qxtk3(self,edad,t=0):
        qxk1=[]
        for k in range(self.n-t):   
            qxk1.append(self.table["qx(3)"][edad+k+t+1])
        return qxk1
    
    def z_vector(self,t=0):
        z=[]
        for k in range(self.n-t):
            z.append(math.pow(1+self.i,-(k+1)))
        return z
    
    def prima_riesgo(self,edad,t=0):
        kpxt=self.kpxT(edad,t)
        qxk1=self.qxtk1(edad,t)
        qxk2=self.qxtk2(edad,t)
        qxk3=self.qxtk3(edad,t)
        z=self.z_vector(t)
        P1=[]
        P2=[]
        P3=[]
        for k in range(self.n-t):
            P1.append( kpxt[k]*qxk1[k]*z[k]*self.b1['beneficio por muerte'][k])
            P2.append( kpxt[k]*qxk2[k]*z[k]*self.b2['Beneficio por cancelacion'][k])
            P3.append(kpxt[k]*qxk3[k]*z[k]*self.b3['Benefecio por invalidez'][k])
        return sum(P1)+sum(P2)+sum(P3)
    
    def anualidad(self,edad,m,t=0):
        kpxt=self.kpxT(edad,t)
        vk=[]
        A=[]
        for k in range(m):
            vk.append(math.pow(1+self.i,-k))
        for i in range(m):
            A.append(kpxt[i]*vk[i])        
        return sum(A)
        
    def prima_NN(self,edad,m,t=0):
        P=self.prima_riesgo(edad,t)
        A=self.anualidad(edad, m,t)
        return P/A

    def PrimaTarifa(self,edad,m,t=0):
        P=self.prima_riesgo(edad,t)
        A=self.anualidad(edad, m,t)
        PNN=P/A
        return PNN/(1-self.alpha-self.beta-self.gamma)
         
