import matplotlib as mlpt
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

Time = np.array(0, Total_T_h, )