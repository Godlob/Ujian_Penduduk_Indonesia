import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('indo_12_1.xls', na_values='-')
df.columns = ['Provinsi',1971,1980,1990,1995,2000,2010]
df = df.drop([0,1,2,37,38])
df = df.reset_index(drop=True)
df.iloc[:,1:] = df.values[:,1:]/100000000
# print(df)
#Jumlah penduduk Indonesia
# print(df[df[2010]==df[2010].max()])
idnidx = df[2010].idxmax()
# provinsi dengan penduduk terbanyak th 2010
df2 = df[df[2010]==df[2010].nlargest(2).iloc[-1]]
#provinsi dengan penduduk tersedikit 1971
minidx = df[1971].idxmin()
plt.figure('Figure 1')
plt.style.use('ggplot')
plt.grid(color='w', linestyle='solid')
plt.plot(df.columns[1:],df.values[idnidx,1:], color='r')
plt.scatter(df.columns[1:],df.values[idnidx,1:], color='r')
plt.plot(df.columns[1:],df2.values[0,1:],color='g')
plt.scatter(df.columns[1:],df2.values[0,1:],color='g')
plt.plot(df.columns[1:],df.values[minidx,1:],color='b')
plt.scatter(df.columns[1:],df.values[minidx,1:], color='b')
plt.title('Jumlah Penduduk INDONESIA (1971-2010)')
plt.xlabel('Tahun')
plt.ylabel('Jumlah Penduduk (ratus juta jiwa)')
plt.legend([df.values[idnidx,0],df2.values[0,0],df.values[minidx,0]])
plt.show()
