# Interactive Python Programming (Part 1)

# Quiz 1

# Q6
import math

def f(x):
    y = -5*math.pow(x,5) + 69*math.pow(x,2) - 47
    return y
    
print f(0)
print f(1)
print f(2)


# Q7

def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    pv = present_value
    fv = pv
    
    for i in range(0,periods):
        fv = pv * (1+rate_per_period)
        pv = fv
    return pv
    
print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)
    
# Q8

import math

def polygon_area(n, s):
    area = (.25 * n * math.pow(s,2)) / math.tan((math.pi/n))
    return area
    
print polygon_area(7,3)

# Q10

import math

def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)    
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale
    
project_to_distance(2, 7, 4)