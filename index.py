
###EJEMPLO DE USP

import TDFP as BEP #Bases de experiencia propia
import TDCNSF as CNSF #Bases de experiencia de mercado de la CNSF



table_TDFP=BEP.TDFP('Tabladecremento1Experienciapropia.csv',
                    'Tabladecremento2Experienciapropia .csv', 
                    'Tabladecremento3Experienciapropia.csv')

table_TDCNSF=CNSF.TDCNSF('TablaCNSFdecremento1.csv',
                         'TablaCNSFdecremento2.csv',
                         'TablaCNSFdecremento3.csv')

table_TDFP.show_beneficios()
table_TDFP.show_table_head()
print('los parametros son')
table_TDFP.show_parametros()
table_TDCNSF.show_table_head()

table_TDCNSF.CalcularReservat(50, 0, 5)

table_TDCNSF.graficar_reserva(50,5,10,1)
table_TDCNSF.graficar_reserva(50,5,10,2)
table_TDCNSF.graficar_reserva(50,5,10,3)
table_TDCNSF.graficar_func_rescate(10,10)
table_TDCNSF.graficar_valor_rescate(50,5,10)
table_TDCNSF.graficar_Seguro_saldado(50,5,10)
table_TDCNSF.graficar_Seguro_prorrogrado(50, 5,10)
