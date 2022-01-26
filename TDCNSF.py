# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 17:44:04 2022

@author: victo
"""

import data_process as pd

class TDCNSF(pd.Data_process):
    TT=10

    def ValorPresenteEgresos1t(self,edad,t):
        kpxtT_value=self.kpxT(edad,t)
        qxtk1_value=self.qxtk1(edad,t)
        z=self.z_vector(t)
        VPEt=[]
        for i in range(self.n-t):
            VPEt.append(kpxtT_value[i]*qxtk1_value[i]*z[i]*self.b1['beneficio por muerte'][i])
        return sum(VPEt)

    def ValorPresenteIngresost(self,edad,t,m):
        PT=self.PrimaTarifa(edad,m,t)
        A=self.anualidad(edad, t, m)
        return PT*sum(A) 
       
    
    def Reserva1t(self,edad,t,m):
        
        return self.ValorPresenteEgresos1t(edad,t)-self.ValorPresenteIngresost(edad, t,  m)
            
    def ValorPresenteEgresos2t(self,edad,t):
        kpxtT=self.kpxT(edad,t)
        qxtk2=self.qxtk2(edad,t)
        z=self.z_vector(t)
        VPEt= []
        print(kpxtT)
        print(qxtk2)
        print(z)
        key="Beneficio por cancelacion"
        for k in range(self.n-t):
            VPEt.append(kpxtT[k]*qxtk2[k]*z[k]*self.b2[key][k])
        return sum(VPEt)
        

    
    def Reserva2t(self,edad,t,m):
        return self.ValorPresenteEgresos2t(edad,t)-self.ValorPresenteIngresost(edad,t,m)
    
        
                
                
        
        
    
        
    
    

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
    
    def CalcularReservat(self,edad,t,m):
        R1t=self.Reserva1t(edad, t, m)
        R2t=self.Reserva2t(edad, t, m)
        R3t=self.Reserva3t(edad, t, m)
        RTt=self.ReservaTotalt(edad, t, m)
        
        print(f'La Reserva del decremento 1 a tiempo {t} es {R1t}')
        print(f'La Reserva del decremento 2 a tiempo {t} es {R2t}')
        print(f'La Reserva del decremento 3 a tiempo {t} es {R3t}')
        print(f'La Reserva Total a tiempo {t} es {RTt}')


    ##2Valores Garantizados

    def funcion_rescate(self,n):
        Rctet=[]
        for k in range(n+1):
            if(k<0.20*n):
                Rctet.append(0)
            elif(0.20*n<=k):
                Rctet.append(0.80+0.25*(k-0.20*n)/n)
                
            else:
                Rctet.append(0.80+0.25*(k-0.20*n)/n)
        return Rctet
    
    def valor_rescate(self,edad,m): #Aqui k=TT
        Rv=[]
        Rcte=self.funcion_rescate(self.TT)
        for j in range(self.TT):
            Rv.append(self.Reserva1t(edad, m, j))
        return Rv
    
    