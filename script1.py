import numpy as np
import pandas as pd
a = np.array([1,2,5,6,7])
a = a*8
b  = np.array([4,5,8,6,8])
b = b-3
c = np.column_stack((a,b))#iki ayri arrayi birer sütun olarak tek bir array haline getirmeye vesile olyor
cc = pd.DataFrame(c)#parametre olarak array alabiliyor it can take an array as a parameter
cc.columns = ["X","Y"]
cc['X'] = 12*cc['X']
cc['Y'] = 6*cc['Y']
print(cc)
