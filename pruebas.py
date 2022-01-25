
import TDFP 
import TDCNSF




table=TDFP.TDFP('Tabladecremento1Experienciapropia.csv',
          'Tabladecremento2Experienciapropia .csv', 
          'Tabladecremento3Experienciapropia.csv')

table.calcular_seguro(50,5 )

table1=TDCNSF.TDCNSF('TablaCNSFdecremento1.csv',
                     'TablaCNSFdecremento2.csv',
                     'TablaCNSFdecremento3.csv')

b=table1.ReservaTotalt(50, 0, 5)

print(b)


table1.CalcularReservat(50,4,5)