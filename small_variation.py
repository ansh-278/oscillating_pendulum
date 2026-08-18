#this will code for small angle variation , and for that the small angle should be in between 1  to 14 degrees , after 14 degrees we see noticible change so we will take upto 13 or 14 degrees
import numpy as np
angle = float(input("Enter small angle (between 1-14 degrees)"))
theta = np.radians(angle)
#setting default values
l= 1.0 #length of the massless string
g =9.81
dt =0.01
t =0.0
omega= 0.0
theta_list=[theta]
t_list =[t]
omega_list=[omega]
print("Time(s)      Omega(1/s)   Theta(rad)")
print(f"{t: .2f}     {omega: .2f}      {np.degrees(theta):.2f}")
 #formulating 
while t <2 :
    alpha = -((g/l)*theta)
    omega += alpha*dt
    theta += omega *dt
    print(f"{t: .2f}     {omega: .2f}      {np.degrees(theta):.2f}")
    theta_list.append(theta)
    t_list.append(t)
    omega_list.append(omega)
    t+= dt

#graph 
import matplotlib.pylab as plt
fig,ax= plt.subplots(1,2, figsize=(12,5))

ax[0].plot(t_list , theta_list , label="Time vs Theta")
ax[0].set_xlabel("Time")
ax[0].set_ylabel("Theta(rad)")
ax[0].set_title("Time Vs Angle")

ax[1].plot(t_list, omega_list, "--", label= "Time VS Omega")
ax[1].set_xlabel("Time")
ax[1].set_ylabel("Omega")
ax[1].set_title("Time Vs Omega")
plt.tight_layout()
plt.show()