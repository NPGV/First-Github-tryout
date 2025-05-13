import matplotlib.pyplot as plt
import numpy as np

s = 3.814       # km of swimming in Triathlon
b = 180.2       # km of biking in Triathlon
r = 41.9        # km of running in Triathlon
td = s + b + r  # total distance covered

speed_s = 2.5   # min / 100m
speed_b = 30    # km / h
speed_r = 5.6   # min / km

time_s = s * 10 * speed_s       # Time swimming minutes
time_b = (b / speed_b) * 60     # Time biking minutes
time_r = r * speed_r            # Time running minutes

Total_T = time_s + time_b + time_r  # Total IronMan time in minutes
Total_T_h = Total_T / 60            # Total IronMan time in hours

# — Cumulative arrays
t_min  = np.cumsum([0, time_s, time_b, time_r])           # [0, T_swim, T_swim+T_bike, total]
t_h = t_min / 60
d_km   = np.cumsum([0, s, b, td])        # [0, D_swim, D_swim+Bike, total]

# — Plot
plt.figure(figsize=(10, 5))
plt.plot(t_h[:2], d_km[:2], label='Swimming')            # swim line
plt.plot(t_h[1:3], d_km[1:3], label='Biking')            # bike line
plt.plot(t_h[2:], d_km[2:], label='Running')             # run line
plt.scatter(t_h[1:], d_km[1:], zorder=3)                 # transition dots

plt.xlabel('Time (hours)')
plt.ylabel('Distance (km)')
plt.title('Ironman Progression')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()