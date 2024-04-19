min = 1000
max = 0

@onevent
def acc():
    global min, max
    min = acc[2] if acc[2] < min else min
    max = acc[2] if acc[2] > max else max
    print(acc[2], min, max)
    
    
timer_period[0] = 2000
@onevent
def timer0():
    global motor_left_target, motor_right_target        
    motor_right_target = 200
    motor_left_target = 200
