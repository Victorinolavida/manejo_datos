# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 17:44:04 2022

@author: victo
"""

import data_process as pd


class TDCNSF(pd.Data_process):

    def ValorPresenteIngresos(self,edad,t,m):
        PT=self.PrimaTarifa(edad,m,t)
        a=self.anualidad(edad, m)
        return PT*a
    
    def ValorPresenteEgresos1t(self,edad,t):
        kpxtT_value=self.kpxT(edad,t)
        qxtk1_value=self.qxtk1(edad,t)
        z=self.z_vector(t)
        VPEt=[]
        for i in range(self.n-t):
            VPEt.append(kpxtT_value[i]*qxtk1_value[i]*z[i]*self.b1['beneficio por muerte'][i])
            
        return sum(VPEt)
        
    
    def Reserva1t(self,edad,t,m):
        return self.ValorPresenteEgresos1t(edad,t)-self.ValorPresenteIngresos(edad,t,m)
    ##########
    
    
    def ValorPresenteIngresos2t(self,edad,t,m):
        kpxtT_value=self.kpxT(edad,t)
        qxtk2_value=self.qxtk2(edad,t)
        z=self.z_vector(t)
        VPEt=[]
        for i in range(self.n-t):
            VPEt.append(kpxtT_value[i]*qxtk2_value[i]*z[i]*self.b2['Beneficio por cancelacion'][i])
            
        return sum(VPEt)
    
    def Reserva2t(self,edad,t,m):
        return self.ValorPresenteEgresos1t(edad,t)-self.ValorPresenteIngresos(edad,t,m)

    def ValorPresenteIngresos3t(self,edad,t,m):
        kpxtT_value=self.kpxT(edad,t)
        qxtk3_value=self.qxtk3(edad,t)
        z=self.z_vector(t)
        VPEt=[]
        for i in range(self.n-t):
            VPEt.append(kpxtT_value[i]*qxtk3_value[i]*z[i]*self.b3['Benefecio por invalidez'][i])
            
        return sum(VPEt)
    
    def Reserva3t(self,edad,t,m):
        return self.ValorPresenteIngresos3t(edad,t,m)-self.ValorPresenteIngresos(edad,t,m)
    
    
    def ReservaTotalt(self,edad,t,m):
        return self.Reserva1t(edad,t,m)+self.Reserva2t(edad,t,m)+self.Reserva3t(edad, t, m)