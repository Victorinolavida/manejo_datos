# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 18:08:16 2022

@author: victo
"""

import load_databases as db
import math

class Data_process(db.Load_databases):
    
    ##funciona bien 
    def kpxT(self,edad,t=0):
        kpxt=[]
        for k in range(self.n-t):
            if(k>0):
                kpxt.append(round(kpxt[k-1]*self.table["px(T)"][edad+t+k-1],7))
            else:
                kpxt.append(1)
        
        return kpxt
    
    ##funciona como debe
    def qxtk1(self,edad,t=0):
        qxk1=[]
        for k in range(self.n-t):   
            qxk1.append(self.table["qx(1)"][edad+k+t])
        return qxk1
    
    ##funcion bien
    def qxtk2(self,edad,t=0):
        qxk1=[]
        for k in range(self.n-t):   
            qxk1.append(self.table["qx(2)"][edad+k+t+1])
        return qxk1
    
    #funciona bien
    def qxtk3(self,edad,t=0):
        qxk1=[]
        for k in range(self.n-t):   
            qxk1.append(self.table["qx(3)"][edad+k+t])
        return qxk1
    ##funciona OK
    def z_vector(self,t=0):
        z=[]
        for k in range(1,self.n-t+1):
            z.append(math.pow(1+self.i,-k))
        return z
    #funciona bien , bug al parecer si pones una edad y t=0
    def prima_riesgo(self,edad,t):
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
    
    def anualidad(self,edad,t,m):##funcion
        if(t<m):
            kpxt=[]
            vk=[]
            VPIt=[]
            for k in range(1,abs(m-t)+1):
                vk.append(math.pow(1+self.i,-(k-1)))
            for k in range(abs(m-t)):
                if(k>0):
                    
                    kpxt.append(round(kpxt[k-1]*self.table["px(T)"][edad+t+k-1],7))
                    
                else:
                    kpxt.append(1)
                
            for k in range(abs(m-t)):
                VPIt.append(vk[k]*kpxt[k])
                ##regresa arreglo
            return VPIt
        else:
            return [0]
     
        
        
    def prima_NN(self,edad,m,t): ##funciona
        P=self.prima_riesgo(edad,t)
        A=self.anualidad(edad, m,t)
        return P/sum(A)

    def PrimaTarifa(self,edad,m,t):##funciona
        P=self.prima_riesgo(edad,t)
        A=sum(self.anualidad(edad, t,m))
        if(A!=0):
            PNN=P/A
            return PNN/(1-self.alpha-self.beta-self.gamma)
        else:
            return 0
         
