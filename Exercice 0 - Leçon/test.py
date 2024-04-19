min = 1000
max = 0

@onevent
def acc():
    global min, max
    min = acc[2] if acc[2] < min else min
    max = acc[2] if acc[2] > max else max
    print(acc[2], min, max)
    
@onevent
def timer0():
    global        
    motor_right_target = 200
    motor_left_target = 200
