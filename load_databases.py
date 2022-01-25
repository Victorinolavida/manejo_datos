import pandas as pd
import itertools
import math



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
    i=0.422
    n=10
    alpha=0.35
    beta=0.22
    gamma=0.175
    path='C:/Users/victo/Downloads/Basededatos/'
    def __init__(self,path1,path2,path3):
        self.base1=pd.read_csv(self.path+path1)
        self.base2=pd.read_csv(self.path+path2)
        self.base3=pd.read_csv(self.path+path3)
        self.data=[self.base1,self.base1,self.base1]
        self.table=self.cal_table_TDFP()
        self.b1=B1
        self.b2=B2
        self.b3=B3
        
 
    
    def cal_table_TDFP(self):
        
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
                salida.append(first[i]*(a-b+c))
            
        calc_qxi(data_qx1, data_qx2, data_qx3, qx1)

        calc_qxi(data_qx2, data_qx1, data_qx3, qx2)

        calc_qxi(data_qx3, data_qx1, data_qx2, qx3)

        qxTEp=[]
        pxTEp =[]

        for i in range(len(qx1)):
            qxTEp.append(qx1[i]+qx2[i]+qx3[i])

        for i in range(len(qxTEp)):
            pxTEp.append(1-qxTEp[i])
            

            
        TDEp=pd.DataFrame({'Edad':self.base1.Edad,"qx(1)":qx1,"qx(2)":qx2,
                            "qx(3)":qx3,"qx(T)":qxTEp,"px(T)":pxTEp
                           })
        return TDEp
   

    
    
    #muestra las databases      
    def show_data(self, number=0):
        if number==1:
            print(self.data[0])
        elif number==2:
            print(self.data[1])
        elif number==3:
            print(self.data[2])
        else:
            print(self.data)
            
            
    def show_beneficios(self):
        print(B1)
        print('*'*50)
        print(B2)
        print('*'*50)
        print(B3)
        
     
    def show_tableh(self):
        print(self.TDFP_table.head())
    
    def show_parametros(self):
        print('Interes:',self.i)
        print('tiempo(años): ',self.n)
        print('Alpha: ',self.alpha)
        print('Beta: ',self.beta)
        print('Gamma: ',self.gamma)
    
    def get_table(self):
        return self.TDFP_table
    