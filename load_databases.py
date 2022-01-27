import pandas as pd
import itertools



## Beneficio por muerte

B1=pd.DataFrame({'beneficio por muerte':
                 range(1000000,0,-100000)})
#beneficio por cancelacion

B2=pd.DataFrame({'Beneficio por cancelacion': 
                 range(10000,0,-1000)})
#beneficio por invalidez

B3=pd.DataFrame({'Benefecio por invalidez':
                 itertools.repeat(0.6*1000000,10) })



class Load_databases:
    
    path='C:/Users/victo/Downloads/Basededatos/'
    def __init__(self,path1,path2,path3):
        self.base1=pd.read_csv(self.path+path1)
        self.base2=pd.read_csv(self.path+path2)
        self.base3=pd.read_csv(self.path+path3)
        self.table=self._cal_table_TDFP()
        self.b1=B1
        self.b2=B2
        self.b3=B3
        self._i=0.0422
        self._n=10
        self._alpha=0.35
        self._beta=0.22
        self._gamma=0.175
        
 
    #privado
    def _cal_table_TDFP(self):
        
        data_qx1=list(self.base1["qx'(1)"])

        data_qx2=list(self.base2["qx'(2)Nacional"])

        data_qx3=list(self.base3["qx'(3)"])

        qx1=[]
        qx2=[]
        qx3=[]

        def calc_qxi(first,second,third,salida):
            for i in range(len(first)):
                a=1-0.5*second[i]
                b=0.5*third[i]
                c=(1/3)*third[i]*second[i]
                salida.append(round(first[i]*(a-b+c),7))
            
        calc_qxi(data_qx1, data_qx2, data_qx3, qx1)

        calc_qxi(data_qx2, data_qx1, data_qx3, qx2)

        calc_qxi(data_qx3, data_qx1, data_qx2, qx3)

        qxTEp=[]
        pxTEp =[]

        for i in range(len(qx1)):
            qxTEp.append(round(qx1[i]+qx2[i]+qx3[i],7))

        for i in range(len(qxTEp)):
            pxTEp.append(round(1-qxTEp[i],7))
            

            
        TDEp=pd.DataFrame({'Edad':self.base1.Edad,"qx(1)":qx1,"qx(2)":qx2,
                            "qx(3)":qx3,"qx(T)":qxTEp,"px(T)":pxTEp
                           })
        return TDEp
   

    def set_parametros(self,i,n,alpha,beta,gamma):
        self._i=i
        self._n=n
        self._alpha=alpha
        self._beta=beta
        self._gamma=gamma
    
    
            
    #publico
    def show_beneficios(self):
        print('    ')
        print(B1)
        print('*'*50)
        print(B2)
        print('*'*50)
        print(B3)
        print('    ')
        
     
    def show_table_head(self):
        print('    ')
        print(self.table.head())
        print('    ')
    
    def show_parametros(self):
        print('    ')
        print('Interes:',self._i)
        print('tiempo(años): ',self._n)
        print('Alpha: ',self._alpha)
        print('Beta: ',self._beta)
        print('Gamma: ',self._gamma)
        print('    ')
        
    