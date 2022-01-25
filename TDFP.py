# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 09:58:20 2022

@author: victo
"""

import data_process as dp


class TDFP(dp.Data_process):
    
    
    def calcular_seguro(self,edad,m):
        P=self.prima_riesgo(edad)
        A=self.anualidad(edad, m)
        PNN=P/A
        PT=PNN/(1-self.alpha-self.beta-self.gamma)
        print("La Prima de Riesgo es:", P)
        print("La Anualidad es:", A)
        print("La Prima Neta Nivelada es:", PNN)
        print("La Prima de Tarifa es:", PT)