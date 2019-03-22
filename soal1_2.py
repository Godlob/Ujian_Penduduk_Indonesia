import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

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
line1, = plt.plot(df.columns[1:],df.values[idnidx,1:], color='r',label='Indonesia')
plt.scatter(df.columns[1:],df.values[idnidx,1:], color='r')
line2, = plt.plot(df.columns[1:],df2.values[0,1:],color='g',label='Jawa Barat')
plt.scatter(df.columns[1:],df2.values[0,1:],color='g')
line3, = plt.plot(df.columns[1:],df.values[minidx,1:],color='b',label='Bengkulu')
plt.scatter(df.columns[1:],df.values[minidx,1:], color='b')
plt.title('Jumlah Penduduk INDONESIA (1971-2010)')
plt.xlabel('Tahun')
plt.ylabel('Jumlah Penduduk (ratus juta jiwa)')
# plt.legend([df.values[idnidx,0],df2.values[0,0],df.values[minidx,0]])
# plt.show()
# print(df)
#LINEAR REGRESSION
# dfpivot = df.pivot_table(index='Provinsi', columns='Year')
idval = df.values[idnidx,1:]
model = LinearRegression()
#indo
dfmodelindo = pd.DataFrame()
dfmodelindo['year'] = df.columns[1:]
dfmodelindo['value'] = df.values[idnidx,1:]
model.fit(dfmodelindo[['year']],dfmodelindo['value'])
idn2050 = model.predict([[2050]])*100000000
idn2050 = idn2050.astype(int)
print('Prediksi jumlah penduduk Indonesia di tahun 2050:',idn2050[0])
plt.plot(df.columns[1:],model.predict(dfmodelindo[['year']]),color='y')
#jabar
dfmodeljabar = pd.DataFrame()
dfmodeljabar['year'] = df.columns[1:]
dfmodeljabar['value'] = df2.values[0,1:]
model.fit(dfmodeljabar[['year']],dfmodeljabar['value'])
jabar2050 =  model.predict([[2050]])*100000000
jabar2050 = jabar2050.astype(int)
print('Prediksi jumlah penduduk Jawa Barat di tahun 2050:',jabar2050[0])
bestfit, = plt.plot(df.columns[1:],model.predict(dfmodeljabar[['year']]),color='y',label='bestfit')
#bengkulu
dfmodelbengk = pd.DataFrame()
dfmodelbengk['year'] = df.columns[1:]
dfmodelbengk['value'] = df.values[minidx,1:]
model.fit(dfmodelbengk[['year']],dfmodelbengk['value'])
bengk2050 =  model.predict([[2050]])*100000000
bengk2050 = bengk2050.astype(int)
print('Prediksi jumlah penduduk Bengkuli di tahun 2050:',bengk2050[0])
plt.plot(df.columns[1:],model.predict(dfmodelbengk[['year']]),color='y')
plt.legend((line1, line2, line3, bestfit),(df.values[idnidx,0],df2.values[0,0],df.values[minidx,0],'Best Fit Line'))
# plt.legend([df.values[idnidx,0],df2.values[0,0],df.values[minidx,0]],handles=bestfit)
# plt.legend(handles=bestfit)

plt.show()

