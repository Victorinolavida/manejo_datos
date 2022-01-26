
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