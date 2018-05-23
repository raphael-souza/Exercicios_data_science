import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np 
tips = sns.load_dataset('tips')

print(tips[0:10])

# displot cria histograma e cria um KDE
#sns.distplot(tips['total_bill'])
#sns.distplot(tips['total_bill'],kde=False)
#sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')
#sns.rugplot(tips['total_bill'])


#PLOTS CATEGORICOS -> contem textos

#sns.barplot(x='sex', y='total_bill', data=tips )

crr = tips.corr()

#sns.heatmap(crr, cmap='coolwarm', annot = True)  # mapa de calor

fights = sns.load_dataset('flights')
pf = fights.pivot_table(values='passengers',index='month',columns='year')

print(fights)

sns.heatmap(pf,linecolor ='blue', linewidths=1)
sns.clustermap(pf) # separar em grupos similares
plt.show()
