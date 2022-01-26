
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

print(table1.ValorPresenteIngresost(50, 5, 5))
    

for i in range(1,11):
    print(table1.ValorPresenteEgresos2t(50, i))
   
print(table1.ValorPresenteEgresos2t(50, 6))


z=[]
t=6
for k in range(1,10+1-t):
    z.append(math.pow(1+0.0422,-k))
print(z)