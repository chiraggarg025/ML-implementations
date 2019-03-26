% matplotlib auto
import numpy as np
import matplotlib.pyplot as plt


def onclick(event):
    global x,y,m,c
    x.append(event.xdata)
    y.append(event.ydata)
    X = np.array(x)
    Y = np.array(y)
    n=np.size(x) 
    
#    Linear Regression
    
    m_x, m_y = np.mean(X), np.mean(Y) 
  
    SS_xy = np.sum(Y*X) - n*m_y*m_x 
    SS_xx = np.sum(X*X) - n*m_x*m_x 
    
    m = SS_xy / SS_xx 
    c = m_y - m*m_x 
    
#    Gradient Descent
    
    alpha=0.01
    num_itr=100
    for i in range(num_itr):
        error_m=[]
        error_c=[]
        for j in range(n):
            error_m.append((Y[j]-(m*X[j])-c)*X[j])
            error_c.append((Y[j]-(m*X[j])-c))
        error_tot_m=sum(error_m)/n
        error_tot_c=sum(error_c)/n
        
        m=m+(alpha*error_tot_m)
        c=c+(alpha*error_tot_c)
    
#    Plotting graph
    
    plt.clf() 
    plt.axis([-10,10,-10,10]) 
    plt.scatter(X,Y,color='blue',s=30)
    plt.plot([-10,10],[m*(-10)+c,m*10+c],color='black')
    plt.draw()
    
m=0
c=0
x = []
y = []

fig = plt.figure(dpi = 100)
ax = fig.add_subplot(111)
ax.autoscale(False)
plt.axis([-10,10,-10,10]) 
cid = fig.canvas.mpl_connect('button_press_event', onclick)
