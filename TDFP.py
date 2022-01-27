# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 09:58:20 2022

@author: victo
"""
import math
import data_process as dp


class TDFP(dp.Data_process):
    
    
    def prima_riesgo(self,edad):
        kpxt=self._kpxT(edad)
        qxk1=self._qxtk1(edad)
        qxk2=self._qxtk2(edad)
        qxk3=self._qxtk3(edad)
        z=self._z_vector()
        P1=[]
        P2=[]
        P3=[]
        for k in range(self._n):
            P1.append( kpxt[k]*qxk1[k]*z[k]*self.b1['beneficio por muerte'][k])
            P2.append( kpxt[k]*qxk2[k]*z[k]*self.b2['Beneficio por cancelacion'][k])
            P3.append(kpxt[k]*qxk3[k]*z[k]*self.b3['Benefecio por invalidez'][k])
        return sum(P1)+sum(P2)+sum(P3)
    
    def anualidad(self,edad,m):##funciona
        kpxt=self._kpxT(edad,0)
        vk=[]
        A=[]
        for k in range(m):
            vk.append(math.pow(1+self._i,-k))
        for i in range(m):
            A.append(kpxt[i]*vk[i])        
        return sum(A)
        
    def prima_NN(self,edad,m): ##funciona
        P=self.prima_riesgo(edad)
        A=self.anualidad(edad, m)
        return P/A

    def PrimaTarifa(self,edad,m):##funciona
        P=self.prima_riesgo(edad)
        A=self.anualidad(edad, m)
        PNN=P/A
        return PNN/(1-self._alpha-self._beta-self._gamma)
    
    
    def calcular_seguro(self,edad,m):
        P=self.prima_riesgo(edad)
        A=self.anualidad(edad, m)
        PNN=P/A
        PT=PNN/(1-self._alpha-self._beta-self._gamma)
        print("La Prima de Riesgo es:", P)
        print("La Anualidad es:", A)
        print("La Prima Neta Nivelada es:", PNN)
        print("La Prima de Tarifa es:", PT)
        
        
   