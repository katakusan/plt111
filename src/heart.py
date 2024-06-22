import matplotlib.pyplot as plt
import matplotlib
from matplotlib.pyplot import MultipleLocator

x = [[5,15,25,35,45,55,65]]
y = [[62,62,64,56,58,57,62],
     [62,62,84,80,69,82,79]]
matplotlib.rc('font', family='Microsoft JhengHei')

fig , ax = plt.subplots()
ax.plot(x[0], y[0], 'ro-', label ='坐著' ) 
ax.plot(x[0], y[1], 'go--', label = '深蹲')

ax.set(xlabel ='time(s)' , ylabel ='心搏次數平均(次)', title = '受試者不同狀態下對平均心搏次數影響折線圖', )
ax.legend(    
    loc= 'best',
    fontsize= 10,
    shadow= True,
    title= 'legend',
    title_fontsize= 20)
x_major_locator = MultipleLocator(5)
# y_major_locator = MultipleLocator(1)

ax.xaxis.set_major_locator(x_major_locator)
# ax.yaxis.set_major_locator(y_major_locator)

plt.show()


# plt.plot(x[0], y[0], 'ro-')   
# plt.plot(x[0], y[1], 'go--')  
# plt.plot(x[0], y[2], 'yo--')  
# plt.show()