#importing libraries

import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt


#creating a list of terms and a list of rates
rates=[]
terms = [1,2,3,5,7,10,20,30]
for i in terms:
    tic='GS'+str(i)
    data=web.get_data_fred(tic)
    r=data[data.columns[-1]][-1]
    rates.append(r)
    
#plotting
    
fig=plt.figure(figsize=(16,6),facecolor='#07000D')
ax = plt.subplot2grid((12,4),(7,0), rowspan = 5, colspan = 4, facecolor='#07000D')

ax.grid(linestyle=':', color='w')
ax.yaxis.label.set_color('w')
ax.xaxis.label.set_color('w')
ax.spines['bottom'].set_color("y")
ax.spines['top'].set_color("y")
ax.spines['left'].set_color("y")
ax.spines['right'].set_color("y")
ax.tick_params(axis='both', which='major',colors='w', labelsize=20 , width=2)
plt.ylabel('Rate',fontsize=20)
plt.xlabel('Term',fontsize=20)
ax.plot(terms,rates, color = 'y')
plt.title('Yield Curve', color='w', fontsize = 30)
