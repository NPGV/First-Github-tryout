import matplotlib.pyplot as plt
import numpy as np
import math

s = 3.814       # km of swimming in Triathlon
b = 180.2       # km of biking in Triathlon
r = 41.9        # km of running in Triathlon
td = s + b + r  # total distance covered

speed_s = 1.5   # min / 100m
speed_b = 40    # km / h
speed_r = 4.1   # min / km

def hm(hours_float: float) -> tuple[int, int, int]:
    """Return (hours, minutes, seconds) rounded to the nearest minute."""
    h = int(hours_float)
    m_float = (hours_float - h) * 60
    m = int(math.floor(m_float))
    s = int(math.ceil((m_float - m) * 60))
    # put 60-minute roll-overs back into the hours part
    if s == 60:
        m += 1
        s = 0
    if m == 60:
        h += 1
        m = 0
    return h, m, s

time_s = s * 10 * speed_s /60       # Time swimming minutes
time_b = (b / speed_b)     # Time biking minutes
time_r = r * speed_r   / 60         # Time running minutes

Total_T = time_s + time_b + time_r  # Total IronMan time in minutes
Total_T_h = Total_T / 60            # Total IronMan time in hours

# — Cumulative arrays
t_min  = np.cumsum([0, time_s, time_b, time_r])           # [0, T_swim, T_swim+T_bike, total]
t_h = t_min 
d_km   = np.cumsum([0, s, b, td])        # [0, D_swim, D_swim+Bike, total]

print(f"Swim:  {hm(time_s)[0]} h {hm(time_s)[1]:02d} min {hm(time_s)[2]:02d} s")
print(f"Bike:  {hm(time_b)[0]} h {hm(time_b)[1]:02d} min {hm(time_b)[2]:02d} s")
print(f"Run:   {hm(time_r)[0]} h {hm(time_r)[1]:02d} min {hm(time_r)[2]:02d} s")
print(f"TOTAL: {hm(Total_T)[0]} h {hm(Total_T)[1]:02d} min {hm(Total_T)[2]:02d} s")

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

# Does it show this?