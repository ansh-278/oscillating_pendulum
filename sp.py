import numpy as np
 # set default variables 
l,m, t =1.0,0.0,0.0
omega=0.0
degree = float(input("Enter the release angle from mean position "))
g = 9.81
dt=0.01
#setting values 
theta = np.radians(degree)
theta_list= [theta]
t_list=[t]
omega_list=[omega]
print(f"Time(s)     Omega(1/s)     Angle(deg)")
print(f"{t:.2f}           {omega: .2f}     {np.degrees(theta) : .2f}")
#initializing values and formulas
while t<8 :
    alpha = -((g/l)*np.sin(theta))
    omega= omega + alpha*dt
    theta += omega*dt
    t_list.append(t)
    theta_list.append(np.degrees(theta))
    omega_list.append(omega)
    print(f"{t:.2f}           {omega: .2f}     {np.degrees(theta) : .2f}")
    t+= dt



#plotting
import matplotlib.pylab as plt
plt.plot(t_list, theta_list, label="Time vs Theta")
plt.xlabel("Time")
plt.ylabel("Angle(degrees)")
plt.grid()
plt.show()