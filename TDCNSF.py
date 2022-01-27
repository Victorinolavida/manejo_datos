# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 17:44:04 2022

@author: victo
"""

import data_process as pd
import matplotlib.pyplot as plt


class TDCNSF(pd.Data_process):
    TT=10

 ##se usa en todos asi que mejor se hace solo una vez
    def ValorPresenteIngresost(self,edad,t,m):
        PT=self.PrimaTarifa(edad,m,t)
        A=self.anualidad(edad, t, m)
        return PT*sum(A) 

    def ValorPresenteEgresos1t(self,edad,t):
        kpxtT_value=self._kpxT(edad,t)
        qxtk1_value=self._qxtk1(edad,t)
        z=self._z_vector(t)
        VPEt=[]
        key='beneficio por muerte'
        for i in range(self._n-t):
            VPEt.append(kpxtT_value[i]*qxtk1_value[i]*z[i]*self.b1[key][i])
        return sum(VPEt)

    def Reserva1t(self,edad,t,m):
        egresos=self.ValorPresenteEgresos1t(edad,t)
        return egresos-self.ValorPresenteIngresost(edad,t,m)
            
    def ValorPresenteEgresos2t(self,edad,t):
        kpxtT=self._kpxT(edad,t)
        qxtk2=self._qxtk2(edad,t)
        z=self._z_vector(t)
        VPEt= []
        key="Beneficio por cancelacion"
        for k in range(self._n-t):
            VPEt.append(kpxtT[k]*qxtk2[k]*z[k]*self.b2[key][k+t])
        return sum(VPEt)
        

    def Reserva2t(self,edad,t,m):
        egresos=self.ValorPresenteEgresos2t(edad,t)
        return egresos-self.ValorPresenteIngresost(edad,t,m)
    
    def ValorPresenteEgresos3t(self,edad,t):
        kpxtT_value=self._kpxT(edad,t)
        qxtk3_value=self._qxtk3(edad,t)
        z=self._z_vector(t)
        VPEt=[]
        key='Benefecio por invalidez'
        for i in range(self._n-t):
            VPEt.append(kpxtT_value[i]*qxtk3_value[i]*z[i]*self.b3[key][i])
        return sum(VPEt)
    
    def Reserva3t(self,edad,t,m):
        egresos=self.ValorPresenteEgresos3t(edad, t)
        return egresos-self.ValorPresenteIngresost(edad,t,m)
    
    def ReservaTotalt(self,edad,t,m):
        reserva1=self.Reserva1t(edad,t,m)
        reserva2=self.Reserva2t(edad,t,m)
        reserva3=self.Reserva3t(edad,t,m)
        return reserva1+reserva2+reserva3
        
                
                
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
                Rctet.append(round(0.80+0.25*(k-0.20*n)/n,7))
                
            else:
                Rctet.append(round(0.80+0.25*(k-0.20*n)/n,7))
        return Rctet
        
    def valor_rescate(self,edad,m): #Aqui k=TT
        Rv=[]
        Rcte=self.funcion_rescate(self.TT)
        for j in range(self.TT):
            Rv.append(self.Reserva1t(edad, j, m)*Rcte[j]*0.95)
        return Rv
    
        
    def SeguroSaldadot(self,edad,t,m):
        vr=self.valor_rescate(edad,m)
        kpxtT=self._kpxT(edad,t)
        qxtk1=self._qxtk1(edad,t)
        z=self._z_vector(t)
        P1=[]
        for k in range(self._n-t):
            P1.append(kpxtT[k]*qxtk1[k]*z[k])
    
        return vr[t]/sum(P1)
    
    
    def SeguroProrrogadot(self,edad,t,m):
        kpxtT=self._kpxT(edad,t)
        qxtk1=self._qxtk1(edad,t)
        z=self._z_vector(t)
        VR=self.valor_rescate(edad, m)
        P1=[]
        b1t=self.b1['beneficio por muerte']
        for k in range(self._n-t):
            P1.append( kpxtT[k]*qxtk1[k]*z[k]*b1t[k])
            
        return (VR[t]/sum(P1))*3
    
    def graficar_reserva(self,edad,m,t=0,num=1):
        reservas=[]
        tiempos=[]
        if(num==1):
            for j in range(t+1):
                reservas.append(self.Reserva1t(edad, j, m))
                tiempos.append(j)
            plt.ylabel('Reserva (1) a tiempo ')
            plt.plot(reservas,color = 'r')
        elif(num==2):
            for j in range(t+1):
                reservas.append(self.Reserva2t(edad, j, m))
                tiempos.append(j)
            plt.plot(reservas,color = '#4CAF50')
            plt.ylabel('Reserva (2) a tiempo ')
        elif(num==3):
            for j in range(t+1):
                reservas.append(self.Reserva3t(edad, j, m))
                tiempos.append(j)
            plt.ylabel('Reserva (1) a tiempo ')
            plt.plot(reservas,color = 'y')
        plt.title(f'Reserva ({num})')
        plt.xlabel('Tiempo t')
        plt.show()  
    
    def graficar_reserva_total(self,edad,m,t=0):
        reservas=[]
        tiempos=[]
        for i in range(t+1):
            reservas.append(self.ReservaTotalt(edad, t, m))
            tiempos.append(i)
        plt.title("Reserva Total")
        plt.ylabel("Reserva total a tiempo t")
        plt.xlabel('Tiempo t')
        plt.plot(tiempos, color='#008000')
        plt.show()  
            
    def graficar_func_rescate(self,n,t=0):
        datos=[]
        for i in range(t+1):
            datos.append(self.funcion_rescate(n)[i])
        plt.plot(datos,color='#49a782')
        plt.title("Funcion Rescate")
        plt.xlabel('Función de Rescate')
        plt.ylabel('Porcentaje de devolución')
        plt.show()
        
    def graficar_valor_rescate(self,edad,m,t=0):
        valorR=[]
        rv=[]
        for i in range(t):
            valorR.append(self.valor_rescate(edad,m)[i])
        for i in range(t+1):
            rv.append(self.Reserva1t(edad,i,m))
        plt.plot(valorR)
        plt.plot(rv)
        plt.title("Valor rescate")
        plt.xlabel('Tiempo t')
        plt.ylabel('Valor de Rescate')
        plt.show()
    
    def graficar_Seguro_saldado(self,edad,m,t=0):
        seguro=[]
        for i in range(t):
            seguro.append(self.SeguroSaldadot(edad, i, m))
        plt.plot(seguro,color='black')
        plt.title("Seguro saldado")
        plt.xlabel("Tiempo t")
        plt.ylabel('Seguro Saldado')
        plt.show()
        
    def graficar_Seguro_prorrogrado(self,edad,m,t=0):
        data=[]
        for i in range(t):
            data.append(self.SeguroProrrogadot(edad, i, m))
        plt.plot(data,color='#ff8f00')
        plt.title("seguro prorrogrado")
        plt.xlabel("Tiempo t")
        plt.ylabel('Seguro Prorrogrado')
        plt.show()
            
        
        