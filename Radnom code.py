import matplotlib.pyplot as plt
import numpy as np

s = 3.814       # km of swimming in Triathlon
b = 180.2       # km of biking in Triathlon
r = 41.9        # km of running in Triathlon
td = s + b + r  # total distance covered

speed_s = 3   # min / 100m
speed_b = 32.5    # km / h
speed_r = 5.6   # min / km

def hm(hours_float: float) -> tuple[int, int]:
    """Return (hours, minutes) rounded to the nearest minute."""
    h = int(hours_float)
    m = int(round((hours_float - h) * 60))
    # put 60-minute roll-overs back into the hours part
    if m == 60:
        h += 1
        m = 0
    return h, m

time_s = s * 10 * speed_s /60       # Time swimming minutes
time_b = (b / speed_b)     # Time biking minutes
time_r = r * speed_r   / 60         # Time running minutes

Total_T = time_s + time_b + time_r  # Total IronMan time in minutes
Total_T_h = Total_T / 60            # Total IronMan time in hours

# — Cumulative arrays
t_min  = np.cumsum([0, time_s, time_b, time_r])           # [0, T_swim, T_swim+T_bike, total]
t_h = t_min 
d_km   = np.cumsum([0, s, b, r])        # [0, D_swim, D_swim+Bike, total]

print(f"Swim:  {hm(time_s)[0]} h {hm(time_s)[1]:02d} min")
print(f"Bike:  {hm(time_b)[0]} h {hm(time_b)[1]:02d} min")
print(f"Run:   {hm(time_r)[0]} h {hm(time_r)[1]:02d} min")
print(f"TOTAL: {hm(Total_T)[0]} h {hm(Total_T)[1]:02d} min")

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

# This will be comitted to side 2