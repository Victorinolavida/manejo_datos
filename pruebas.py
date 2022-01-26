
import TDFP 
import TDCNSF

import math


table=TDFP.TDFP('Tabladecremento1Experienciapropia.csv',
          'Tabladecremento2Experienciapropia .csv', 
          'Tabladecremento3Experienciapropia.csv')

#print(table.calcular_seguro(50,5 ))

table1=TDCNSF.TDCNSF('TablaCNSFdecremento1.csv',
                     'TablaCNSFdecremento2.csv',
                     'TablaCNSFdecremento3.csv')






table.calcular_seguro(50, 5)


print(table1.valor_rescate(50, 5))

for i in range(10):
    print(table1.SeguroProrrogadot(30, i, 5))