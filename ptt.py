import matplotlib.pyplot as plt
import matplotlib
from matplotlib.pyplot import MultipleLocator

x = [[0,1,2,3,4,5,6,7,8,9,10]]
y = [[80,56,54.5,53.5,52.5,51.5,50.5,49.5,48,47,46],
     [80,58,57,56,55,54,54,53,52,51.5,50.5],
     [80,56,54,53.5,53,53,52,51.5,50,49.5,49.5]]
matplotlib.rc('font', family='Microsoft JhengHei')

fig , ax = plt.subplots()
ax.plot(x[0], y[0], 'ro-', label = '甲(7.5mm)' ,) 
ax.plot(x[0], y[1], 'go--', label = '乙(2mm)')
ax.plot(x[0], y[2], 'yo-.', label = '丙(1mm)')

ax.set(xlabel ='time(min)' , ylabel ='temperature(°C)', title = '不同口徑容器對咖啡牛奶溫度影響折線圖', )
ax.legend(    
    loc= 'best',
    fontsize= 10,
    shadow= True,
    title= 'legend',
    title_fontsize= 20)
x_major_locator = MultipleLocator(1)
# y_major_locator = MultipleLocator(1)

ax.xaxis.set_major_locator(x_major_locator)
# ax.yaxis.set_major_locator(y_major_locator)

plt.show()


# plt.plot(x[0], y[0], 'ro-')   
# plt.plot(x[0], y[1], 'go--')  
# plt.plot(x[0], y[2], 'yo--')  
# plt.show()